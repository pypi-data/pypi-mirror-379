from typing import Any, Literal, Optional

from pydantic import BaseModel


class WorkflowExecutable(BaseModel):
    node_id: Literal["Workflow"]
    inputs: dict[str, Any]


class WorkflowRecord(BaseModel):
    id: Optional[str] = None
    name: str
    owner_id: str
    created_at: Optional[str] = None
    versions: list[str] = []


class WorkflowVersion(BaseModel):
    id: Optional[str] = None
    workflow_id: Optional[str] = None
    name: str
    owner_id: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
