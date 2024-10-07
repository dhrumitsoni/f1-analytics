from sqlalchemy import Column, Integer, String
from app.db.base import Base


class Season(Base):
    __tablename__ = "seasons"

    year = Column(Integer, primary_key=True, nullable=False, default=0, index=True)
    url = Column(String, unique=True, nullable=False, default='')
