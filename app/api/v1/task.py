from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.core.db.connect import SessionDepends
from app.core.db.models.model_task import ModelTask
from app.services.model_service import ModelService

router = APIRouter()

"""
모델 이름을 입력받고 해당 모델을 경량화/최적화 후 mlflow에 저장하는 라우터
"""


@router.get("")
def get_tasks(
    *,
    db: Session = SessionDepends,
):
    """
    Get all tasks
    """
    ModelService.get_lite_model(
        db=db,
    )
    tasks = db.query(ModelTask).all()
    print(tasks)
    return tasks


@router.get("/{task_id}")
def get_task(*, db: Session = SessionDepends, task_id: str):
    """
    Get one task by task_id
    """
    pass
    return task_id


@router.patch("/{task_id}")
def patch_task(*, db: Session = SessionDepends, task_id: str):
    """
    Patch one task by task_id
    """
    pass
    return task_id
