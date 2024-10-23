from enum import Enum


class ModelLiteMapper(Enum):
    """
    경량화 / 최적화 이미지 매핑
    """

    OWLV2_PTQ = "aipaas-harbor.surromind.ai/ptq-workflow/owl_v2_ptq_test:v0.5"
