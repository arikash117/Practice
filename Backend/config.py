from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = 'mysql+pymysql://root:root@localhost:3306/Vacancies_data'


settings = Settings()
