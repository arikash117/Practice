from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = 'mysql+pymsql://root:root@localhost:8000/Vacancies_data'