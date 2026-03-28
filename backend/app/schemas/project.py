import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.project import ProjectStatus, ProjectMemberRole


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    color: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    status: ProjectStatus | None = None
    color: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None


class ProjectResponse(BaseModel):
    id: uuid.UUID
    workspace_id: uuid.UUID
    name: str
    description: str | None
    status: ProjectStatus
    color: str | None
    start_date: datetime | None
    end_date: datetime | None
    created_by: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True
