# EasyInvestBank


**EasyInvestBank** is a django based project that has a news page, crypto price list and user registration/login with transaction system
between users that includes automatic currency transfer.

demo image

EasyInvestBank stores the data in SQLite database as it is lightweight and doesn't require an advanced database type.


# Installation and usage

Clone the repository and create a virtual environment. Currently, EasyInvestBank uses Python 3.10

### Create virtual environment with:
`python3.10 -m venv venv`

### Activate virtual enviorment with:
Linux command line: `source venv/bin/activate` <br/>
Windows command line: `venv/Scripts/activate.bat`

### Install the requirements with:
`pip install -r requirements.txt`

### Make migrations with:
`python manage.py makemigrations` <br/>
`python manage.py migrate` <br/>
and then uncomment the line `AUTH_USER_MODEL = 'User.Account'`
at the bottom of the `settings.py` file which is in the applications root folder

### Launch the application with:
python manage.py runserver from the application's root folder

Navigate to http://127.0.0.1:8000 or http://localhost:8000


# Admin panel

## Admin user creation:
You can create a superuser/admin in the terminal with the command </br>
`python manage.py createsuperuser`

Under country you can insert LT for Lithuania, LV for Latvia and EE for Estonia

You can access admin panel at http://127.0.0.1:8000/admin or http://localhost:8000/admin


# Database
SQLite database easyinvestbank.db is provided in the repository

For database migrations you can use python manage.py makemigrations and then python manage.py migrate


# Testing
Launch the tests for each app in the application's root folder with python manage.py test "app name"
for example if you want to test Bank app then you run python manage.py test Bank