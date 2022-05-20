from fastapi import APIRouter

from app.api.v1.endpoints import agent, developer, login, user

api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(developer.router, prefix="/developers", tags=["developers"])
api_router.include_router(agent.router, prefix="/agents", tags=["agents"])
