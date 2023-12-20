from fastapi import HTTPException, Response, status, APIRouter, Depends
from models.schemas import PostCreate, PostUpdate, PostResponse, PostUpdateResponse, PostVotesResponse
from utilities.search_error_handler import find_error_message_exception
from models.classes import Post as PostModel
from ..oauth.oauth2 import get_current_user
from db.start_session import init_session
from typing import List, Optional
from ..services.post_service import get_all_service, create_post_service, get_latest_service, get_a_post_service, delete_post_service, update_post_service

router = APIRouter(
    prefix="/api/posts",
    tags=["Posts"]
)

session = init_session("Post")


@router.get("/", response_model=List[PostVotesResponse])
def get_posts(_: object = Depends(get_current_user),
              limit: int = 20,
              skip: int = 0,
              search: Optional[str] = ""):
    return get_all_service(limit, skip, search)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostCreate, current_user: object = Depends(get_current_user)):
    return create_post_service(post, current_user)


@router.get("/latest", response_model=PostResponse)
def get_latest_post(_: object = Depends(get_current_user)):
    return get_latest_service()


@router.get("/{id}", response_model=PostVotesResponse)
def get_post(id: int, _: object = Depends(get_current_user)):
    query_post = get_a_post_service(id)
    if not query_post:
        find_error_message_exception("Post", id)
    return query_post


@router.delete("/{id}")
def delete_post(id: int, current_user: object = Depends(get_current_user)):
    post_to_delete = delete_post_service(id)
    if not post_to_delete.first():
        find_error_message_exception("Delete", id)

    post = post_to_delete.first()

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to delete this post"
        )

    post_to_delete.delete(synchronize_session=False)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=PostUpdateResponse)
def update_post(id: int, update_post: PostUpdate, current_user: object = Depends(get_current_user)):
    post_query_to_update = update_post_service(id)

    if not post_query_to_update.first():
        find_error_message_exception(id)

    post = post_query_to_update.first()

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to update this post"
        )

    post_query_to_update.update(
        update_post.model_dump(), synchronize_session=False)

    session.commit()
  
    return update_post
