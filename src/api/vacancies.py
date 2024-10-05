from fastapi import APIRouter
from services.vacancies import VacanciesService
from schemas.vacancies import VacanciesAdd


router_vacancies = APIRouter(
    tags=['Vacancies'],
    prefix='/vacancies',
)


@router_vacancies.post('/')
async def add_vacancies(vacancies: VacanciesAdd) -> int:
    return await VacanciesService().add_vacancies(vacancies)

