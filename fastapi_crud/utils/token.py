from datetime import datetime, timedelta, timezone
from fastapi_crud.config import get_settings
import jwt

settings = get_settings()


def create_access_token(data: dict):
    to_encode = data.copy()

    expires_delta = timedelta(minutes=settings.jwt_expire)
    expire = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.jwt_secret, algorithm=settings.jwt_algorithm
    )

    return encoded_jwt
