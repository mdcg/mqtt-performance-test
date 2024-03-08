import time
from typing import Optional

from src.domain.entities.metrics.parameters.time_series_data import TimeSeriesData
from src.domain.entities.mqtt.parameters.mqtt_on_publish import MQTTOnPublish
from src.domain.interfaces.metrics.time_series_database import TimeSeriesDatabase
from src.domain.interfaces.mqtt.mqtt_publisher import MQTTPublisher
from src.infrastructure.logging import Logger
from src.infrastructure.metrics.influxdb import InfluxDB
from src.infrastructure.mqtt.publishers.paho_mqtt_publisher import PahoMQTTPublisher
from src.infrastructure.settings import Settings

logger = Logger("Publisher")


class Publisher:
    def __init__(
        self,
        settings: Optional[Settings] = None,
        mqtt_client: Optional[MQTTPublisher] = None,
        metrics: Optional[TimeSeriesDatabase] = None,
    ):
        self.settings = settings or Settings()
        self._metrics = metrics or InfluxDB(self.settings)
        self._mqtt = mqtt_client or PahoMQTTPublisher(self.settings)
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
        start_time = time.perf_counter()
        self._mqtt.publish(message)
        end_time = time.perf_counter()

        self._collect_time_spent(end_time - start_time)
        logger.info(f"Message sent: {message}")

    def _collect_time_spent(self, total_time: float):
        self._metrics.collect(
            TimeSeriesData(
                point_name=self.settings.MQTT_TOPIC,
                tag_name="service",
                tag_value="publisher",
                field_name="time_spent",
                field_value=total_time,
            )
        )

    def run(self):
        self._mqtt.run()

    def stop(self):
        self._mqtt.stop()
