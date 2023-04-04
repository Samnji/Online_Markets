# Online_Markets

# How to set up and run  the Project

# Note
The Project core Has The Two Apps:
#1. Authentication - The app enables the users to create accounts with strong passwords to improve the login page's security from bruteforce attacks.
#2. Advert - This is where all the buying and selling of products takes place in the web application. 

#Remember the urls are encrypted and encoded to prevent url bruteforce attack by an adversary.
#Admin and media urls haven't been encrypted and encoded yet for easy accessibility while debuging but advised to encrypted and encoded them in production - Encrypting and encoding file located at advert/encrypt_url.py

# Usage Disclaimer
#The home or the landing page designed with the assumation of products should than 5 in  in order for the web application to be operational.
#The project has not yet been dockerized
#You can choose to run the project inside a virtual environment or not

#Incase you want to run the project inside a virtual environment
# Create Virtual Environment - Optional
#To automate this process you may skip this

#Windows, run the commands below
#python -m venv .venv
#.venv/Scripts/activate

#Linux
#python3 -m venv .venv
#source .venv/bin/activate


# clone the project from github
#To automate this process you may skip this
#git clone https://github.com/Samnji/Online_Markets.git
#cd into Online_Markets

# Install Dependencies
#To automate this process you may skip this
#pip install -r requirements.txt - Windows only

# Changes to the setup before running the app
#Or to automate the process first create a postgres database could "market"

#Windows
#Then change directory to Online_Markets/setup then run
#./install.py - not ready yet just do the whole setup

#Linux
#Or to automate the process first create a postgres database named "market"
#Then change directory to Online_Markets/setup then run
#./install.sh

#Make sure you have changed the the postgres logins in the .env file before running the server
#Run the server by running this command on terminal
#python manage.py runserver - Windows
#python3 manage.py runserver - Linux

# Create SuperUser
#Run the command below on your terminal/cmd
#python manage.py createsuperuser

#Run the server by running this command on terminal
#python manage.py runserver


# Access The Application
#Open this ip on your browser http://127.0.0.1:8000 to access the web application

#Access the post page first and try to post more than 5 products in order to view them in the home or landing page
#Promo code - "This is the promo code"

#To access the admin panel, go to http://127.0.0.1:8000/admin

# Running The TestCase
#Open a terminal on Online_Markets directory then type
#Windows - python manage.py test
#Linux - python3 manage.py test

