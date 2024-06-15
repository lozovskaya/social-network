CREATE TABLE kafka_received
(
    type_action String,
    post_id UInt64,
    current_user_id UInt64,
    time_stamp DateTime
) ENGINE = Kafka
SETTINGS
    kafka_broker_list = 'social-network-kafka:29092',
    kafka_topic_list = 'new_action',
    kafka_group_name = 'clickhouse-group',
    kafka_format = 'JSONEachRow';


CREATE TABLE post_views (
    id UUID,
    post_id UInt64,
    time_stamp DateTime,
    user_id UInt64
) ENGINE = MergeTree
PRIMARY KEY (id)
ORDER BY id;


CREATE TABLE post_likes (
    id UUID,
    post_id UInt64,
    time_stamp DateTime,
    user_id UInt64
) ENGINE = MergeTree
PRIMARY KEY (id)
ORDER BY id;


CREATE MATERIALIZED VIEW kafka_to_post_views
TO post_views
AS SELECT
    generateUUIDv4() AS id,
    post_id,
    time_stamp,
    current_user_id AS user_id
FROM kafka_received
WHERE type_action = 'view';


CREATE MATERIALIZED VIEW kafka_to_post_likes
TO post_likes
AS SELECT
    generateUUIDv4() AS id,
    post_id,
    time_stamp,
    current_user_id AS user_id
FROM kafka_received
WHERE type_action = 'like';