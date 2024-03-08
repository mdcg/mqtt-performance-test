from typing import Any, Callable

import paho.mqtt.client as mqtt

from src.domain.entities.mqtt.parameters.mqtt_on_connect import MQTTOnConnect
from src.domain.entities.mqtt.parameters.mqtt_on_message import MQTTOnMessage
from src.domain.interfaces.mqtt.mqtt_subscriber import MQTTSubscriber
from src.infrastructure.settings import Settings


class PahoMQTTSubscriber(MQTTSubscriber):
    def __init__(self, settings: Settings):
        self._client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.settings = settings

    def register_on_connect(self, callback: Callable[[MQTTOnConnect], None]):
        self._on_connect_callback = callback

    def register_on_message(self, callback: Callable[[MQTTOnMessage], None]):
        self._on_message_callback = callback

    def __on_connect(
        self, client: Any, userdata: Any, flags: Any, reason_code: Any, properties: Any
    ) -> Callable[[MQTTOnConnect], None]:
        payload = MQTTOnConnect(
            client=client,
            userdata=userdata,
            flags=flags,
            reason_code=reason_code,
            properties=properties,
        )
        client.subscribe(self.settings.MQTT_TOPIC)
        return self._on_connect_callback(payload)

    def __on_message(self, client, userdata, msg) -> Callable[[MQTTOnMessage], None]:
        payload = MQTTOnMessage(
            client=client,
            userdata=userdata,
            msg=msg,
        )
        return self._on_message_callback(payload)

    def run(self):
        self._client.on_connect = self.__on_connect
        self._client.on_message = self.__on_message
        self._client.connect(self.settings.MQTT_HOST, self.settings.MQTT_PORT)
        self._client.loop_forever()
