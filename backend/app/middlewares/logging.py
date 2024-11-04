import logging
import time

from fastapi import Request

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)


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
