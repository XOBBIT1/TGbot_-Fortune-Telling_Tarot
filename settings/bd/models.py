from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.orm import relationship

Base = declarative_base()


class Cards(Base):
    __tablename__ = 'Cards'

    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column("card_name", db.String)
    card_url = db.Column("card_url", db.String)
    card_description = db.Column("card_description", db.String)
    harness = db.Column("harness", db.String)
    descriptions_id = db.Column("descriptions_id", db.BigInteger, db.ForeignKey('Descriptions.id'))
    img_id = db.Column("img_id", db.BigInteger, db.ForeignKey('Images.id'))
    descriptions = relationship("Descriptions", back_populates="cards", uselist=False)
    images = relationship("Images", back_populates="cards", uselist=False)


class Users(Base):
    __tablename__ = "Users"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column("name", db.String)
    chat_id = db.Column("chat_id", db.BigInteger)


class Descriptions(Base):
    __tablename__ = "Descriptions"

    id = db.Column(db.Integer, primary_key=True)
    love_description = db.Column("love_description", db.String)
    work_description = db.Column("work_description", db.String)
    issue_description = db.Column("issue_description", db.String)
    money_description = db.Column("money_description", db.String)
    health_description = db.Column("health_description", db.String)
    spirit_description = db.Column("spirit_description", db.String)
    cards = relationship("Cards", back_populates="descriptions", uselist=False)


class Images(Base):
    __tablename__ = "Images"
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column("images_url", db.String)
    cards = relationship("Cards", back_populates="images", uselist=False)

