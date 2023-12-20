from fastapi import HTTPException, status, APIRouter
from models.schemas import UserCreate, UserResponse
from utilities.search_error_handler import find_error_message_exception
from utilities.password_hash_verify import hash
from models.classes import User as UserModel
from db.start_session import init_session


router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)

session = init_session("User")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate):
    user_exists = session.query(UserModel).filter(
        UserModel.email == user.email).first()

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Email already exists"
        )
    # hash password
    hashed_password = hash(user.password)
    user.password = hashed_password

    user_created = UserModel(**user.model_dump())
    session.add(user_created)
    session.commit()
    session.refresh(user_created)

    return user_created


@router.get("/{id}", response_model=UserResponse)
def get_user(id: int):
    query_user = session.query(UserModel).filter(UserModel.id == id).first()
    if not query_user:
        find_error_message_exception("User", id)
    return query_user
