import logging
from typing import List

from app import App
from core.settings import settings
from movement_generator.random_movement import RandomMovementGenerator
from storage.clickhouse_storage import ClickhouseStorage
from ticker.ticker_generator import TickerGenerator

logging.getLogger().setLevel(logging.INFO)


def _create_tickers() -> List[TickerGenerator]:
    """Create artificial trading instrument objects."""
    tickers = []
    for i in range(settings.ticker_count):
        ticker = TickerGenerator(f'ticker_{i:02}', RandomMovementGenerator())
        tickers.append(ticker)
    return tickers


def main():
    """Runs everything."""
    tickers = _create_tickers()
    storage = ClickhouseStorage()

    app = App(tickers, storage)
    app.run(settings.scheduler_interval)


if __name__ == '__main__':
    main()
