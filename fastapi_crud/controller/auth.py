from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_crud.model.user import User
from fastapi_crud.schema.auth import RegisterRequest
from fastapi_crud.utils.password import get_password_hash


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


async def register(_user: RegisterRequest, session: AsyncSession):
    _user.password = get_password_hash(_user.password)
    user = User(
        username=_user.username,
        password=_user.password,
        email=_user.email,
        name=_user.name,
    )

    try:
        session.add(user)
        await session.commit()
    except ValidationError as e:
        print(e.json())
    return {"message": "Register endpoint"}


def login():
    return {"message": "Login endpoint"}
