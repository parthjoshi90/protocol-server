from app.models.ondc_request import OndcRequest
from app.utils.date_utils import get_current_time_utc


def add_ondc_request(db_session, domain, action, message_id, request):
    ondc_request = OndcRequest(
        action=action,
        domain=domain,
        message_id=message_id,
        request=request,
        created_at=get_current_time_utc(),
    )
    db_session.add(ondc_request)
    db_session.commit()
    return True
