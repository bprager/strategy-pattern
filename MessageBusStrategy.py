import abc


# Strategy Interface
class MessageBusStrategy(abc.ABC):
    @abc.abstractmethod
    def publish(self, message, topic):
        pass

    @abc.abstractmethod
    def subscribe(self, topic):
        pass
