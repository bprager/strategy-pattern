# Context Class

import MessageBusStrategy


class MessageBus:
    def __init__(self, strategy: MessageBusStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: MessageBusStrategy):
        self._strategy = strategy

    def publish_message(self, message, topic):
        self._strategy.publish(message, topic)

    def subscribe_to_topic(self, topic):
        self._strategy.subscribe(topic)
