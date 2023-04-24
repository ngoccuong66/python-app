from sqlalchemy import VARCHAR, Column, text, Integer
from sqlalchemy.orm import relationship

from app.third_parties.sqlite.base import Base


class User(Base):
    __tablename__ ='user'

    id = Column('id', Integer, primary_key=True)
    user_name = Column('user_name', VARCHAR(50), nullable=False)
    pass_word = Column('pass_word', VARCHAR(20), nullable=False)
    token = Column('token', Integer, nullable=False)
