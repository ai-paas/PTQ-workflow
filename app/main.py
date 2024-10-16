from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import router
from app.core.db.models import model_task
from app.core.db.session import engine

model_task.Base.metadata.create_all(bind=engine)

SWAGGER_TITLE = "AI-PaaS PTQ Workflow"
SWAGGER_SUMMARY = "PTQ Workflow Backend Server"
SWAGGER_DESCRIPTION = """
주요 기능
1. Model
    - REST API를 통해 최적화 및 경량화 시킬 모델과 최적화 방법, 파라미터들을 입력 받은 후, 최적화된 모델을 MLFlow에 저장합니다.
    - PTQ 적용된 모델을 불러옵니다.
"""


app = FastAPI(
    title=SWAGGER_TITLE, summary=SWAGGER_SUMMARY, description=SWAGGER_DESCRIPTION
)

# CORS 설정
origins = [
    "*",  # 모든 출처 허용
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
