# Online_Markets

The Project core has two Apps:\
1. **Authentication** - The app enables the users to create accounts with strong passwords to improve the login page's security from bruteforce attacks.
2. **Advert** - This is where all the buying and selling of products takes place in the web application. 

Remember the urls are encrypted and encoded to prevent url bruteforce attack by an adversary.\
Admin and media urls haven't been encrypted and encoded yet for easy accessibility while debuging but advised to encrypted and encoded them in production.\
    - Encrypting and encoding file located at advert/encrypt_url.py

The web application has been dockerized. Run the install script to install the web app but git and docker must be installed in your machine first.

## Usage Disclaimer
The home or the landing page designed with the assumation of products should be more than 5  in order for the web application to be operational.

## How to set up and run  the Project
### Setup tools to install first
1. git
2. docker
3. docker-compose - optional, depends on which linux distro you are using.

### Setup automation
To automate the setup process\
*Windows*\
Copy the code in install.py file from the setup directory and paste it into install.py file that you will create on the directory where you want to save the Online Markets folder\
Then run the following command:\
    **python install.py**

*Linux*\
Download the python file from the setup directory by right clicking and selecting save linked content as and save it into the directory where you want to save the Online Markets folder\
Make sure to change the file to executable by running the following command:\
    **chmod 755 install.sh**\
Then run the following command:\
    **./install.sh**

### clone the project from github
To automate this process you may skip this\
Run the following commands to clone the repo and move into the directory:\
    **git clone https://github.com/Samnji/Online_Markets.git**\
    **cd into Online_Markets**

### run docker compose file
Run this command to run docker compose in detach mode:\
    **sudo docker compose up -d** 

Then run this command:\
    **sudo docker exec online_markets-webapp-1 python3 manage.py migrate**

And to create a superuser for the admin panel, run this command:\
    **sudo docker exec -it online_markets-webapp-1 python3 manage.py createsuperuser**


# Access The Application
Open click [App](http://127.0.0.1:8000) or type *http://127.0.0.1:8000* on your browser  to access the web application.

Access the post page first and try to post more than 5 products in order to view them in the home or landing page\
    Promo code - **"This is the promo code"**

To access the admin panel, click [Admin](http://127.0.0.1:8000/admin) or type *http://127.0.0.1:8000/admin* on your browser go to http://127.0.0.1:8000/admin

# Running The TestCase
Open a terminal on Online_Markets directory then run the following command:\
    **sudo docker exec online_markets-webapp-1 python3 manage.py test**