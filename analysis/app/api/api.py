from fastapi import APIRouter

from app.api.endpoints import zh

api_router = APIRouter()
api_router.include_router(zh.router, prefix="/zh", tags=["zh"])
