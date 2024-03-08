from abc import ABC, abstractmethod

from src.domain.entities.metrics.parameters.time_series_data import TimeSeriesData


class TimeSeriesDatabase(ABC):
    @abstractmethod
    def collect(self, data: TimeSeriesData) -> None:
        pass
