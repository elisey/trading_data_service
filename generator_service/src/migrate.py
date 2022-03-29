"""This is script for applying migrations to clickhouse storage."""

from clickhouse_migrate.migrate import migrate

from core import settings


def main():
    config = settings.settings.clickhouse

    migrate(
        config.db_name,
        'migrations',
        config.host,
        config.user,
        config.password,
        config.port
    )


if __name__ == '__main__':
    main()
