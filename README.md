# shlink
#### URL Shortener, made in Django 3.0.5 (Python 3.x) and Bootstrap 4.
The project is at https://shlink-project-asharma.herokuapp.com/.


### Running Locally

***Install Python (if you didn't), and Django 3***
1. Download Python 3.x: https://www.python.org/downloads/
2. Install Django
> pip3 install django==3.0.5
3. Run the web application
> python3 manage.py runserver 
4. Go to the URL address in the console (http://127.0.0.1:8000/)

***You may need to make migrations***
1. Make migration files
> python3 manage.py makemigrations
2. Apply migration files, so the models actually work
> python3 manage.py migrate
