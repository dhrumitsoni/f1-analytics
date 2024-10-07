from sqlalchemy import Column, String, Integer, Float
from app.db.base import Base


class ConstructorStanding(Base):
    __tablename__ = "constructorStandings"

    constructorStandingsId = Column(Integer, primary_key=True, autoincrement=True)
    raceId = Column(Integer, nullable=False, default=0)
    constructorId = Column(Integer, nullable=False, default=0)
    points = Column(Float, nullable=False, default=0)
    position = Column(Integer, default=None)
    positionText = Column(String(length=255), default=None)
    wins = Column(Integer, nullable=False, default=0)
