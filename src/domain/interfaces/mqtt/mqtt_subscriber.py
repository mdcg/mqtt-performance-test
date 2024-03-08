from abc import ABC, abstractmethod
from typing import Callable

from src.domain.entities.mqtt.parameters.mqtt_on_connect import MQTTOnConnect
from src.domain.entities.mqtt.parameters.mqtt_on_message import MQTTOnMessage


class MQTTSubscriber(ABC):
    @abstractmethod
    def register_on_connect(self, callback: Callable[[MQTTOnConnect], None]):
        pass

    @abstractmethod
    def register_on_message(self, callback: Callable[[MQTTOnMessage], None]):
        pass

    @abstractmethod
    def run(self):
        pass
