from pydantic import BaseModel


class PatchTaskForm(BaseModel):
    """
    Task 수정시 사용되는 Form
    """

    # pipeline 상태
    progress_status: bool

    # 경량화 모델 저장 경로
    path_output_model: str
