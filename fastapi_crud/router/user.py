from typing import Annotated
from fastapi import Depends
from fastapi.routing import APIRouter
from sqlmodel import Session

from fastapi_crud.database import get_session
from fastapi_crud.controller import auth
from fastapi_crud.middleware.auth import get_current_user
from fastapi_crud.model.user import User
from fastapi_crud.schema.auth import LoginRequest, RegisterRequest

router = APIRouter()


@router.get("/")
def profile(current_user: Annotated[User, Depends(get_current_user)]):
    return {"data": current_user}
