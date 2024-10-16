from fastapi import Depends

from app.core.db.session import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


SessionDepends = Depends(get_db)
