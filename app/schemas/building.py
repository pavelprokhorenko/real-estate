from typing import List, Optional

from app.schemas import BaseSchema


class AmenityIn(BaseSchema):
    name: str


class AmenityOut(AmenityIn):
    id: int
    name: str


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

    amenities: List[AmenityIn]


class BuildingOut(BuildingIn):
    id: int
    amenities: List[AmenityOut]
