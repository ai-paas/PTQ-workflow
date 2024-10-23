from fastapi import APIRouter

from app.api.v1.model import router as model_router
from app.api.v1.task import router as task_router

# API 버전 관리 폴더
router = APIRouter(prefix="/v1")

router.include_router(model_router, prefix="/models", tags=["Models"])
router.include_router(task_router, prefix="/tasks", tags=["Tasks"])
