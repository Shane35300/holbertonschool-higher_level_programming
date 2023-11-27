#!/usr/bin/python3
"""
Module defining the State class using SQLAlchemy
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class representing the
    'state' table in the database.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    # Définition de la relation entre City et State
    cities = relationship("City", back_populates="state")
