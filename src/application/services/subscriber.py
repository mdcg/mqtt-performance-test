from typing import Optional

from src.domain.entities.mqtt.parameters.mqtt_on_connect import MQTTOnConnect
from src.domain.entities.mqtt.parameters.mqtt_on_message import MQTTOnMessage
from src.domain.interfaces.mqtt.mqtt_subscriber import MQTTSubscriber
from src.infrastructure.logging import Logger
from src.infrastructure.mqtt.subscribers.paho_mqtt_subscriber import PahoMQTTSubscriber
from src.infrastructure.settings import Settings

logger = Logger("Subscriber")


class Subscriber:
    def __init__(self, settings: Optional[Settings] = None, mqtt_client: Optional[MQTTSubscriber] = None):
        self._mqtt = mqtt_client or PahoMQTTSubscriber(settings=settings or Settings())
        self._mqtt.register_on_connect(self.on_connect)
        self._mqtt.register_on_message(self.on_message)

    def on_message(self, data: MQTTOnMessage):
        logger.info(f"Message received: {data.msg.payload}")

    def on_connect(self, data: MQTTOnConnect):
        logger.info(f"Connection Status: {data.reason_code}")

    def run(self):
        logger.info("Running...")
        self._mqtt.run()
