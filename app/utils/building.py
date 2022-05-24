from typing import Any, List

from app.schemas import AmenityOut, BuildingOut


def get_building_schema(building_record: Any, amenities: List[Any]) -> BuildingOut:
    return BuildingOut(
        id=building_record.id,
        name=building_record.name,
        description=building_record.description,
        latitude=building_record.latitude,
        longitude=building_record.longitude,
        building_class=building_record.building_class,
        postcode=building_record.postcode,
        number_of_units=building_record.number_of_units,
        number_of_floors=building_record.number_of_floors,
        year_built=building_record.year_built,
        amenities=[
            AmenityOut(id=amenity.id, name=amenity.name) for amenity in amenities
        ],
    )
