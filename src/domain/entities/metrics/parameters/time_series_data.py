from dataclasses import dataclass
from typing import Any


@dataclass
class TimeSeriesData:
    point_name: str
    tag_name: str
    tag_value: Any
    field_name: str
    field_value: Any
