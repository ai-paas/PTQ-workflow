from uuid import uuid4

from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.core.db.connect import SessionDepends
from app.schemas.requests import model
from app.services.model_service import ModelService

router = APIRouter()

"""
모델 이름을 입력받고 해당 모델을 경량화/최적화 후 mlflow에 저장하는 라우터
"""


@router.post("", response_model=model.ModelCreateForm)
def lite_model(
    *,
    db: Session = SessionDepends,
    model_create_form: model.ModelCreateForm,
):
    """
    * params
        - lite_type
            1. ptq
    """
    ModelService.lite_model(db=db)
    return {"test": model_create_form.name, "test2": model_create_form.lite_type}


@router.get("")
def get_models(
    *,
    db: Session = SessionDepends,
):

    return "test"
