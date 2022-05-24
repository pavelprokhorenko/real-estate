from typing import Any, List

from databases import Database

from app.crud.base import CRUDBase
from app.models import building, building_amenities
from app.schemas.building import BuildingIn, BuildingUpdate


class CRUDBuilding(CRUDBase[type(building), BuildingIn, BuildingUpdate]):
    async def get_by_name(self, db: Database, *, name: str) -> Any:
        return await db.fetch_one(self.model.select().where(self.model.c.name == name))

    async def get_by_amenities(self, db: Database, *, amenities: List[int]) -> Any:
        buildings = list()
        for amenity_id in amenities:
            buildings.extend(
                await db.fetch_all(building_amenities.c.amenity_id == amenity_id)
            )
        return buildings

    # async def add_amenity_to_building(self, db: Database, *, obj_in: BuildingIn) -> Any:


building = CRUDBuilding(building)
