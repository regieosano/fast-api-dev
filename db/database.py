from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config.config_settings import settings


SQL_ALCHEMY_DB_URL = f"postgresql://{settings.user}:{settings.password}@{
    settings.host}:{settings.port}/{settings.database_name}"

Base = declarative_base()

engine = create_engine(SQL_ALCHEMY_DB_URL)


def create_database_table():
    Base.metadata.create_all(engine)
