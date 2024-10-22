from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.core.db.connect import SessionDepends
from app.core.db.models.model_task import ModelTask
from app.schemas.requests.task import PatchTaskForm

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
    tasks = db.query(ModelTask).all()
    return tasks


@router.get("/{task_id}")
def get_task(*, db: Session = SessionDepends, task_id: str):
    """
    Get one task by task_id
    """

    task = db.query(ModelTask).filter(ModelTask.task_uuid == task_id).first()
    return task


@router.patch("/{task_id}")
def patch_task(
    *,
    db: Session = SessionDepends,
    task_id: str,
    patch_task_form: PatchTaskForm,
):
    """
    Patch one task by task_id
    """

    task = db.query(ModelTask).filter(ModelTask.task_uuid == task_id).first()
    updates = {
        "progress_status": patch_task_form.progress_status,
        "model_path_output": patch_task_form.model_path_output,
    }
    if task:
        for key, value in updates.items():
            setattr(task, key, value)  # 속성 업데이트
        db.commit()
        db.refresh(task)
    return task
