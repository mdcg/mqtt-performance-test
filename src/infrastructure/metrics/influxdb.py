from influxdb_client import InfluxDBClient, Point

from src.domain.entities.metrics.parameters.time_series_data import TimeSeriesData
from src.domain.interfaces.metrics.time_series_database import TimeSeriesDatabase
from src.infrastructure.settings import Settings


class InfluxDB(TimeSeriesDatabase):
    def __init__(self, settings: Settings):
        self.settings = settings

        client = InfluxDBClient(
            url=self.settings.INFLUXDB_URL, token=self.settings.INFLUXDB_TOKEN, org=self.settings.INFLUXDB_ORG
        )
        self.write_api = client.write_api()

    def collect(self, data: TimeSeriesData):
        point = Point(data.point_name).tag(data.tag_name, data.tag_value).field(data.field_name, data.field_value)
        self.write_api.write(bucket=self.settings.INFLUXDB_BUCKET, record=point)
