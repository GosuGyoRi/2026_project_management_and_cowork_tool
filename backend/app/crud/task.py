import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models.task import Task, TaskAssignee


class CRUDTask(CRUDBase[Task]):
    async def get_by_project(self, db: AsyncSession, project_id: uuid.UUID) -> list[Task]:
        result = await db.execute(
            select(Task)
            .where(Task.project_id == project_id, Task.parent_task_id == None)
            .order_by(Task.order)
        )
        return list(result.scalars().all())


crud_task = CRUDTask(Task)
