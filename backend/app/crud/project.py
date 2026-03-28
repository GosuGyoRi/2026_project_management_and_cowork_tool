import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models.project import Project, ProjectMember


class CRUDProject(CRUDBase[Project]):
    async def get_by_workspace(self, db: AsyncSession, workspace_id: uuid.UUID) -> list[Project]:
        result = await db.execute(
            select(Project).where(Project.workspace_id == workspace_id)
        )
        return list(result.scalars().all())


class CRUDProjectMember(CRUDBase[ProjectMember]):
    pass


crud_project = CRUDProject(Project)
crud_project_member = CRUDProjectMember(ProjectMember)
