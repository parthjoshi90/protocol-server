from enum import Enum
from typing import Optional

from pydantic import BaseModel


class StatusEnum(Enum):
    ACK = "ACK"
    NACK = "NACK"


class Status(BaseModel):
    status: StatusEnum


class AckMessage(BaseModel):
    ack: Status


class ResponseACK(BaseModel):
    context: Optional[str] = None
    message: AckMessage
    error: Optional[str]
