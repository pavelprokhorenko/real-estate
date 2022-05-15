from typing import Generator, Optional

from databases import Database

from app.core.config import settings


async def get_db_pg() -> Generator:
    db: Optional[Database] = None
    try:
        db = Database(settings.POSTGRES_URL)
        await db.connect()
        yield db
    finally:
        if db is not None:
            await db.disconnect()
