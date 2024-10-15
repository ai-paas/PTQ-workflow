from fastapi import APIRouter

from app.api.v1.model import router as model_router

# API 버전 관리 폴더
router = APIRouter(prefix="/v1")

router.include_router(model_router, prefix="/models", tags=["Models"])
