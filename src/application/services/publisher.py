from typing import Optional

from src.domain.entities.mqtt.parameters.mqtt_on_publish import MQTTOnPublish
from src.domain.interfaces.mqtt.mqtt_publisher import MQTTPublisher
from src.infrastructure.logging import Logger
from src.infrastructure.mqtt.publishers.paho_mqtt_publisher import PahoMQTTPublisher
from src.infrastructure.settings import Settings

logger = Logger("Publisher")


class Publisher:
    def __init__(self, settings: Optional[Settings] = None, mqtt_client: Optional[MQTTPublisher] = None):
        self._mqtt = mqtt_client or PahoMQTTPublisher(settings=settings or Settings())
        self._mqtt.register_on_publish(self.on_publish)

    def on_publish(self, data: MQTTOnPublish):
        try:
            data.userdata.remove(data.mid)
        except KeyError:
            logger.error(
                """
                on_publish() is called with a mid not present in unacked_publish
                This is due to an unavoidable race-condition:
                * publish() return the mid of the message sent.
                * mid from publish() is added to unacked_publish by the main thread
                * on_publish() is called by the loop_start thread
                While unlikely (because on_publish() will be called after a network round-trip),
                this is a race-condition that COULD happen
                
                The best solution to avoid race-condition is using the msg_info from publish()
                We could also try using a list of acknowledged mid rather than removing from pending list,
                but remember that mid could be re-used !
                """
            )

    def publish(self, message: str):
        logger.info(f"Message sent: {message}")
        self._mqtt.publish(message)

    def run(self):
        self._mqtt.run()

    def stop(self):
        self._mqtt.stop()
