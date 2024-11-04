import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .routers import chats, documents, messages, users
from .utils.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        create_db_and_tables()
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

logger = logging.getLogger()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    log_dict = {
        "method": request.method,
        "path": request.url.path,
        "status": 0,
        "duration": 0,
    }
    start_time = time.time()
    response = await call_next(request)
    log_dict["status"] = response.status_code
    log_dict["duration"] = time.time() - start_time

    logger.info(log_dict)

    return response


@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}
