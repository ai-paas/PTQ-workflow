from typing import List

from pydantic import BaseModel


class LiteModelForm(BaseModel):
    """
    모델 생성시 사용되는 Form
    """

    # 모델 이름
    name: str

    # 경량화/최적화 타입
    lite_type: int

    # 모델이 저장된 mlflow의 run id
    saved_model_run_id: str

    # model 이 저장된 주소 ex) models/bert-base-uncased-model
    saved_model_path: str

    # mlflow s3 endpoint 주소
    mlflow_s3_endpoint_url: str

    # mlflow 주소
    mlflow_tracking_url: str

    quantization_layers: List[str]
