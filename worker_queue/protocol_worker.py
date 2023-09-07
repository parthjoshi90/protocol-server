from pika.adapters.blocking_connection import BlockingChannel

from worker_queue.jobs.job import (
    logistic_to_client,
    logistic_to_network,
    retail_to_network,
    retial_to_client,
)


class ProtocolWorkers:
    def __init__(self, channel: BlockingChannel) -> None:
        self.channel = channel

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.channel.stop_consuming()

    def worker_wait_for_work(self):
        self.channel.basic_consume(
            queue="retial_to_client",
            on_message_callback=retial_to_client,
            auto_ack=True,
        )
        self.channel.basic_consume(
            queue="retail_to_network",
            on_message_callback=retail_to_network,
            auto_ack=True,
        )
        self.channel.basic_consume(
            queue="logistic_to_client",
            on_message_callback=logistic_to_client,
            auto_ack=True,
        )
        self.channel.basic_consume(
            queue="logistic_to_network",
            on_message_callback=logistic_to_network,
            auto_ack=True,
        )
        self.channel.start_consuming()
