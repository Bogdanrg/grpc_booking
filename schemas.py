from pydantic import BaseModel


class OrderModel(BaseModel):
    event_id: int
    username: str
    places: int


class ResponseModel(BaseModel):
    event_id: int
    order_places: int
    success: bool
