from pydantic import BaseModel


class SeasonSchema(BaseModel):
    year: int
    url: str | None = None

    class Config:
        from_attributes = True
