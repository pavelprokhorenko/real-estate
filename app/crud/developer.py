from typing import Any, Optional

from databases import Database

from app.crud.base import CRUDBase
from app.models import developer
from app.schemas.developer import DeveloperIn, DeveloperUpdate


class CRUDDeveloper(CRUDBase[type(developer), DeveloperIn, DeveloperUpdate]):
    async def get_by_international_name(
        self, db: Database, *, international_name: str
    ) -> Optional[Any]:
        return await db.fetch_one(
            self.model.select().where(
                self.model.c.international_name == international_name
            )
        )


developer = CRUDDeveloper(developer)
