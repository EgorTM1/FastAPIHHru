from fastapi import APIRouter
from services.workers import WorkersService
from schemas.workers import WorkerAdd, WorkersDTO

router_workers = APIRouter(
    tags=['Workers'],
    prefix='/workers',
)


@router_workers.get('/')
async def get_all() -> list[WorkersDTO]:
    res = await WorkersService().find_all()

    return res


@router_workers.post('/')
async def add_worker(worker: WorkerAdd) -> int:
    data = worker.model_dump()
    res = await WorkersService().add_one(data)

    return res
