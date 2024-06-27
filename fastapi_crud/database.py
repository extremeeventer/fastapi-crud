from sqlmodel import Session, create_engine

from fastapi_crud.config import get_settings

settings = get_settings()

DATABASE_URL = f"{settings.db_type}+{settings.db_mode}://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(DATABASE_URL, echo=True)

session = Session(engine)


def get_session():
    return session
