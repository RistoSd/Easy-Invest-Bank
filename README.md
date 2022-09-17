# EasyInvestBank


**EasyInvestBank** is a django based project that has a news page, crypto price list and user registration/login with transaction system
between users that includes automatic currency transfer.

![Example image](https://user-images.githubusercontent.com/45123135/190678339-4ec67aaa-118c-4de7-a6ff-06209e662296.png)

EasyInvestBank stores the data in MySQL database.


# Installation and usage

Clone the repository and create a virtual environment. Currently, EasyInvestBank uses Python 3.10

### Create virtual environment with:
`python3.10 -m venv venv`

### Activate virtual enviorment with:
Linux command line: `source venv/bin/activate` <br/>
Windows command line: `venv/Scripts/activate.bat`

### Install the requirements with:
`pip install -r requirements.txt`

### Database:
Inside the command line:
Enter mysql command line with `mysql -u root -p`
Enter your mysql password
Create database with `'CREATE DATABASE 'NAME';`
Then enter your database information in the `DATABASE` section inside the `settings.py` file which resides in the EasyInvestBank root folder

### Make migrations with:
`python manage.py makemigrations` <br/>
`python manage.py migrate` <br/>
and then uncomment the line `AUTH_USER_MODEL = 'User.Account'`
at the bottom of the `settings.py` file which is in the applications root folder

### Launch the application with:
`python manage.py runserver` from the application's root folder

Navigate to http://127.0.0.1:8000 or http://localhost:8000


Keep in mind that when a new user is created they have a balance of 0, you can 
add balance to a user in the admin panel.

# Admin panel

### Admin user creation:
You can create a superuser/admin in the terminal with the command </br>
`python manage.py createsuperuser`

Under country you can insert LT for Lithuania, LV for Latvia and EE for Estonia

You can access admin panel at http://127.0.0.1:8000/admin or http://localhost:8000/admin


# Database
This project uses the MySQL database.

For database migrations you can use `python manage.py makemigrations` and then `python manage.py migrate`


# Testing
Launch the tests for each app in the application's root folder with python manage.py test "app name" </br>
for example if you want to test Bank app then you run `python manage.py test Bank`