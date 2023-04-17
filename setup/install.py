import os


os.system("git clone https://github.com/Samnji/Online_Markets.git")

os.system("cd Online_Markets/")

os.system("docker compose up -d")
os.system("docker exec online_markets_webapp_1 python3 manage.py migrate")