from pydantic import BaseModel


class Site(BaseModel):
    id: int
    url: str


class Metric(BaseModel):
    site_id: int
    status_code: int
