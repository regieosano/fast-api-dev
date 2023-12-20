from fastapi import HTTPException, status, APIRouter, Depends
from models.schemas import VoteCreate
from ..oauth.oauth2 import get_current_user
from utilities.search_error_handler import find_error_message_exception
from models.classes import Post as PostModel, Vote as VoteModel
from db.start_session import init_session


router = APIRouter(
    prefix="/api/votes",
    tags=["Votes"]
)

session = init_session("Vote")


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: VoteCreate, current_user: int = Depends(get_current_user)):
    post_to_be_voted = session.query(PostModel).filter(
        PostModel.id == vote.post_id).first()
    
    if not post_to_be_voted:
        find_error_message_exception("Post", vote.post_id)

    vote_exists = session.query(VoteModel).filter(
        VoteModel.post_id == vote.post_id, VoteModel.user_id == current_user.id).first()

    if (vote.dir == 1):
        if vote_exists:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {current_user.id} already voted for this post with id of post as {
                    vote.post_id}"
            )

        new_vote = VoteModel(post_id=vote.post_id, user_id=current_user.id)
        session.add(new_vote)
        session.commit()
        return {"message": "Vote created successfully"}
    else:
        if not vote_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vote does not exist"
            )

        session.delete(vote_exists)
        session.commit()
        return {"message": "Vote deleted successfully"}
