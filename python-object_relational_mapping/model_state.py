#!/usr/bin/python3
# Salama-Jamal (model_state.py)
"""
Explain class State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class State; exmple of Base
    Join to MySQL table "states"
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)