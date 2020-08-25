-- DROP TABLE avocado;
-- DROP TABLE gas;
-- DROP TABLE tot_transport;
-- DROP TABLE avo_transport;

CREATE TABLE avocado (
date DATE PRIMARY KEY,
average_price FLOAT,
total_volume FLOAT,
small_avocados_sold FLOAT,
large_avocados_sold FLOAT,
xl_avocados_sold FLOAT,
type VARCHAR,
year INT,
region VARCHAR
);

CREATE TABLE gas (
date DATE PRIMARY KEY,
gas_all_grades FLOAT,
regular FLOAT,
midgrade FLOAT,
premium FLOAT,
diesel FLOAT
);

CREATE TABLE tot_transport (
date DATE,
origin VARCHAR,
destination VARCHAR,
transport_distance INT,
commodity VARCHAR,
low_weekly_rate INT,
high_weekly_rate INT,
average_weekly_rate INT,
avg_rate_per_mile_ratio FLOAT,
availability_score INT
);

CREATE TABLE avo_transport (
date DATE,
origin VARCHAR,
destination VARCHAR,
transport_distance INT,
commodity VARCHAR,
low_weekly_rate INT,
high_weekly_rate INT,
average_weekly_rate INT,
avg_rate_per_mile_ratio FLOAT,
availability_score INT
);