import json
import time

from fastapi import Request
from loguru import logger

logger.add(
    "logs/app.log",
    format="{time} | {level} | {message}",
    level="INFO",
    rotation="10 MB",
    serialize=True,
)


async def log_middleware(request: Request, call_next):
    start_time = time.time()

    # Extract details from the request
    request_body = await request.body()
    request_data = {
        "method": request.method,
        "url": str(request.url),
        "query_params": dict(request.query_params),
        "body": request_body.decode("utf-8") if request_body else None,
    }

    response = await call_next(request)

    duration = time.time() - start_time

    log_dict = {
        "method": request.method,
        "url": str(request.url),
        "status_code": response.status_code,
        "duration": duration,
        "request": request_data,
        "response_status_code": response.status_code,
    }

    logger.info(json.dumps(log_dict, indent=2))

    return response
