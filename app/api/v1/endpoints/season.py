from typing import List
from sqlalchemy.orm import Session
from app.db.session import get_db
from fastapi import APIRouter, Depends
from app.schemas.seasson import SeasonSchema
from app.service.season_service import get_all_seasons
from app.utils.custom_responses import success_response, error_response

router = APIRouter()


@router.get("/season/", response_model=List[SeasonSchema])
def get_seasons(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    try:
        seasons = get_all_seasons(db=db, skip=skip, limit=limit)
        return success_response(data=seasons)
    except Exception as e:
        return error_response(message=str(e), status_code=500)







