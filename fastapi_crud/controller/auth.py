from fastapi_crud.model.user import User
from fastapi_crud.schema.auth import LoginRequest, RegisterRequest
from fastapi_crud.utils.password import get_password_hash, verify_password
from sqlmodel import Session, select

from fastapi_crud.utils.token import create_access_token


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

    token = create_access_token(data={"sub": result.id})

    return {"message": "Login successfully!", "token": token}
