from typing import Optional

from src.domain.entities.metrics.parameters.time_series_data import TimeSeriesData
from src.domain.entities.mqtt.parameters.mqtt_on_connect import MQTTOnConnect
from src.domain.entities.mqtt.parameters.mqtt_on_message import MQTTOnMessage
from src.domain.interfaces.metrics.time_series_database import TimeSeriesDatabase
from src.domain.interfaces.mqtt.mqtt_subscriber import MQTTSubscriber
from src.infrastructure.common.time_measurement import TimeMeasurement
from src.infrastructure.logging import Logger
from src.infrastructure.metrics.influxdb import InfluxDB
from src.infrastructure.mqtt.subscribers.paho_mqtt_subscriber import PahoMQTTSubscriber
from src.infrastructure.settings import Settings

logger = Logger("Subscriber")


class Subscriber:
    def __init__(
        self,
        settings: Optional[Settings] = None,
        mqtt_client: Optional[MQTTSubscriber] = None,
        metrics: Optional[TimeSeriesDatabase] = None,
    ):
        self.settings = settings or Settings()
        self._metrics = metrics or InfluxDB(self.settings)
        self._mqtt = mqtt_client or PahoMQTTSubscriber(self.settings)
        self._mqtt.register_on_connect(self.on_connect)
        self._mqtt.register_on_message(self.on_message)

    def on_message(self, data: MQTTOnMessage):
        with TimeMeasurement() as time_spent:
            logger.info(f"Message received: {data.msg.payload}")

        self._collect_time_spent(time_spent())

    def on_connect(self, data: MQTTOnConnect):
        logger.info(f"Connection Status: {data.reason_code}")

    def _collect_time_spent(self, total_time: float):
        self._metrics.collect(
            TimeSeriesData(
                point_name=self.settings.MQTT_TOPIC,
                tag_name="service",
                tag_value="subscriber",
                field_name="time_spent",
                field_value=total_time,
            )
        )

    def run(self):
        logger.info("Running...")
        self._mqtt.run()
