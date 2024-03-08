from dataclasses import dataclass
from typing import Any


@dataclass
class MQTTOnMessage:
    client: Any
    userdata: Any
    msg: Any
