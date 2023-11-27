#!/usr/bin/python3
"""
Module defining the City class using SQLAlchemy
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import State, Base


class City(Base):
    """
    City class representing the
      'cities' table in the database.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Définition de la relation entre City et State
    state = relationship("State", back_populates="cities")
