## To run database:
1.
```bash
docker compose up -d
```

2. Migrations (from the root)

**Gateway:**
```bash
docker run --rm --network="social-network-network" -v ./gateway/migrations:/app liquibase/liquibase:4.19.0 --log-level ERROR --defaultsFile=/app/dev.properties update
```