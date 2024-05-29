# Gateway service

Client API, handles user registration and authentication

## To test the fuctionality:

### Gateway API endpoints:

**Swagger UI:**

http://localhost/docs

**Register a new user:**

```bash
curl -X 'POST' \
  'http://localhost:80/user/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "login": "login",
  "password": "password"
}'
```

**Login request:**

Returns access token

```bash
curl -X 'POST' \
  'http://localhost/user/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=login&password=password&scope=&client_id=&client_secret='
```

**Update user data request:**

Please, insert your access token

```bash
curl -X PUT http://localhost:80/user/update -H "Authorization: Bearer <your token>" -H "Content-Type: application/json" -d '{"name": "John", "surname": "Doe", "email": "john.doe@example.com"}'
```

## Troubleshooter:

*"Is the server running on that host and accepting TCP/IP connections?
2024-05-24 13:05:00 connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused
2024-05-24 13:05:00     Is the server running on that host and accepting TCP/IP connections?"*

If the postgres server is running for whatever reason even without you running to, do this:

```bash
psql
SHOW data_directory;
\q

pg_ctl stop -D {insert_path}
```