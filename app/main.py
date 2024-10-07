from fastapi import FastAPI
from app.api.v1.endpoints import season

app = FastAPI()

app.include_router(season.router, prefix="/app/v1", tags=["Season"])


@app.get("/", tags=["Index"])
def read_root():
    return {"message": "Welcome to the F1 Analytics API"}