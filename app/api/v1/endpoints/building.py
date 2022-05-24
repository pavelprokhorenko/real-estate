from typing import Any, List

from databases import Database
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query, status

from app import crud, schemas
from app.api.deps import get_db_pg, get_request_active_superuser
from app.utils.building import get_building_schema

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.BuildingOut],
    dependencies=[Depends(get_request_active_superuser)],
)
async def read_buildings(
    *,
    skip: int = Query(0),
    limit: int = Query(100),
    db: Database = Depends(get_db_pg),
) -> Any:
    """
    Retrieve buildings.
    """
    buildings = list()
    db_buildings = await crud.building.get_multi(db, skip=skip, limit=limit)
    for building in db_buildings:
        buildings.append(
            get_building_schema(
                building_record=building,
                amenities=await crud.building.get_building_amenities(
                    db, model_id=building.id
                ),
            )
        )

    return buildings


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.BuildingOut,
    dependencies=[Depends(get_request_active_superuser)],
)
async def create_building(
    *,
    building: schemas.BuildingIn = Body(...),
    db: Database = Depends(get_db_pg),
) -> Any:
    """
    Create new building.
    """
    db_building = await crud.building.get_by_name(db, name=building.name)
    if db_building:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The building with this name already exists.",
        )
    obj = await crud.building.create(db, obj_in=building)
    return get_building_schema(
        building_record=obj,
        amenities=await crud.building.get_building_amenities(db, model_id=obj.id),
    )


@router.get(
    "/{building_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.BuildingOut,
    dependencies=[Depends(get_request_active_superuser)],
)
async def read_building_by_id(
    *,
    building_id: int = Path(...),
    db: Database = Depends(get_db_pg),
) -> Any:
    """
    Get a specific building by id.
    """
    building = await crud.building.get(db, model_id=building_id)
    if not building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The building with this id does not exist",
        )
    return get_building_schema(
        building_record=building,
        amenities=await crud.building.get_building_amenities(db, model_id=building.id),
    )


@router.patch(
    "/{building_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.BuildingOut,
    dependencies=[Depends(get_request_active_superuser)],
)
async def update_building(
    *,
    building_id: int = Path(...),
    building_in: schemas.BuildingUpdate = Body(...),
    db: Database = Depends(get_db_pg),
) -> Any:
    """
    Update a building.
    """
    building = await crud.building.get(db, model_id=building_id)
    if not building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The building with this id does not exist",
        )
    return get_building_schema(
        building_record=await crud.building.update(
            db, db_obj=building, obj_in=building_in
        ),
        amenities=await crud.building.get_building_amenities(db, model_id=building.id),
    )


@router.delete(
    "/{building_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_request_active_superuser)],
)
async def delete_building(
    *,
    building_id: int = Path(...),
    db: Database = Depends(get_db_pg),
) -> None:
    """
    Delete a building.
    """
    building = await crud.building.get(db, model_id=building_id)
    if not building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The building with this id does not exist",
        )
    return await crud.building.remove(db, model_id=building_id)
