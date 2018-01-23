## database PostgreSQL

https://www.postgresql.org/download/

`/Library/PostgreSQL/9.6/bin/psql -U postgres`

`CREATE DATABASE my_postgres_db OWNER postgres;`

`\c my_postgres_db`

`CREATE TABLE my_table (firstname varchar(40), lastname varchar(40));`

`my_postgres_db < db/users.sql`

## start server http://localhost:5000/

`export FLASK_APP=onelab_test.py`

`export FLASK_DEBUG=1`

`flask run`
