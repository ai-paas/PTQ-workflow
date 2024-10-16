from sqlalchemy.orm import Session


class ModelService:
    def lite_model(self, db: Session) -> str: ...
