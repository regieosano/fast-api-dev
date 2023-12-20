from fastapi import APIRouter, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from db.start_session import init_session
from ..oauth.oauth2 import create_access_token
from utilities.password_hash_verify import verify
from models.schemas import TokenResponse, UserLogin
from models.classes import User as UserModel

router = APIRouter(tags=["Authentication"])

session = init_session("Auth")


@router.post("/login", response_model=TokenResponse)
def login(user_credentials: UserLogin):
    user = session.query(UserModel).filter(
        UserModel.email == user_credentials.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Credentials"
        )

    user_is_authenticated = verify(user_credentials.password, user.password)

    if not user_is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Credentials"
        )

    access_token = create_access_token(data={"user_id": user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
