from pydantic import BaseModel


class VacanciesAdd(BaseModel):
    title: str
    description: str
    worker_id: int


class VacanciesGet(BaseModel):
    id: int
    title: str
    description: str
    worker_id: int
    