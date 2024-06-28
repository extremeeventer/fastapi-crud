from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jwt import decode, InvalidTokenError
from sqlmodel import Session, select


from fastapi_crud.config import Settings, get_settings
from fastapi_crud.database import get_session
from fastapi_crud.model.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    settings: Settings = Depends(get_settings),
    session: Session = Depends(get_session),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode(
            token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
        )
        id: int = payload.get("sub")
        if id is None:
            raise credentials_exception

        query = select(User).where(User.id == id)
        result = session.exec(query).first()

        print(result)

        if result is None:
            raise credentials_exception
        return result

    except InvalidTokenError:
        raise credentials_exception
    except Exception as e:
        raise {"message": "Internal Server Error"}
