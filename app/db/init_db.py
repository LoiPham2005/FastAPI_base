from sqlmodel import SQLModel
from app.db.session import engine
from app.db.base import *  # noqa: F403

async def init_db():
    async with engine.begin() as conn:
        # For development, you might want to drop tables first
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
