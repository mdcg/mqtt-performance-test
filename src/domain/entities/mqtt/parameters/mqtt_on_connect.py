from dataclasses import dataclass
from typing import Any


@dataclass
class MQTTOnConnect:
    client: Any
    userdata: Any
    flags: Any
    reason_code: Any
    properties: Any
