#!/bin/bash

git clone https://github.com/Samnji/Online_Markets.git

cd Online_Markets/
sudo docker compose up
# . .venv/bin/activate

# To backup and restore databases to and from a docker container
# docker exec <container_name_or_id> pg_dump -U <database_user> <database_name> > backup.sql
# cat backup.sql | docker exec -i <container_name_or_id> psql -U <database_user> <database_name>
