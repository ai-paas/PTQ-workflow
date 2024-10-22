from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.core.db.connect import SessionDepends
from app.schemas.requests import model
from app.services.model_service import ModelService
from app.utils.kfp_client_manager import kfp_client

router = APIRouter()

"""
모델 이름을 입력받고 해당 모델을 경량화/최적화 후 mlflow에 저장하는 라우터
"""


@router.post("")
# @router.post("", response_model=model.ModelCreateForm)
def lite_model(
    *,
    db: Session = SessionDepends,
    lite_model_form: model.LiteModelForm,
):
    """
    * params
        - lite_type
            1. ptq
    """
    result = ModelService.lite_model_ptq(db=db, model_create_form=lite_model_form)
    return result


@router.get("")
def get_model(
    *,
    db: Session = SessionDepends,
):
    ModelService.get_lite_model(
        db=db,
    )
    test = kfp_client.get_run(run_id="a25b2786-74f9-4d52-bb70-95df24c6d7ea")
    return "test"
