from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Any, Dict, List, Literal, Self

AgentTaskStatus = Literal["working", "input_required", "completed", "error"]
"""AgentTaskStatus is a type alias for the status of an agent task.

The possible values are:
- `working`: The agent is currently processing the task.
- `input_required`: The agent requires additional input from the user to proceed.
- `completed`: The agent has successfully completed the task.
- `error`: An error occurred during the task execution.
"""

class AgentTaskResult(BaseModel):
    """Result of an agent invocation.

    Attributes:
        task_status (AgentTaskStatus): The status of the agent task.
        content (str): The content of the agent's response or message.
    
    Attributes meaning:
    | `task_status`  | `content`                                                            |
    |----------------|----------------------------------------------------------------------|
    | working        | Ongoing task description or progress update.                         |
    | input_required | Description of the required user input or context.                   |
    | completed      | Final response or result of the agent's processing.                  |
    | error          | Error message indicating what went wrong during the task execution.  |
    """

    task_status: AgentTaskStatus
    content: str

    # override + operation
    def __add__(self, other: Self) -> Self:
        if self.task_status != other.task_status:
            raise ValueError("Cannot add AgentTaskResults with different task_status")
        return AgentTaskResult(
            task_status=other.task_status,
            content=other.content,
        )

class AgentState(BaseModel, ABC):
    """Abstract base class representing an agent's state.

    This class combines Pydantic's model validation with abstract state management
    requirements for agent operations. Subclasses should define concrete state models
    while implementing the required abstract methods.

    Note:
        Subclasses must implement all abstract methods and can define additional state
        fields using Pydantic's model field declarations.

    Abstract Methods:
        from_query: Factory method to create an agent state from an initial query
        update_after_checkpoint_restore: Refresh state after checkpoint restoration
        to_task_result: Convert current state to task result object
    
    Methods:
        is_waiting_for_human_input: Check if agent requires human input
    
    Example:
    ```python
    from br_rapp_sdk.agents import AgentState, AgentTaskResult
    from typing import List, Optional, Self
    from typing_extensions import override

    class MyAgentState(AgentState):
        user_inputs: List[str] = []
        assistant_outputs: List[str] = []
        question: str = ""
        answer: Optional[str] = None

        @classmethod
        def from_query(cls, query: str) -> Self:
            return cls(
                user_inputs=[query],
                question=query,
            )
        
        @override
        def update_after_checkpoint_restore(self, query: str) -> None:
            self.user_inputs.append(query)
            self.question = query
        
        @override
        def to_task_result(self) -> AgentTaskResult:
            if self.answer is None:
                return AgentTaskResult(
                    task_status="working",
                    content="Processing your request..."
                )
            return AgentTaskResult(
                task_status="completed",
                content=self.answer
            )
    """
    br_rapp_sdk_extra: Dict[str, Any] = {}
    br_rapp_sdk_buffer: List = []

    @classmethod
    @abstractmethod
    def from_query(
        cls,
        query: str
    ) -> Self:
        """Instantiate agent state from initial query.

        Factory method called by the execution framework to create a new state instance.
        Alternative to direct initialization, allowing state-specific construction logic.

        Args:
            query: Initial user query to bootstrap agent state

        Returns:
            Self: Fully initialized agent state instance
        """
        pass

    def update_after_checkpoint_restore(self, query: str) -> None:
        """Update state with new query after checkpoint restoration.

        Called by the SDK when restoring from a saved checkpoint. Allows the state
        to synchronize with new execution parameters before resuming the graph.

        Args:
            query: New query to execute with the restored state
        """
        pass

    @abstractmethod
    def to_task_result(self) -> AgentTaskResult:
        """Convert current state to a task result object.

        Used to yield execution results during graph processing. This method defines
        how the agent's internal state translates to external-facing task results.

        Returns:
            AgentTaskResult: Task result representation of current state
        """
        pass

    def is_waiting_for_human_input(self) -> bool:
        """Check if agent is blocked waiting for human input.

        Default implementation returns `False`. Override in subclasses to implement
        human-in-the-loop pausing behavior.

        Returns:
            bool: True if agent requires human input to proceed, False otherwise
        """
        return False
