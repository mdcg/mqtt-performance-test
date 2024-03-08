from abc import ABC, abstractmethod
from typing import Callable

from src.domain.entities.mqtt.parameters.mqtt_on_publish import MQTTOnPublish


class MQTTPublisher(ABC):
    @abstractmethod
    def register_on_publish(self, callback: Callable) -> MQTTOnPublish:
        pass

    @abstractmethod
    def publish(self, message: str):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass
