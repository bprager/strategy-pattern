#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import logging
from importlib import import_module


load_dotenv()
load_dotenv("config.env")

DEFAULT_MESSAGE_BUS_STRATEGY = "MQTTStrategy"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(name)s - %(funcName)s:%(lineno)d: %(message)s",
    handlers=[logging.FileHandler("messages.log")],
    datefmt="%Y-%m-%d %H:%M:%S",
)


# Factory Class
class MessageBusFactory:
    @staticmethod
    def get_strategy():
        # Get the configuration from environment
        strategy_class_name = os.getenv(
            "message_bus_strategy", default=DEFAULT_MESSAGE_BUS_STRATEGY
        )

        logging.debug(f"Using {strategy_class_name} strategy")

        # Dynamically import the appropriate strategy class
        module = import_module(f"MessageBusStrategies.{strategy_class_name}")

        # Get the class from the module
        strategy_class = getattr(module, strategy_class_name)

        # Return an instance of the strategy class
        return strategy_class()
