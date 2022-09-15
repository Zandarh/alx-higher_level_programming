#!/usr/bin/python3
"""contains State class + instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class with id and name attributes of each state
    """
    __table__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
