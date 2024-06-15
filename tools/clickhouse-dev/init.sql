CREATE TABLE kafka_received
(
    type_action String,
    post_id UInt64,
    current_user_id UInt64,
    time_stamp DateTime,
    post_owner UInt64
) ENGINE = Kafka
SETTINGS
    kafka_broker_list = 'social-network-kafka:29092',
    kafka_topic_list = 'new_action',
    kafka_group_name = 'clickhouse-group-v1',
    kafka_format = 'JSONEachRow';


CREATE TABLE post_views (
    post_id UInt64,
    time_stamp DateTime,
    user_id UInt64,
    post_owner UInt64
) ENGINE = MergeTree
ORDER BY post_id;


CREATE TABLE post_likes (
    post_id UInt64,
    time_stamp DateTime,
    user_id UInt64,
    post_owner UInt64
) ENGINE = MergeTree
ORDER BY post_id;


CREATE MATERIALIZED VIEW kafka_to_post_views
TO post_views
AS SELECT
    post_id,
    time_stamp,
    current_user_id AS user_id,
    post_owner
FROM kafka_received
WHERE type_action = 'view';


CREATE MATERIALIZED VIEW kafka_to_post_likes
TO post_likes
AS SELECT
    post_id,
    time_stamp,
    current_user_id AS user_id,
    post_owner
FROM kafka_received
WHERE type_action = 'like';