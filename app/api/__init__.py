from fastapi import APIRouter

from app.api.v1 import router as v1_router

# API 관련 라우트 파일들

router = APIRouter(prefix="/api")

router.include_router(v1_router)
