from alembic import command
from alembic.config import Config
import uvicorn
from datetime import datetime

alembic_cfg = Config("alembic.ini")


def migrate():
    command.revision(alembic_cfg, f"{int(datetime.now().timestamp())}", True)
    command.upgrade(alembic_cfg, "head")


def dev():
    uvicorn.run("fastapi_crud.main:app", host="127.0.0.1", port=8000, reload=True)
