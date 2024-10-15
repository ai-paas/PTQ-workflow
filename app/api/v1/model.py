from fastapi import APIRouter

from app.schemas.requests import model

router = APIRouter()

"""
모델 이름을 입력받고 해당 모델을 경량화/최적화 후 mlflow에 저장하는 라우터
"""


@router.post("", response_model=model.ModelCreateForm)
def lite_model(
    *,
    model_create_form: model.ModelCreateForm,
):
    """
    * params
        - lite_type
            1. ptq
    """
    return {"test": model_create_form.name, "test2": model_create_form.lite_type}


@router.get("")
def get_models():
    return "test"
