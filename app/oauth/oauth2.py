from fastapi import Depends, status, HTTPException
from jose import JWTError, jwt
from datetime import datetime, timedelta
from models.schemas import TokenData
from models.classes import User as UserModel
from db.start_session import init_session
from fastapi.security import OAuth2PasswordBearer
from config.config_settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

session = init_session("OAuth")

secret_key = settings.secret_key
algorithm = settings.algorithm
access_token_expire_minutes = settings.access_token_expire_minutes


def create_access_token(data: dict):
    to_encode = data.copy()
    access_token_expires = datetime.utcnow(
    ) + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": access_token_expires})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception

        user_id = str(id)

        token_data = TokenData(id=user_id)

    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    token = verify_access_token(token, credentials_exception)

    user = session.query(UserModel).filter(
        UserModel.id == token.id).first()

    return user
