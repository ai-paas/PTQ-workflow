from uuid import uuid4

from kfp import dsl
from sqlalchemy.orm import Session

from app.config.model_lite_mapper import ModelLiteMapper
from app.core.settings import get_settings
from app.schemas.requests import model
from app.utils.kfp_client_manager import kfp_client


class ModelService:
    def lite_model_ptq(db: Session, model_create_form: model.LiteModelForm) -> str:
        """
        ptq를 적용한 모델 경량화
        """
        ptq_docker_image_path = ModelLiteMapper.OWLV2_PTQ.value
        # TODO: server_path 변경
        # 작업 완료시 server에 요청을 보낼 url
        response_server_url = "0.0.0.0"

        uuidV4 = uuid4()
        uuid_str = str(uuidV4)

        # 사용할 컨테이너 정의 및 설정 추가
        @dsl.container_component
        def ptq_workflow(greeting: dsl.OutputPath(str)):
            quantization_layers_str = ",".join(model_create_form.quantization_layers)
            return dsl.ContainerSpec(
                # 사용할 도커이미지의 주소 및 태그
                image=ptq_docker_image_path,
                # 실행할 커맨드
                # command=["pipenv", "run", "python", "main.py"],
                command=[
                    "pipenv",
                    "run",
                    "python",
                    "main.py",
                ],
                # 필요한 변수들 정의 (string으로 정의)
                args=[greeting]
                + [
                    "--model_name",
                    model_create_form.name,
                    "--model_run_id",
                    model_create_form.saved_model_run_id,
                    "--model_path",
                    model_create_form.saved_model_path,
                    "--quantization_layers",
                    quantization_layers_str,
                    "--mlflow_tracking_url",
                    model_create_form.mlflow_tracking_url,
                    "--mlflow_s3_endpoint_url",
                    model_create_form.mlflow_s3_endpoint_url,
                    "--server_uuid",
                    uuid_str,
                    "--server_path",
                    response_server_url,
                ],
            )

        # 파이프라인 정의
        @dsl.pipeline
        def lite_model_ptq_test() -> str:
            workflow = ptq_workflow()

            return workflow.outputs["greeting"]

        # 정의된 함수로 파이프라인 생성
        run = kfp_client.create_run_from_pipeline_func(
            # experiment_id=lite_model_trt_test,
            pipeline_func=lite_model_ptq_test,
            namespace=get_settings().KUBEFLOW_NAMESPACE,
        )

        print("test")

    def get_lite_model(
        db: Session,
    ):
        pass
