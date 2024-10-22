from sqlalchemy import Integer, String, orm
from sqlalchemy.orm import Mapped

from app.core.db.models.base import Base


# TDOO: 컬럼 분리 및 관계 설정
class ModelTask(Base):
    __tablename__ = "model_tasks"

    # 모델 저장 요청별 uuid
    # TODO: 모델 저장시 바로 가져올수 있으면 지우기
    task_uuid: Mapped[str] = orm.mapped_column(String, nullable=False)

    # 요청 작업 성공 여부 (기본값 False)
    progress_status: Mapped[bool] = orm.mapped_column(default=False, nullable=False)

    # 모델 이름
    model_name: Mapped[str] = orm.mapped_column(String, nullable=False)

    # 원본 모델 경로
    model_path_input: Mapped[str] = orm.mapped_column(String, nullable=False)

    # 경량화 방식
    lite_id: Mapped[int] = orm.mapped_column(Integer, nullable=False)

    # 최적화된 모델 경로 (mlflow 작업 완료 후 rest api로 요청)
    model_path_output: Mapped[str] = orm.mapped_column(
        String, nullable=True, default=None
    )

    # kubeflow experiment id
    kubeflow_experiment_id: Mapped[str] = orm.mapped_column(String, nullable=False)
