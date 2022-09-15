#!/usr/bin/python3
"""contains State class + instance Base = declarative_base()
"""

from os import stat_result
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class with id and name attributes of each state
    """
    __table__ = "states"
     id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
