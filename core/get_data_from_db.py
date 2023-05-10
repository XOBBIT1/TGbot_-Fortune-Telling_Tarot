from my_settings.bd.session_to_postgres import create_dbsession
from my_settings.bd.models import Cards

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
