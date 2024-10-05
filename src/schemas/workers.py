from pydantic import BaseModel
from schemas.vacancies import VacanciesGet


class WorkerAdd(BaseModel):
    name: str
    lastname: str
    resume: str


class WorkersGet(BaseModel):
    id: int
    name: str
    lastname: str
    resume: str


class WorkersDTO(WorkersGet):
    vacancies: list[VacanciesGet]
    