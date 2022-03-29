# Service for receiving and previewing trade data

## Choice of technologies

### Storage

To store a large amount of historical data with the possibility of their subsequent analysis, a columnar database is well suited. Chose Clickhouse from the tech stack list.

### Display

For display, it makes sense to use a ready-made solution with minimal development effort. I chose Grafana, also from the technology stack list.

## What can be improved

- Something more popular for clickhouse migrations
- Remove hardcoded clickhouse settings in grafana settings
- Some kind of control over whether data was written to the clickhouse in 1 second. It can be added to the queue, and write to the clickhouse in another thread.
- Add clickhouse waiter script.

## How to set dev environment

Create .env file

```shell
cp .env.example .env
vim.env
```

Run clickhouse in docker

```shell
docker-compose up --build -d clickhouse
```

Wait for clickhouse to start and run the rest services

```shell
docker-compose up --build -d generator_service grafana
```

Go to [grafana](http://localhost:3000/) and see dashboard Tickers _(login: admin, pass: admin)_.