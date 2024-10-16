from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session

from .database import create_db_and_tables, get_session
from .routers import chats, documents, messages, users

SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await create_db_and_tables()
        yield
    finally:
        pass


app = FastAPI(lifespan=lifespan)
app.include_router(users.router)
app.include_router(chats.router)
app.include_router(messages.router)
app.include_router(documents.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}
