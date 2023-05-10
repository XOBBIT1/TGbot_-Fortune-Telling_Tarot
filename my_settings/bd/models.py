from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

Base = declarative_base()


class Cards(Base):
    __tablename__ = 'Cards'

    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column("card_name", db.String)
    card_url = db.Column("card_url", db.String)
    card_description = db.Column("card_description", db.String)
    harness = db.Column("harness", db.String)