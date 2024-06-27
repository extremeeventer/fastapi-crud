from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_crud.database import get_session
from fastapi_crud.controller import auth

router = APIRouter()


@router.get("/register")
async def register(session: AsyncSession = Depends(get_session)):
    return await auth.register(session)


@router.get("/login")
def login():
    return auth.login()
