from my_settings import config_settings
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


def create_dbsession(**kwargs):
    db_path = f'postgresql://{config_settings.user}:{config_settings.password}@{config_settings.host}:{config_settings.port}/{config_settings.db_name}'
    engine = db.create_engine(db_path)
    SessionClass = sessionmaker(bind=engine)
    return SessionClass()
