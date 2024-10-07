from sqlalchemy import Column, String, Integer, Float
from app.db.base import Base


class Circuit(Base):
    __tablename__ = "circuits"

    circuitId = Column(Integer, primary_key=True, autoincrement=True)
    circuitRef = Column(String(length=255), nullable=False, default='')
    name = Column(String(length=255), nullable=False, default='')
    location = Column(String(length=255), nullable=False, default='')
    country = Column(String(length=255), nullable=False, default='')
    lat = Column(Float, default=None)
    long = Column(Float, default=None)
    alt = Column(Integer, default=None)
    url = Column(String(length=255), unique=True, default='')
