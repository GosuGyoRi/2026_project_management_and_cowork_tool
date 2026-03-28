from fastapi import APIRouter

from app.api.v1.endpoints import auth, users, workspaces, projects, tasks, comments, notifications

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(workspaces.router, prefix="/workspaces", tags=["workspaces"])
api_router.include_router(projects.router, prefix="/workspaces/{workspace_id}/projects", tags=["projects"])
api_router.include_router(tasks.router, prefix="/projects/{project_id}/tasks", tags=["tasks"])
api_router.include_router(comments.router, prefix="/tasks/{task_id}/comments", tags=["comments"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
