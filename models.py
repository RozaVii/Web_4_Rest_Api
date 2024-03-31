from sqlalchemy import Column, Integer, String
from database import base

class Demons(base):
    __tablename__ = "demons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    todo = Column(String)