from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, post, user, vote
from db.start_db import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init_db()


@app.get("/")
def root():
    return {"message": "Welcome to FastAPIs!"}


app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)
