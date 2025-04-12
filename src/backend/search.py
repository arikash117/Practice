import requests

from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/vacancies_data')
Base = declarative_base()
metadata = MetaData()

class Table(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    area = Column(String(100), nullable=False)
    schedule = Column(String(100), nullable=False)
    employer = Column(String(100), nullable=False)
    experience = Column(String(100), nullable=False)

Session = sessionmaker(bind=engine)
session = Session()

def searching_vac(vac_name, query):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    response = requests.get('https://api.hh.ru/vacancies', params={'text': vac_name})
    filtered_vacancies = []
    vacancies = response.json()['items']
    for vacancy in vacancies:

        new_vacancy_data = Table(
            name = vacancy['name'],
            area = vacancy['area']['name'],
            schedule = vacancy['schedule']['name'],
            employer = vacancy['employer']['name'],
            experience = vacancy['experience']['name'],
        )
        session.add(new_vacancy_data)

        filtered_vacancies.append({
            'name': new_vacancy_data.name,
            'area': new_vacancy_data.area,
            'schedule': new_vacancy_data.schedule,
            'employer': new_vacancy_data.employer,
            'experience': new_vacancy_data.experience,
        })
    session.commit()

    if query == 'all':
        filtered_vacancies_list = []
        for x in filtered_vacancies:
            filtered_vacancies = [x['name'], x['area'], x['schedule'], x['employer'], x['experience']]
            filtered_vacancies_list.append(filtered_vacancies)
    else:
        filtered_vacancies_list = [x['name'] for x in filtered_vacancies]
    return filtered_vacancies_list
