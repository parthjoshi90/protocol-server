from app.domain.logistic_domain import send_to_logistic_queue
from app.repository.ondc_repository import add_ondc_request
from app.schemas.actions import Action, Domain
from app.utils.response import get_response


def logistic_network_request_data(request_data, db_session):
    try:
        message_id = request_data.context.message_id
        action = request_data.context.action.value
        is_successful = add_ondc_request(
            db_session,
            domain=Domain(Domain.LOGISTICS),
            action=Action(action),
            message_id=message_id,
            request=request_data.model_dump_json(),
        )
        if is_successful:
            send_to_logistic_queue(action, request_data.model_dump_json())
            return get_response()
    except Exception as e:
        return get_response(ack=False, error=str(e))
