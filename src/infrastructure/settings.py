from dataclasses import dataclass
from os import getenv


@dataclass
class Settings:
    MQTT_HOST: str = getenv("MQTT_HOST", "localhost")
    MQTT_PORT: int = int(getenv("MQTT_PORT", "1883"))
    MQTT_TOPIC: str = getenv("MQTT_TOPIC", "test/topic")
    MQTT_CLIENT_USERNAME: str = getenv("MQTT_CLIENT_USERNAME", "username")
    MQTT_CLIENT_PASSWORD: str = getenv("MQTT_CLIENT_PASSWORD", "p455w0rd")
