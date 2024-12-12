#!/bin/bash

export PYTHONDONTWRITEBYTECODE=yes

export MARIADB_HOST=database.local
export MARIADB_PORT=3306
export MARIADB_DATABASE=myapi_db
export MARIADB_USER=myapi_user
export MARIADB_PASSWORD=s3cr3tp4ssw0rd

gunicorn --reload --bind=127.0.0.1:8080 myapi:app
