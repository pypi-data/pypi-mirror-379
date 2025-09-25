import enum

from pydantic import BaseModel
from pydantic import Field


class Operation(str, enum.Enum):
    CREATE = 'Create'
    READ = 'Read'
    UPDATE = 'Update'
    DELETE = 'Delete'


class Complexity(str, enum.Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'


class Task(BaseModel):
    id: str = Field(
        description="A unique identifier for the task, e.g., 'task_001'.",
    )
    description: str = Field(
        description="The natural language command to be given to the agent. Should be from a user's perspective.",
    )
    complexity: Complexity = Field(
        default=Complexity.LOW,
        description="The estimated complexity of the task: 'Low', 'Medium', or 'High'.",
    )
    operation: Operation = Field(
        default=Operation.READ,
        description="The operation to be performed in the task, e.g., 'Create'.",
    )
    category: str = Field(
        description="The functional area of the application this task belongs to, e.g., 'Project Management'.",
    )


class TaskList(BaseModel):
    tasks: list[Task]
