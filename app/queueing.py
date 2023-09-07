# Dependency
import pika
from pika import PlainCredentials
from pika.adapters.blocking_connection import BlockingChannel

from app.config import get_settings


def get_channel(queue: str) -> BlockingChannel:
    cr = PlainCredentials(get_settings().rabbit_user, get_settings().rabbit_pass)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=get_settings().rabbit_host, credentials=cr)
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    return channel
