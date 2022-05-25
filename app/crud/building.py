from typing import Any, Dict, List, Union

from databases import Database
from sqlalchemy import delete

from app.crud.base import CRUDBase
from app.models import amenity, building, building_amenities
from app.schemas.building import BuildingIn, BuildingUpdate


class CRUDBuilding(CRUDBase[type(building), BuildingIn, BuildingUpdate]):
    async def get_by_name(self, db: Database, *, name: str) -> Any:
        return await db.fetch_one(self.model.select().where(self.model.c.name == name))

    async def get_by_amenities(self, db: Database, *, amenities: List[int]) -> Any:
        buildings = list()
        for amenity_id in amenities:
            buildings.extend(
                await db.fetch_all(
                    building_amenities.select().where(
                        building_amenities.c.amenity_id == amenity_id
                    )
                )
            )
        return await db.fetch_all(
            self.model.select().where(
                self.model.c.id.in_([record.building_id for record in buildings])
            )
        )

    async def get_building_amenities(self, db: Database, *, model_id: int) -> Any:
        amenities = await db.fetch_all(
            building_amenities.select().where(
                building_amenities.c.building_id == model_id
            )
        )
        return await db.fetch_all(
            amenity.select().where(
                amenity.c.id.in_([record.amenity_id for record in amenities])
            )
        )

    async def delete_building_amenities(self, db: Database, *, model_id: int) -> None:
        await db.execute(
            delete(building_amenities).where(
                building_amenities.c.building_id == model_id
            )
        )

    async def add_amenity_to_building(
        self, db: Database, *, model_id: int, amenities: List[int]
    ) -> None:
        values = list()
        for amenity_id in amenities:
            values.append(dict(amenity_id=amenity_id, building_id=model_id))

        await db.execute_many(building_amenities.insert(), values=values)

    async def create(self, db: Database, *, obj_in: BuildingIn) -> Any:
        obj_in_data = obj_in.dict(exclude_unset=True, exclude={"amenities"})
        db_query = self.model.insert().values(**obj_in_data)
        obj_id = await db.execute(db_query)

        await self.add_amenity_to_building(
            db, amenities=obj_in.amenities, model_id=obj_id
        )

        return await self.get(db=db, model_id=obj_id)

    async def update(
        self, db: Database, *, db_obj: Any, obj_in: Union[BuildingIn, Dict[str, Any]]
    ) -> Any:
        if isinstance(obj_in, dict):
            update_data = obj_in
            del update_data["amenities"]
        else:
            update_data = obj_in.dict(exclude_unset=True, exclude={"amenities"})

        await self.delete_building_amenities(db, model_id=db_obj.id)
        await self.add_amenity_to_building(
            db, amenities=obj_in.amenities, model_id=db_obj.id
        )

        return await super().update(db, db_obj=db_obj, obj_in=update_data)


building = CRUDBuilding(building)
