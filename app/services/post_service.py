from models.classes import Post as PostModel, Vote as VoteModel
from sqlalchemy import func
from db.start_session import init_session

session = init_session("Post")

voteCountFunc = func.count(VoteModel.post_id).label('votes')

def get_all_service(limit,
                    skip,
                    search):
       
    posts_data = session.query(PostModel, voteCountFunc).join(VoteModel, VoteModel.post_id == PostModel.id, isouter=True).group_by(PostModel.id).filter(PostModel.title.contains(search)).limit(limit).offset(skip).all()   
    
    return posts_data


def create_post_service(post_to_be_created: PostModel, current_user):
    post_created = PostModel(
        owner_id=current_user.id, **post_to_be_created.model_dump())
    session.add(post_created)
    session.commit()
    session.refresh(post_created)
    return post_created


def get_latest_service():
    latest_post = session.query(PostModel).order_by(
        PostModel.id.desc()).first()
    return latest_post


def get_a_post_service(id: int):
    return session.query(PostModel, voteCountFunc).join(VoteModel, VoteModel.post_id == PostModel.id, isouter=True).group_by(PostModel.id).filter(PostModel.id == id).first()


def delete_post_service(id: int):
    return session.query(
        PostModel).filter(PostModel.id == id)
   

def update_post_service(id: int):
    return session.query(
        PostModel).filter(PostModel.id == id)    

