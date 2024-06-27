from fastapi import Depends
from fastapi.routing import APIRouter
from sqlmodel import Session

from fastapi_crud.database import get_session
from fastapi_crud.controller import auth
from fastapi_crud.schema.auth import LoginRequest, RegisterRequest

router = APIRouter()


@router.post("/register")
def register(_user: RegisterRequest, session: Session = Depends(get_session)):
    return auth.register(_user, session)


@router.post("/login")
def login(_user: LoginRequest, session: Session = Depends(get_session)):
    return auth.login(_user, session)
