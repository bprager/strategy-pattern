#!/usr/bin/env python3

import logging

from MessageBus import MessageBus
from MessageBusFactory import MessageBusFactory

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(name)s - %(funcName)s:%(lineno)d: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Application setup
if __name__ == "__main__":
    # The factory method creates the appropriate strategy based on the configuration file
    factory = MessageBusFactory()
    strategy = factory.get_strategy()

    # Set up the context with the chosen strategy
    message_bus = MessageBus(strategy)

    # Example usage
    message_bus.publish_message("Hello, World!", "greetings")
    message_bus.subscribe_to_topic("greetings")
