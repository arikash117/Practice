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
        name = vacancy['name']
        area = vacancy['area']['name']
        schedule = vacancy['schedule']['name']
        employer = vacancy['employer']['name']
        experience = vacancy['experience']['name']

        new_vacancy_data = Table(
            name = name,
            area = area,
            schedule = schedule,
            employer = employer,
            experience = experience,
        )
        session.add(new_vacancy_data)

        filtered_vacancies.append({
            'name': name,
            'area': area,
            'schedule': schedule,
            'employer': employer,
            'experience': experience
        })
    session.commit()

    if query == 'all':
        return filtered_vacancies
    else:
        return [v.schedule for v in filtered_vacancies]
        
print(searching_vac('Менеджер', query=None))