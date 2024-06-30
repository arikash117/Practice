from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = 'mysql+pymysql://root:root@127.0.0.1:3306/vacancies_data'


settings = Settings()
