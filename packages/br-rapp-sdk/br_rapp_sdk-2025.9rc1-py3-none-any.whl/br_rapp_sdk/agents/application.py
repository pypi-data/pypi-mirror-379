import httpx
import time
from ..common import create_logger
from .chat_model_client import UsageMetadata
from .graph import AgentGraph
from .state import AgentTaskResult
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.apps import A2AStarletteApplication
from a2a.server.events import EventQueue
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore, TaskUpdater
from a2a.types import (
    AgentCard,
    InternalError,
    InvalidParamsError,
    Part,
    Task,
    TaskState,
    TextPart,
    UnsupportedOperationError,
)
from a2a.utils import (
    new_agent_text_message,
    new_task,
)
from a2a.utils.errors import ServerError
from starlette.applications import Starlette
from typing import Dict
from typing_extensions import override, Any

_logger = create_logger("br_rapp_sdk.agents.application", "debug")

class MinimalAgentExecutor(AgentExecutor):
    """Minimal Agent Executor.
    
    Minimal implementation of the AgentExecutor interface used by the `AgentApplication` class to execute agent tasks.
    """

    def __init__(
        self,
        agent_graph: AgentGraph
    ):
        self.agent_graph = agent_graph

    @override
    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        if not self._request_ok(context):
            raise ServerError(error=InvalidParamsError())

        query = context.get_user_input()
        task = context.current_task
        if not task:
            task = new_task(context.message)
            await event_queue.enqueue_event(task)
        updater = TaskUpdater(event_queue, task.id, task.context_id)
        try:
            config = {"configurable": {"thread_id": task.context_id}}
            ts = time.time()
            keep_streaming = True
            async for item in self.agent_graph.astream(query, config):
                if keep_streaming:
                    usage_metadata = self.agent_graph._get_usage_metadata(ts)
                    ts = time.time()
                    keep_streaming = await self._process_task_result(task, item, updater, {'usage': usage_metadata})
                # else just keep consuming the stream
        except Exception as e:
            _logger.error(f'An error occurred while streaming the response: {e}')
            raise ServerError(error=InternalError()) from e

    def _request_ok(self, context: RequestContext) -> bool:
        return True

    async def _process_task_result(
        self,
        task: Task,
        task_result: AgentTaskResult,
        updater: TaskUpdater,
        metadata: Dict[str, Any]
    ) -> bool:
        keep_streaming = True
        match task_result.task_status:
            case "working":
                message = new_agent_text_message(
                    task_result.content,
                    task.context_id,
                    task.id,
                )
                message.metadata = metadata
                await updater.update_status(
                    TaskState.working,
                    message,
                )
                message.metadata = metadata
            case "input_required":
                message = new_agent_text_message(
                    task_result.content,
                    task.context_id,
                    task.id,
                )
                message.metadata = metadata
                await updater.update_status(
                    TaskState.input_required,
                    message,
                    final=True,
                )
                keep_streaming = False
            case "completed":
                await updater.add_artifact(
                    [Part(root=TextPart(text=task_result.content))],
                    metadata=metadata,
                )
                keep_streaming = False
            case "error":
                raise ServerError(error=InternalError(message=task_result.content))
            case _:
                _logger.warning(f"Unknown task status: {task_result.task_status}")
        return keep_streaming

    @override
    async def cancel(
        self, request: RequestContext, event_queue: EventQueue
    ) -> Task | None:
        raise ServerError(error=UnsupportedOperationError())

class AgentApplication:
    """Agent Application based on `Starlette`.

    Attributes:
        agent_card (AgentCard): The agent card containing metadata about the agent.
        agent_graph (AgentGraph): The agent graph that defines the agent's behavior and capabilities.
    
    Example:
    ```python
        import httpx
        import json
        import uvicorn
        from a2a.types import AgentCard
        from br_rapp_sdk.agents import AgentApplication

        with open('./agent.json', 'r') as file:
            agent_data = json.load(file)
            agent_card = AgentCard.model_validate(agent_data)
            logger.info(f'Agent Card loaded: {agent_card}')
        
        url = httpx.URL(agent_card.url)
        graph = MyAgentGraph()
        agent = AgentApplication(
            agent_card=agent_card,
            agent_graph=graph,
        )

        uvicorn.run(agent.build(), host=url.host, port=url.port)
    ```
    """

    def __init__(
        self,
        agent_card: AgentCard,
        agent_graph: AgentGraph
    ):
        """
        Initialize the AgentApplication with an agent card and agent graph.
        Args:
            agent_card (AgentCard): The agent card.
            agent_graph (AgentGraph): The agent graph implementing the agent's logic.
        """
        self._agent_executor = MinimalAgentExecutor(agent_graph)
        self.agent_card = agent_card

        self._httpx_client = httpx.AsyncClient()
        self._request_handler = DefaultRequestHandler(
            agent_executor=self._agent_executor,
            task_store=InMemoryTaskStore(),
        )
        self._server = A2AStarletteApplication(
            agent_card=self.agent_card,
            http_handler=self._request_handler
        )

    @property
    def agent_graph(self) -> AgentGraph:
        """Get the agent graph."""
        return self._agent_executor.agent_graph
    
    def build(self) -> Starlette:
        """Build the A2A Starlette application.
        
        Returns:
            Starlette: The built Starlette application.
        """
        return self._server.build()