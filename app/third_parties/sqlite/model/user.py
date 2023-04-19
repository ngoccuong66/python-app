from sqlalchemy import VARCHAR, Column, DateTime, ForeignKey, Table, text, INTEGER
from sqlalchemy.orm import relationship

from app.third_parties.sqlite.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column('id', INTEGER, primary_key=True, server_default=text("sys_guid() "))
    user_name = Column('user_name', VARCHAR(50), nullable=False)
    pass_word = Column('pass_word', VARCHAR(20), nullable=False)
    token = Column('user_name', VARCHAR(255), nullable=False)
