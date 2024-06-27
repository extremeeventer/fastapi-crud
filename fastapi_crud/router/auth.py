from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_crud.database import get_session
from fastapi_crud.controller import auth
from fastapi_crud.schema.auth import RegisterRequest

router = APIRouter()


@router.post("/register")
async def register(
    _user: RegisterRequest, session: AsyncSession = Depends(get_session)
):
    return await auth.register(_user, session)


@router.get("/login")
def login():
    return auth.login()
