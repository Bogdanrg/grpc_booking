import logging
import os
from concurrent import futures
import booking_pb2
import booking_pb2_grpc

import grpc
from core.database import db


class BookingServicer(booking_pb2_grpc.BookerServicer):
    def OrderPlace(self, request, content):
        collection = db["booking"]
        collection.insert_one({"event_id": request.event_id, "username": request.username, "places": request.places})
        return booking_pb2.Response(event_id=request.event_id, order_places=request.places, success=True)


def serve():
    port = os.environ.get("SERVER_PORT")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookerServicer_to_server(BookingServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
