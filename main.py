from fastapi import FastAPI
from schemas import OrderModel
import grpc
from booking_pb2_grpc import BookerStub
import booking_pb2

app = FastAPI()


@app.post("/order")
async def create_order(order: OrderModel) -> dict:
    with grpc.insecure_channel("server:8080") as channel:
        stub = BookerStub(channel)
        response = stub.OrderPlace(booking_pb2.Order(event_id=order.event_id, username=order.username, places=order.places))
    return {
        "event_id": response.event_id,
        "order_places": response.order_places,
        "success": response.success
    }
