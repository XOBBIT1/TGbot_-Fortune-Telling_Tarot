import datetime
from functools import wraps

from settings.bd.session_to_postgres import create_dbsession
from settings.bd.models import Users
import random

db_session = create_dbsession()


def get_names(model):
    query = db_session.query(model).all()
    names = []
    for card_name in query:
        names.append(card_name.card_name)
    return names


def get_data_by_name(model):
    random_card = random.choice(get_names(model))
    query = db_session.query(model).filter(model.card_name == random_card).all()
    return query


def add_user(message):
    user_count = db_session.query(Users).filter_by(chat_id=message.chat.id).count()
    if user_count > 0:
        print("User already exists")
    else:
        db_session.add(Users(name=message.from_user.first_name,
                             chat_id=message.chat.id,
                             username=message.from_user.username,
                             created_at=datetime.datetime.now()))
        db_session.commit()
        db_session.close()


async def writing_data(data: dict, model):
    db_session.add(model(**data))
    db_session.commit()
    db_session.close()
