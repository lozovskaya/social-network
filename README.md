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
        docker compose up -d
    ```