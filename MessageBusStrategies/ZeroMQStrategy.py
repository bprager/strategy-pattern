# Concrete Strategy for ZeroMQ

import logging

from MessageBusStrategy import MessageBusStrategy

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(name)s - %(funcName)s:%(lineno)d: %(message)s",
    handlers=[logging.FileHandler(f"messages.log")],
    datefmt="%Y-%m-%d %H:%M:%S",
)


class ZeroMQStrategy(MessageBusStrategy):
    def publish(self, message, topic):
        logging.debug(f"Publishing {message} to topic {topic} using ZeroMQ")
        # ZeroMQ specific publish logic

    def subscribe(self, topic):
        logging.debug(f"Subscribing to topic {topic} using ZeroMQ")
        # ZeroMQ specific subscribe logic
