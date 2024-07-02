import requests
import mysql.connector

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/vacancies_data')
Base = declarative_base()

class Table(Base):
    __tablename__ = 'Vacancies_data'
    id = Column(Integer, primary_key=True)
    vacancy = Column(String(100), nullable=False)
    area = Column(String(100), nullable=False)
    schedule = Column(String(100), nullable=False)
    employer = Column(String(100), nullable=False)
    experience = Column(String(100), nullable=False)

Base.metadata.create_all(engine)

def searching_vac(vac_name, query):
    response = requests.get('https://api.hh.ru/vacancies')
    vacancy_flt = vac_name.lower()
    filtered_vacancies = []
    vacancies = response.json()['items']
    for vacancy in vacancies:
        name = vacancy['name']
        area = vacancy['area']['name']
        schedule = vacancy['schedule']['name']
        employer = vacancy['employer']['name']
        experience = vacancy['experience']['name']

    if vacancy_flt in name.lower():
        new_vacancy_data = Table(
            name = name,
            area = area,
            schedule = schedule,
            employer = employer,
            experience = experience,
        )
        Base.session.add(new_vacancy_data)
        Base.session.commit()

        filtered_vacancies.append({
            'name': name,
            'area': area,
            'schedule': schedule,
            'employer': employer,
            'experience': experience
        })
        if query == 'all':
            return filtered_vacancies
        else:
            return filtered_vacancies(name)