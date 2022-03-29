CREATE TABLE data.ticker (
    datetime DateTime DEFAULT now(),
    name String,
    value Float32
) ENGINE = MergeTree() ORDER BY datetime
