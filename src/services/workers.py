from sqlalchemy import select
from db.db import Session
from utils.repository import Repository
from models.models import WorkersORM
from sqlalchemy.orm import selectinload
from schemas.workers import WorkersDTO, WorkerAdd


class WorkersService(Repository):
    model = WorkersORM

    async def find_all(self) -> WorkersDTO:
        async with Session as session:
            query = (
                select(WorkersORM)
                .options(selectinload(WorkersORM.vacancies))
            )

            res = await session.execute(query)
            result = [WorkersDTO.model_validate(row, from_attributes=True) for row in res.scalars().all()]
            print(f'{result=}')
            return result
        


        