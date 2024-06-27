from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_crud.model.main import User


async def register(session: AsyncSession):
    user = User(username="test_user", password="test_password", email="test_email")
    session.add(user)
    await session.commit()
    return {"message": "Register endpoint"}


def login():
    return {"message": "Login endpoint"}
