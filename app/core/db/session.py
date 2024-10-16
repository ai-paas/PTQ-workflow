from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import get_settings

settings = get_settings()

engine = create_engine(
    settings.get_db_uri,
    connect_args={"check_same_thread": False},
    echo=False,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
