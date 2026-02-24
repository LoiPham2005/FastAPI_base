import time
import logging
from fastapi import Request, FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("app.middleware")

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Log request info
        method = request.method
        path = request.url.path
        client_host = request.client.host if request.client else "unknown"
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        status_code = response.status_code
        
        # Log response info
        log_msg = f"{client_host} - {method} {path} - {status_code} - {process_time:.4f}s"
        
        if status_code >= 400:
            logger.warning(log_msg)
        else:
            logger.info(log_msg)
            
        response.headers["X-Process-Time"] = str(process_time)
        return response

def setup_middleware(app: FastAPI):
    app.add_middleware(LoggingMiddleware)
