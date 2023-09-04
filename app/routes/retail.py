from app.schemas.actions import Action
from app.database import get_session
from sqlalchemy.orm import Session
from app.schemas.network_request import ONDCRequest
from app.controllers.retail_controller import retail_network_request_data
from fastapi import APIRouter, Depends


router = APIRouter(tags=['Retail'], prefix="/v1")

for action in Action:
    @router.post(f'/{action.value}')
    async def handle_request(request_data: ONDCRequest, db_session: Session = Depends(get_session)):
        return retail_network_request_data(request_data, db_session)
