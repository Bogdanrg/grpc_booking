from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = ("event_id", "username", "places")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PLACES_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    username: str
    places: int
    def __init__(self, event_id: _Optional[int] = ..., username: _Optional[str] = ..., places: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("event_id", "order_places", "success")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_PLACES_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    order_places: int
    success: bool
    def __init__(self, event_id: _Optional[int] = ..., order_places: _Optional[int] = ..., success: bool = ...) -> None: ...
