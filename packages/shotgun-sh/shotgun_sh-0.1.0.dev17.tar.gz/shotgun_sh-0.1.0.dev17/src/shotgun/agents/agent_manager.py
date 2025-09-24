"""Agent manager for coordinating multiple AI agents with shared message history."""

import logging
from collections.abc import AsyncIterable
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, cast

from pydantic_ai import (
    Agent,
    DeferredToolRequests,
    DeferredToolResults,
    RunContext,
    UsageLimits,
)
from pydantic_ai.agent import AgentRunResult
from pydantic_ai.messages import (
    AgentStreamEvent,
    FinalResultEvent,
    ModelMessage,
    ModelRequest,
    ModelResponse,
    ModelResponsePart,
    PartDeltaEvent,
    PartStartEvent,
    ToolCallPartDelta,
)
from textual.message import Message
from textual.widget import Widget

from .history.compaction import apply_persistent_compaction
from .models import AgentDeps, AgentRuntimeOptions, FileOperation
from .plan import create_plan_agent
from .research import create_research_agent
from .specify import create_specify_agent
from .tasks import create_tasks_agent

logger = logging.getLogger(__name__)


class AgentType(Enum):
    """Enumeration for available agent types (for Python < 3.11)."""

    RESEARCH = "research"
    PLAN = "plan"
    TASKS = "tasks"
    SPECIFY = "specify"


class MessageHistoryUpdated(Message):
    """Event posted when the message history is updated."""

    def __init__(
        self,
        messages: list[ModelMessage],
        agent_type: AgentType,
        file_operations: list[FileOperation] | None = None,
    ) -> None:
        """Initialize the message history updated event.

        Args:
            messages: The updated message history.
            agent_type: The type of agent that triggered the update.
            file_operations: List of file operations from this run.
        """
        super().__init__()
        self.messages = messages
        self.agent_type = agent_type
        self.file_operations = file_operations or []


class PartialResponseMessage(Message):
    """Event posted when a partial response is received."""

    def __init__(self, message: ModelResponse | None, is_last: bool) -> None:
        """Initialize the partial response message."""
        super().__init__()
        self.message = message
        self.is_last = is_last


@dataclass(slots=True)
class _PartialStreamState:
    """Tracks partial response parts while streaming a single agent run."""

    parts: list[ModelResponsePart | ToolCallPartDelta] = field(default_factory=list)
    latest_partial: ModelResponse | None = None
    final_sent: bool = False


class AgentManager(Widget):
    """Manages multiple agents with shared message history."""

    def __init__(
        self,
        deps: AgentDeps | None = None,
        initial_type: AgentType = AgentType.RESEARCH,
    ) -> None:
        """Initialize the agent manager.

        Args:
            deps: Optional agent dependencies. If not provided, defaults to interactive mode.
        """
        super().__init__()
        self.display = False

        # Use provided deps or create default with interactive mode
        self.deps = deps

        if self.deps is None:
            raise ValueError("AgentDeps must be provided to AgentManager")

        # Create AgentRuntimeOptions from deps for agent creation
        agent_runtime_options = AgentRuntimeOptions(
            interactive_mode=self.deps.interactive_mode,
            working_directory=self.deps.working_directory,
            max_iterations=self.deps.max_iterations,
            queue=self.deps.queue,
            tasks=self.deps.tasks,
        )

        # Initialize all agents and store their specific deps
        self.research_agent, self.research_deps = create_research_agent(
            agent_runtime_options=agent_runtime_options
        )
        self.plan_agent, self.plan_deps = create_plan_agent(
            agent_runtime_options=agent_runtime_options
        )
        self.tasks_agent, self.tasks_deps = create_tasks_agent(
            agent_runtime_options=agent_runtime_options
        )
        self.specify_agent, self.specify_deps = create_specify_agent(
            agent_runtime_options=agent_runtime_options
        )

        # Track current active agent
        self._current_agent_type: AgentType = initial_type

        # Maintain shared message history
        self.ui_message_history: list[ModelMessage] = []
        self.message_history: list[ModelMessage] = []
        self.recently_change_files: list[FileOperation] = []
        self._stream_state: _PartialStreamState | None = None

    @property
    def current_agent(self) -> Agent[AgentDeps, str | DeferredToolRequests]:
        """Get the currently active agent.

        Returns:
            The currently selected agent instance.
        """
        return self._get_agent(self._current_agent_type)

    def _get_agent(
        self, agent_type: AgentType
    ) -> Agent[AgentDeps, str | DeferredToolRequests]:
        """Get agent by type.

        Args:
            agent_type: The type of agent to retrieve.

        Returns:
            The requested agent instance.
        """
        agent_map = {
            AgentType.RESEARCH: self.research_agent,
            AgentType.PLAN: self.plan_agent,
            AgentType.TASKS: self.tasks_agent,
            AgentType.SPECIFY: self.specify_agent,
        }
        return agent_map[agent_type]

    def _get_agent_deps(self, agent_type: AgentType) -> AgentDeps:
        """Get agent-specific deps by type.

        Args:
            agent_type: The type of agent to retrieve deps for.

        Returns:
            The agent-specific dependencies.
        """
        deps_map = {
            AgentType.RESEARCH: self.research_deps,
            AgentType.PLAN: self.plan_deps,
            AgentType.TASKS: self.tasks_deps,
            AgentType.SPECIFY: self.specify_deps,
        }
        return deps_map[agent_type]

    def _create_merged_deps(self, agent_type: AgentType) -> AgentDeps:
        """Create merged dependencies combining shared and agent-specific deps.

        This preserves the agent's system_prompt_fn while using shared runtime state.

        Args:
            agent_type: The type of agent to create merged deps for.

        Returns:
            Merged AgentDeps with agent-specific system_prompt_fn.
        """
        agent_deps = self._get_agent_deps(agent_type)

        # Ensure shared deps is not None (should be guaranteed by __init__)
        if self.deps is None:
            raise ValueError("Shared deps is None - this should not happen")

        # Create new deps with shared runtime state but agent's system_prompt_fn
        # Use a copy of the shared deps and update the system_prompt_fn
        merged_deps = self.deps.model_copy(
            update={"system_prompt_fn": agent_deps.system_prompt_fn}
        )

        return merged_deps

    def set_agent(self, agent_type: AgentType) -> None:
        """Set the current active agent.

        Args:
            agent_type: The agent type to activate (AgentType enum or string).

        Raises:
            ValueError: If invalid agent type is provided.
        """
        try:
            self._current_agent_type = AgentType(agent_type)
        except ValueError:
            raise ValueError(
                f"Invalid agent type: {agent_type}. Must be one of: {', '.join(e.value for e in AgentType)}"
            ) from None

    async def run(
        self,
        prompt: str | None = None,
        *,
        deps: AgentDeps | None = None,
        usage_limits: UsageLimits | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        **kwargs: Any,
    ) -> AgentRunResult[str | DeferredToolRequests]:
        """Run the current agent with automatic message history management.

        This method wraps the agent's run method, automatically injecting the
        shared message history and updating it after each run.

        Args:
            prompt: Optional prompt to send to the agent.
            deps: Optional dependencies override (defaults to manager's deps).
            usage_limits: Optional usage limits for the agent run.
            deferred_tool_results: Optional deferred tool results for continuing a conversation.
            **kwargs: Additional keyword arguments to pass to the agent.

        Returns:
            The agent run result.
        """
        # Use merged deps (shared state + agent-specific system prompt) if not provided
        if deps is None:
            deps = self._create_merged_deps(self._current_agent_type)

        # Ensure deps is not None
        if deps is None:
            raise ValueError("AgentDeps must be provided")

        if prompt:
            self.ui_message_history.append(ModelRequest.user_text_prompt(prompt))
        self._post_messages_updated()

        # Ensure system prompt is added to message history before running agent
        from pydantic_ai.messages import SystemPromptPart

        from shotgun.agents.common import add_system_prompt_message

        # Start with persistent message history
        message_history = self.message_history

        # Check if the message history already has a system prompt
        has_system_prompt = any(
            hasattr(msg, "parts")
            and any(isinstance(part, SystemPromptPart) for part in msg.parts)
            for msg in message_history
        )

        # Always ensure we have a system prompt for the agent
        # (compaction may remove it from persistent history, but agent needs it)
        if not has_system_prompt:
            message_history = await add_system_prompt_message(deps, message_history)

        # Run the agent with streaming support (from origin/main)
        self._stream_state = _PartialStreamState()

        model_name = ""
        if hasattr(deps, "llm_model") and deps.llm_model is not None:
            model_name = deps.llm_model.name
        is_gpt5 = (  # streaming is likely not supported for gpt5. It varies between keys.
            "gpt-5" in model_name.lower()
        )

        try:
            result: AgentRunResult[
                str | DeferredToolRequests
            ] = await self.current_agent.run(
                prompt,
                deps=deps,
                usage_limits=usage_limits,
                message_history=message_history,
                deferred_tool_results=deferred_tool_results,
                event_stream_handler=self._handle_event_stream if not is_gpt5 else None,
                **kwargs,
            )
        finally:
            # If the stream ended unexpectedly without a final result, clear accumulated state.
            if self._stream_state is not None and not self._stream_state.final_sent:
                partial_message = self._build_partial_response(self._stream_state.parts)
                if partial_message is not None:
                    self._post_partial_message(partial_message, True)
            self._stream_state = None

        self.ui_message_history = self.ui_message_history + [
            mes for mes in result.new_messages() if not isinstance(mes, ModelRequest)
        ]

        # Apply compaction to persistent message history to prevent cascading growth
        all_messages = result.all_messages()
        self.message_history = await apply_persistent_compaction(all_messages, deps)

        # Log file operations summary if any files were modified
        file_operations = deps.file_tracker.operations.copy()
        self.recently_change_files = file_operations

        self._post_messages_updated(file_operations)

        return result

    async def _handle_event_stream(
        self,
        _ctx: RunContext[AgentDeps],
        stream: AsyncIterable[AgentStreamEvent],
    ) -> None:
        """Process streamed events and forward partial updates to the UI."""

        state = self._stream_state
        if state is None:
            state = self._stream_state = _PartialStreamState()

        partial_parts = state.parts

        async for event in stream:
            try:
                if isinstance(event, PartStartEvent):
                    index = event.index
                    if index < len(partial_parts):
                        partial_parts[index] = event.part
                    elif index == len(partial_parts):
                        partial_parts.append(event.part)
                    else:
                        logger.warning(
                            "Received PartStartEvent with out-of-bounds index",
                            extra={"index": index, "current_len": len(partial_parts)},
                        )
                        partial_parts.append(event.part)

                    partial_message = self._build_partial_response(partial_parts)
                    if partial_message is not None:
                        state.latest_partial = partial_message
                        self._post_partial_message(partial_message, False)

                elif isinstance(event, PartDeltaEvent):
                    index = event.index
                    if index >= len(partial_parts):
                        logger.warning(
                            "Received PartDeltaEvent before corresponding start event",
                            extra={"index": index, "current_len": len(partial_parts)},
                        )
                        continue

                    try:
                        updated_part = event.delta.apply(
                            cast(ModelResponsePart, partial_parts[index])
                        )
                    except Exception:  # pragma: no cover - defensive logging
                        logger.exception(
                            "Failed to apply part delta", extra={"event": event}
                        )
                        continue

                    partial_parts[index] = updated_part

                    partial_message = self._build_partial_response(partial_parts)
                    if partial_message is not None:
                        state.latest_partial = partial_message
                        self._post_partial_message(partial_message, False)

                elif isinstance(event, FinalResultEvent):
                    final_message = (
                        state.latest_partial
                        or self._build_partial_response(partial_parts)
                    )
                    self._post_partial_message(final_message, True)
                    state.latest_partial = None
                    state.final_sent = True
                    partial_parts.clear()
                    self._stream_state = None
                    break

                # Ignore other AgentStreamEvent variants (e.g. tool call notifications) for partial UI updates.

            except Exception:  # pragma: no cover - defensive logging
                logger.exception(
                    "Error while handling agent stream event", extra={"event": event}
                )

    def _build_partial_response(
        self, parts: list[ModelResponsePart | ToolCallPartDelta]
    ) -> ModelResponse | None:
        """Create a `ModelResponse` from the currently streamed parts."""

        completed_parts = [
            part for part in parts if not isinstance(part, ToolCallPartDelta)
        ]
        if not completed_parts:
            return None
        return ModelResponse(parts=list(completed_parts))

    def _post_partial_message(
        self, message: ModelResponse | None, is_last: bool
    ) -> None:
        """Post a partial message to the UI."""
        self.post_message(PartialResponseMessage(message, is_last))

    def _post_messages_updated(
        self, file_operations: list[FileOperation] | None = None
    ) -> None:
        # Post event to notify listeners of the message history update
        self.post_message(
            MessageHistoryUpdated(
                messages=self.ui_message_history.copy(),
                agent_type=self._current_agent_type,
                file_operations=file_operations,
            )
        )
