from sqlalchemy import JSON, Column, DateTime, Enum, Integer, String

from app.database import Base
from app.schemas.actions import Action, Domain


class OndcRequest(Base):
    __tablename__ = "ondc_request"

    id = Column(Integer, primary_key=True)
    action = Column(Enum(Action))
    domain = Column(Enum(Domain))
    message_id = Column(String(50))
    request = Column(JSON)
    created_at = Column(DateTime)
