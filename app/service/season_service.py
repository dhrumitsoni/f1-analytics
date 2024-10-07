from sqlalchemy import desc
from sqlalchemy.orm import Session
from app.db.models.season import Season
from app.schemas.seasson import SeasonSchema


def get_all_seasons(db: Session, skip: int = 0, limit: int = 20):
    seasons = db.query(Season).order_by(desc(Season.year)).offset(skip).limit(limit).all()
    return [SeasonSchema.from_orm(season) for season in seasons]
