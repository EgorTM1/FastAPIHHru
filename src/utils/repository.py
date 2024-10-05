from sqlalchemy import select
from abc import ABC, abstractmethod
from db.db import Session


class AbstractRepository(ABC):

    @abstractmethod
    async def add_one():
        raise NotImplementedError
    

class Repository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with Session as session:
            add_obj = self.model(**data)

            session.add(add_obj)
            session.flush()
            await session.commit()

            return add_obj.id
        