#!/bin/bash

git clone https://github.com/Samnji/Online_Markets.git

cd Online_Markets/

sudo docker compose up -d
sudo docker exec online_markets-webapp-1 python3 manage.py migrate

# To backup and restore databases to and from a docker container
# docker exec online_markets-database-1 pg_dump -U postgres market > backup.sql
# cat backup.sql | docker exec -i online_markets-database-1 psql -U postgres market 
