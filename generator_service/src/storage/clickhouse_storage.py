import logging
from dataclasses import asdict
from typing import List

import clickhouse_driver
from clickhouse_driver import Client

from core.settings import settings
from storage.interface import StorageInterface, TickerData, ErrorStoreException


class ClickhouseStorage(StorageInterface):
    """Clickhouse storage."""

    def __init__(self):
        config = settings.clickhouse
        self.table_name = config.table_name

        self.client = Client(
            config.host,
            database=config.db_name,
            user=config.user,
            password=config.password,
            port=config.port
        )

    def store(self, tickers: List[TickerData]):
        """Store array of tickers data to clickhouse."""
        logging.info('Write tickers to clickhouse')

        tickers = [asdict(ticker) for ticker in tickers]

        try:
            self.client.execute(f'INSERT INTO {self.table_name} (name, value) VALUES', tickers)
        except clickhouse_driver.errors.Error as e:
            logging.error(e)
            raise ErrorStoreException('Error store tickers data to clickhouse')
