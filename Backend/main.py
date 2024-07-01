import requests

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


response = requests.get('https://api.hh.ru/vacancies')
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/vacancies_data')
Base = declarative_base()

class Table(Base):
    __tablename__ = 'Vacancies_data'
    id = Column(Integer, primary_key=True)
    area = Column(String(100), nullable=False)
    schedule = Column(String(100), nullable=False)
    employer = Column(String(100), nullable=False)
    experience = Column(String(100), nullable=False)

Base.metadata.create_all(engine)

vacancies = response.json()['items']
for vacancy in vacancies:
    id = vacancy['id']
    name = vacancy['name']
    area = vacancy['area']['name']
    schedule = vacancy['schedule']['name']
    employer = vacancy['employer']['name']
    experience = vacancy['experience']['name']

