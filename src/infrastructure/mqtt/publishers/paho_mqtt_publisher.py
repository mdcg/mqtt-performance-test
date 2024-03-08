from typing import Any, Callable

import paho.mqtt.client as mqtt

from src.domain.entities.mqtt.parameters.mqtt_on_publish import MQTTOnPublish
from src.domain.interfaces.mqtt.mqtt_publisher import MQTTPublisher
from src.infrastructure.settings import Settings


class PahoMQTTPublisher(MQTTPublisher):
    def __init__(self, settings: Settings):
        self._client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.settings = settings
        self.unacked_publish = set()

    def register_on_publish(self, callback: Callable[[MQTTOnPublish], None]):
        self._on_publish_callback = callback

    def __on_publish(
        self, client: Any, userdata: Any, mid: Any, reason_code: Any, properties: Any
    ) -> Callable[[MQTTOnPublish], None]:
        payload = MQTTOnPublish(
            client=client, userdata=userdata, mid=mid, reason_code=reason_code, properties=properties
        )
        return self._on_publish_callback(payload)

    def publish(self, message: str):
        msg_info = self._client.publish(self.settings.MQTT_TOPIC, message, qos=1)
        self.unacked_publish.add(msg_info.mid)
        msg_info.wait_for_publish()

    def run(self):
        self._client.on_publish = self.__on_publish
        self._client.user_data_set(self.unacked_publish)
        self._client.connect(self.settings.MQTT_HOST, self.settings.MQTT_PORT)
        self._client.loop_start()

    def stop(self):
        self._client.disconnect()
        self._client.loop_stop()
