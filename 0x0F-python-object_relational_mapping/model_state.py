#!/usr/bin/python3
"""contains State class + instance Base = declarative_base()
"""

from os import stat_result
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __table__ = "states"
    id = Column(Integer, primary_key=True)
    id = Column(Integer, primary_key=True)
