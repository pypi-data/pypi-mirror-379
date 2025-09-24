import httpx
import os
from ..common import create_logger
from .chat_model_client import ChatModelClient, UsageMetadata
from .state import AgentState, AgentTaskResult
from a2a.types import (
    AgentCard,
    SendStreamingMessageRequest,
    SendStreamingMessageSuccessResponse,
)
from a2a.client import A2AClient
from abc import ABC
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command
from typing import AsyncIterable, Literal, Mapping, Optional

USAGE_METADATA_KEY = "usage"

class AgentGraph(ABC):
    """Abstract base class for agent graphs.
    
    Extend this class to implement the specific behavior of an agent.

    Example:
    ```python
    from br_rapp_sdk.agents import AgentGraph, AgentState
    from langgraph.runnables import RunnableConfig
    from langgraph.graph import StateGraph

    class MyAgentState(BaseModel):
        # Your state here
        # ...
        pass

    class MyAgentGraph(AgentGraph):
        def __init__(self):
            # Define the agent graph using langgraph.graph.StateGraph class
            graph_builder = StateGraph(MyAgentState)
            # Add nodes and edges to the graph as needed ...
            super().__init__(
                graph_builder=graph_builder,
                use_checkpoint=True,
                logger_name="my_agent"
            )
            self._log("Graph initialized", "info")
        
        # Your nodes logic here
        # ...
    """

    _graph: CompiledStateGraph
    _AgentStateType: type[AgentState]

    def __init__(
        self,
        graph_builder: StateGraph,
        use_checkpoint: bool = False,
        logger_name: Optional[str] = None,
    ):
        """Initialize the AgentGraph with a state graph and optional checkpointing and logger.
        Compile the state graph and set up the logger if the logger_name is provided.

        Args:
            graph_builder (StateGraph): The state graph builder.
            use_checkpoint (bool): Whether to use checkpointing. Defaults to False.
            logger_name (Optional[str]): The name of the logger to use. Defaults to None.
        """
        self._logger = None if logger_name is None else create_logger(
            name=logger_name,
            level=os.getenv("LOG_LEVEL", "info").lower(),
        )
        self._memory = MemorySaver() if use_checkpoint else None
        self._graph = graph_builder.compile(
            checkpointer=self._memory
        )
        self._AgentStateType = graph_builder.state_schema
        print(type(self._AgentStateType))
        self._usage_buffer = UsageMetadata()

    def _log(
        self,
        message: str,
        level: Literal["info", "debug", "warning", "error", "critical"],
        exc_info: bool = None,
        extra: Mapping[str, object] | None = None
    ) -> None:
        """Log a message using the logger if the logger_name was provided in the constructor."""
        if not self._logger:
            return
        
        if level == "info":
            self._logger.info(message, extra=extra, exc_info=exc_info)
        elif level == "debug":
            self._logger.debug(message, extra=extra, exc_info=exc_info)
        elif level == "warning":
            self._logger.warning(message, extra=extra, exc_info=exc_info)
        elif level == "error":
            self._logger.error(message, extra=extra, exc_info=exc_info)
        elif level == "critical":
            self._logger.critical(message, extra=extra, exc_info=exc_info)
        else:
            raise ValueError(f"Invalid log level: {level}")
    
    async def astream(
        self,
        query: str,
        config: RunnableConfig,
    ) -> AsyncIterable[AgentTaskResult]:
        """Asynchronously stream results from the agent graph based on the query and configuration.
        This method performes the following steps:
        1. Looks for a checkpoint associated with the provided configuration.
        2. If no checkpoint is found, creates a new agent state from the query, 
            using the `from_query` method of the `AgentStateType`.
        3. If a checkpoint is found, restores the state from the checkpoint and updates it with the query
            using the `update_after_checkpoint_restore` method.
        4. Prepares the input for the graph execution, wrapping the state in a `Command` if the
            `is_waiting_for_human_input` method of the state returns `True`.
        5. Executes the graph with the `astream` method, passing the input and configuration.
        6. For each item in the stream:
            - If it is an interrupt, yields an `AgentTaskResult` with the status
            `input_required`. This enables human-in-the-loop interactions.
            - Otherwise, validates the item as an `AgentStateType` and converts it to an
            `AgentTaskResult` using the `to_task_result` method of the state. Then it yields the result.

        This method prints debug logs in the format `[<thread_id>]: <message>`.
        
        Args:
            query (str): The query to process.
            config (RunnableConfig): Configuration for the runnable.
        Returns:
            AsyncIterable[AgentTaskResult]: An asynchronous iterable of agent task results.
        """
        thread_id = config.get("configurable", {}).get("thread_id")

        checkpoint = self._memory.get(config) if self._memory else None
        if checkpoint is None:
            self._log(f"[{thread_id}]: No checkpoint", "debug")
            state = self._AgentStateType.from_query(query)
            self._log(f"[{thread_id}]: State initialized", "debug")
        else:
            self._log(f"[{thread_id}]: Checkpoint found", "debug")
            channel_values = checkpoint.get("channel_values", {})
            state = self._AgentStateType.model_validate(channel_values)
            self._log(f"[{thread_id}]: State restored", "debug")
            state.update_after_checkpoint_restore(query)
            self._log(f"[{thread_id}]: State updated", "debug")

        input = Command(resume=state) if state.is_waiting_for_human_input() else state
        
        stream = self._graph.astream(
            input=input,
            config=config,
            stream_mode="values",
            subgraphs=True,
        )
        self._log(f"[{thread_id}]: Graph execution started {'with Command' if state.is_waiting_for_human_input() else ''}", "debug")

        try:
            async for item in stream:
                try:
                    state_item = self._AgentStateType.model_validate(item[1])
                    task_result_item = state_item.to_task_result()
                    self._log(f"[{thread_id}]: Yielding AgentTaskResult: [{task_result_item.task_status}] {task_result_item.content}", "debug")
                    yield task_result_item
                except Exception as ve:
                    self._logger.error(f"[{thread_id}]: Validation error: {ve}")
                    yield AgentTaskResult(
                        task_status="error",
                        content="Invalid state format",
                    )
        except Exception as e:
            self._logger.error(f"[{thread_id}]: Error during stream processing: {e}")
            yield AgentTaskResult(
                task_status="error",
                content=f"Stream error: {str(e)}",
            )
        
        # Checkpoints are possible only if memory is enabled
        if self._memory:
            current_state = self._graph.get_state(config=config)
            intr = current_state.tasks[0].interrupts[0] if current_state.tasks else None
            if intr:
                self._log(f"[{thread_id}]: Yielding Interrupt: {intr.value}", "debug")
                yield AgentTaskResult(
                    task_status="input_required",
                    content=intr.value,
                )
        self._log(f"[{thread_id}]: Graph execution completed", "debug")

    async def consume_agent_stream(
        self,
        agent_card: AgentCard,
        request: SendStreamingMessageRequest,
    ) -> AsyncIterable[SendStreamingMessageSuccessResponse]:
        """Consume the agent stream from another A2A agent using the provided agent card and request.
        
        Args:
            agent_card (AgentCard): The agent card of the target agent.
            request (SendStreamingMessageRequest): The request to send to the agent.
        
        Yields:
            AsyncIterable[SendStreamingMessageSuccessResponse]: An asynchronous iterable of streaming message responses.
        """
        async with httpx.AsyncClient() as httpx_client:
            client = A2AClient(
                agent_card=agent_card,
                httpx_client=httpx_client,
            )
            stream = client.send_message_streaming(request)
            try:
                async for item in stream:
                    if isinstance(item, SendStreamingMessageSuccessResponse):
                        result = item.root.result
                        if result.metadata and USAGE_METADATA_KEY in result.metadata:
                            usage = result.metadata[USAGE_METADATA_KEY]
                            self._usage_buffer += UsageMetadata.model_validate(usage)
                    # TODO: handle errors
                    yield item
            except Exception as e:
                self._log(f"Node `agent_call`: Streaming failed: {e}", "error")
                raise

    def draw_mermaid(
        self,
        file_path: Optional[str] = None,
    ) -> None:
        """Draw the agent graph in Mermaid format. If a file path is provided, save the diagram to
        the file, otherwise print it to the console.

        Args:
            file_path (Optional[str]): The path to the file where the Mermaid diagram should be saved.
        """
        mermaid_str = self._graph.get_graph().draw_mermaid()
        if file_path:
            with open(file_path, "w") as f:
                f.write(mermaid_str)
        else:
            print(mermaid_str)

    def _pop_usage_metadata_from_buf(
        self,
    ) -> UsageMetadata:
        """Pop the usage metadata from the buffer and return it."""
        usage = self._usage_buffer
        self._usage_buffer = UsageMetadata()
        return usage

    def _get_usage_metadata(
        self,
        from_timestamp: Optional[float] = None,
    ) -> UsageMetadata:
        """Get the total usage metadata for the graph including all ChatModelClient instances
            and other agents called using the `consume_agent_stream` method.

            Args:
                from_timestamp (Optional[float]): If provided, only usage after this timestamp is considered.
                    If None, all usage metadata is returned.
            Returns:
                UsageMetadata: The total usage metadata for the graph.
        """
        total = self._pop_usage_metadata_from_buf()
        for _, value in self.__dict__.items():
            if isinstance(value, ChatModelClient):
                total += value.get_usage_metadata(
                    from_timestamp=from_timestamp,
                )
        return total
