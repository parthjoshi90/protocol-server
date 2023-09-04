from app.schemas.response import StatusEnum

def get_response(ack=True, error=''):
    resp = {"context": None, "message": {"ack": {"status": StatusEnum.ACK.value if ack else StatusEnum.NACK.value}}}
    if error:
        resp['error'] = error
    return resp