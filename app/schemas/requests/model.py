from pydantic import BaseModel


# 모델 생성시 사용되는 Form
class ModelCreateForm(BaseModel):
    # 모델 이름
    name: str
    # 경량화/최적화 타입
    lite_type: int
