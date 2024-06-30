from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str = "7198230486:AAEuSM07Pu2tJt1luZoKERbdAuVOUJPs81E"
    db_url: str = 'mysql+pymysql://root:root@127.0.0.1:3306/vacancies_data'


settings = Settings()