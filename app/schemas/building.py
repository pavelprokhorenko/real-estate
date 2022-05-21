from typing import Optional

from app.schemas import BaseSchema


class BuildingIn(BaseSchema):
    name: Optional[str] = ""
    description: Optional[str] = ""
    latitude: float
    longitude: float
    building_class: str
    postcode: str
    number_of_units: int
    number_of_floors: int
    year_built: str


class BuildingOut(BuildingIn):
    id: int
