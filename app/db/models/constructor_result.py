from sqlalchemy import Column, String, Integer, Float
from app.db.base import Base


class ConstructorResult(Base):
    __tablename__ = "constructorResults"

    constructorResultsId = Column(Integer, primary_key=True, autoincrement=True)
    raceId = Column(Integer, nullable=False, default=0)
    constructorId = Column(Integer, nullable=False, default=0)
    points = Column(Float, default=None)
    status = Column(String(length=255), default=None)
