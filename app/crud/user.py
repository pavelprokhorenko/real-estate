from typing import Any, Dict, Mapping, Optional, Union

from databases import Database

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models import user
from app.schemas.user import UserIn, UserUpdate


class CRUDUser(CRUDBase[type(user), UserIn, UserUpdate]):
    async def get_by_email(self, db: Database, *, email: str) -> Optional[Mapping]:
        return await db.fetch_one(
            self.model.select().where(self.model.c.email == email)
        )

    async def create(self, db: Database, *, obj_in: UserIn) -> Mapping:
        db_obj = obj_in.dict(exclude={"password"})
        db_obj["hashed_password"] = get_password_hash(obj_in.password)
        user_id = await db.execute(self.model.insert().values(**db_obj))
        return await self.get(db, model_id=user_id)

    async def update(
        self, db: Database, *, db_obj: user, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> Mapping:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return await super().update(db, db_obj=db_obj, obj_in=update_data)

    async def authenticate(
        self, db: Database, *, email: str, password: str
    ) -> Optional[Mapping]:
        obj = await self.get_by_email(db, email=email)
        if not obj:
            return None
        if not verify_password(password, obj.hashed_password):
            return None
        return obj


user = CRUDUser(user)
