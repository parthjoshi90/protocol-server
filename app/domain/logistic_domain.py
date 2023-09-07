from app.config import get_settings
from app.queueing import get_channel


def send_to_logistic_queue(action, payload):
    if action.startswith("on_"):
        return send_to_logistic_network_queue(payload)
    return send_to_logistic_client_queue(payload)


def send_to_logistic_client_queue(payload):
    settings = get_settings()
    get_channel(settings.logistic_client_queue).basic_publish(
        exchange="", routing_key=settings.logistic_client_queue, body=payload
    )
    return True


def send_to_logistic_network_queue(payload):
    settings = get_settings()
    get_channel(settings.logistic_network_queue).basic_publish(
        exchange="", routing_key=settings.logistic_network_queue, body=payload
    )
    return True
