from schemas.vacancies import VacanciesAdd
from utils.repository import Repository
from models.models import VacanciesORM


class VacanciesService(Repository):
    model = VacanciesORM
    
    async def add_vacancies(self, vacancies: VacanciesAdd) -> int:
        info_vacancies = vacancies.model_dump()
        
        res = await super().add_one(info_vacancies)

        return res