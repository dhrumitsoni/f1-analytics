from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base


class Driver(Base):
    __tablename__ = "drivers"

    driverId = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    driverRef = Column(String(length=255), nullable=False, default='')
    number = Column(Integer, default=None)
    code = Column(String(length=3), default=None)
    forename = Column(String(length=255), nullable=False, default='')
    surname = Column(String(length=255), nullable=False, default='')
    dob = Column(Date, default=None)
    nationality = Column(String(length=255), default=None)
    url = Column(String(length=255), unique=True, nullable=False, default='')
