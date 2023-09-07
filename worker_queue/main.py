import logging
import os
import sys

import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.credentials import PlainCredentials

from worker_queue.config import Settings, get_settings
from worker_queue.protocol_worker import ProtocolWorkers

_logger = logging.getLogger(__name__)


def create_queue_channel(settings: Settings) -> BlockingChannel:
    cr = PlainCredentials(settings.rabbit_user, settings.rabbit_pass)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.rabbit_host, credentials=cr)
    )
    channel = connection.channel()
    channel.queue_declare(queue=settings.retail_client_queue)
    channel.queue_declare(queue=settings.retail_network_queue)
    channel.queue_declare(queue=settings.logistic_client_queue)
    channel.queue_declare(queue=settings.logistic_network_queue)
    return channel


def main():
    settings = get_settings()
    channel = create_queue_channel(settings)
    ProtocolWorkers(channel=channel).worker_wait_for_work()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
