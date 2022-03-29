import logging
from abc import abstractmethod, ABC
from typing import List

from apscheduler.schedulers.blocking import BlockingScheduler

from storage.interface import StorageInterface, TickerData, ErrorStoreException
from ticker.abstract import TickerAbstract


class SchedulerMixin(ABC):
    """Mixin which can add simple scheduling feature."""

    @abstractmethod
    def job(self):
        """Function which needs to be scheduled."""
        pass

    def run(self, interval: int):
        """
        Run scheduled function.

        This is blocking call.
        """
        scheduler = BlockingScheduler()
        scheduler.add_job(
            self.job,
            trigger='interval',
            seconds=interval,
        )
        scheduler.start()


class App(SchedulerMixin):
    """Main application."""

    def __init__(self, tickers: List[TickerAbstract], storage: StorageInterface):
        self.tickers = tickers
        self.storage = storage

    def job(self):
        """Gets new ticker values and stores it in storage."""
        tickers_data = []
        for ticker in self.tickers:
            value = ticker.get_value()
            name = ticker.get_name()
            ticker_data = TickerData(
                name=name,
                value=value,
            )
            tickers_data.append(ticker_data)

        try:
            self.storage.store(tickers_data)
        except ErrorStoreException as e:
            logging.error('Error store tickers data')
