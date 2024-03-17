from dataclasses import dataclass
from os import getenv


@dataclass
class Settings:
    MQTT_HOST: str = getenv("MQTT_HOST", "localhost")
    MQTT_PORT: int = int(getenv("MQTT_PORT", "1883"))
    MQTT_TOPIC: str = getenv("MQTT_TOPIC", "test/PLUSULTRA")
    MQTT_CLIENT_USERNAME: str = getenv("MQTT_CLIENT_USERNAME", "username")
    MQTT_CLIENT_PASSWORD: str = getenv("MQTT_CLIENT_PASSWORD", "p455w0rd")

    INFLUXDB_USERNAME: str = getenv("INFLUXDB_USERNAME", "user")
    INFLUXDB_PASSWORD: str = getenv("INFLUXDB_PASSWORD", "p455w0rd")
    INFLUXDB_TOKEN: str = getenv(
        "INFLUXDB_TOKEN", "F-QFQpmCL9UkR3qyoXnLkzWj03s6m4eCvYgDl1ePfHBf9ph7yxaSgQ6WN0i9giNgRTfONwVMK1f977r_g71oNQ=="
    )
    INFLUXDB_URL: str = getenv("INFLUXDB_URL", "http://localhost:8086")
    INFLUXDB_ORG: str = getenv("INFLUXDB_ORG", "iot")
    INFLUXDB_BUCKET: str = getenv("INFLUXDB_BUCKET", "mqtt")
