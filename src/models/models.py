from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.db import Base
from typing import List


class WorkersORM(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    lastname: Mapped[str]
    resume: Mapped[str] = mapped_column(String(200))

    vacancies: Mapped[List['VacanciesORM']] = relationship(
        back_populates='worker'
    )



class VacanciesORM(Base):
    __tablename__ = 'vacancies'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]

    worker_id: Mapped[str] = mapped_column(ForeignKey('workers.id'))

    worker: Mapped['WorkersORM'] = relationship(
        back_populates='vacancies'
    )

