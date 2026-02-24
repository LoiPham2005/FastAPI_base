from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.db.init_db import init_db
from app.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB tables during development
    if settings.DEBUG:
        await init_db()
    
    from app.core.bootstrap import log_app_startup
    log_app_startup()
    
    yield

def get_application() -> FastAPI:
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        version="1.0.0",
        lifespan=lifespan,
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # API Routers
    _app.include_router(api_router, prefix=settings.API_V1_STR)
    
    from app.core.middleware import setup_middleware
    from app.core.exceptions import setup_exceptions
    from app.core.logging import setup_logging
    
    # Initialize Core modules
    setup_logging()
    setup_middleware(_app)
    setup_exceptions(_app)

    return _app

app = get_application()

@app.get("/")
async def root():
    return {"message": "Welcome to Sports Booking API (SQLModel Optimized)"}
