from pydantic import BaseSettings, Field


class Clickhouse(BaseSettings):
    db_name: str = Field(..., env='CLICKHOUSE_DB')
    table_name: str = Field(..., env='CLICKHOUSE_TABLE')
    user: str = Field(..., env='CLICKHOUSE_USER')
    password: str = Field(..., env='CLICKHOUSE_PASSWORD')
    host: str = Field(..., env='CLICKHOUSE_HOST')
    port: int = Field(..., env='CLICKHOUSE_PORT')


class Settings(BaseSettings):
    scheduler_interval: int = 1  # Period new values generation
    ticker_count: int = 100  # Num of artificial trading instruments
    clickhouse: Clickhouse = Clickhouse()


settings = Settings()
