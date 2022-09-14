EasyInvestBank
EasyInvestBank is a django based project that has a news page, crypto price list and user registration/login with transaction system
between users that includes automatic currency transfer.

demo image

EasyInvestBank stores the data in SQLite database as it is lightweight and doesn't require an advanced database type.


Installation and usage


Local installation
Clone the repository and create a virtual environment for it. Currently, EasyInvestBank uses Python 3.10

python3.10 -m venv venv
Linux command line: source venv/bin/activate
Windows command line: venv/Scripts/activate.bat
Install the requirements

pip install -r requirements.txt

Launch the application with python manage.py runserver from the application's root folder

Navigate to http://127.0.0.1:5000 or http://localhost:5005


Database
SQLite database easyinvestbank.db is provided in the repository

For database migrations you can use python manage.py makemigrations and then python manage.py migrate


Testing
Launch the tests for each app in the application's root folder with python manage.py test "app name"
for example if you want to test Bank app then you run python manage.py test Bank