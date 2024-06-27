from sqlmodel import Session, select

from fastapi_crud.model.user import User
from fastapi_crud.schema.auth import LoginRequest, RegisterRequest
from fastapi_crud.utils.password import get_password_hash, verify_password


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3


def register(_user: RegisterRequest, session: Session):
    _user.password = get_password_hash(_user.password)
    user = User(
        username=_user.username,
        password=_user.password,
        email=_user.email,
        name=_user.name,
    )
    session.add(user)

    try:
        session.commit()
        return {"message": "Registered successfully!"}
    except Exception as e:
        print(e)
        session.rollback()
        if len(e.args) == 1 and "Duplicate entry" in str(e.args[0]):
            return {"message": "Username is already existed!"}
        return {"message": "An error occurred while registering"}


def login(_user: LoginRequest, session: Session):
    query = select(User).where(User.email == _user.email)
    result = session.exec(query).first()

    if result == None:
        return {"message": "Email is not existed!"}

    is_correct_password = verify_password(_user.password, result.password)

    if is_correct_password == False:
        return {"message": "Incorrect password!"}

    return {"message": "Login endpoint"}
