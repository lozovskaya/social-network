# Social Network

## Лозовская Алина, БПМИ2110

To run the service, do the following:

1. Generate Secret key for JWT:
    ```bash
    openssl rand -hex 32
    ```
2. Add the Secret key to the file .env to gateway/src with the following information:
    ```bash
    SECRET_KEY=<Your secret key>
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```
3. Run docker-compose file:
    ```bash
        docker compose up --build -d 
    ```
4. To check the state of the Clickhouse database:
    ```bash
       docker exec -it social-network-clickhouse clickhouse-client
    ```
    ```bash
        SELECT * FROM post_views;
        SELECT * FROM post_likes;
    ```
    or
    ```bash
        docker run -p 5521:5521 ghcr.io/caioricciuti/ch-ui:latest
    ```
    user: default

    logs:
    ```
        docker exec -it social-network-clickhouse cat /var/log/clickhouse-server/clickhouse-server.log
        docker exec -it social-network-clickhouse cat /var/log/clickhouse-server/clickhouse-server.err.log
    ```