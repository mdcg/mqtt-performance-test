from dataclasses import dataclass
from typing import Any


@dataclass
class MQTTOnPublish:
    client: Any
    userdata: Any
    mid: Any
    reason_code: Any
    properties: Any
