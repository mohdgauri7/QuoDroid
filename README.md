# QuoDroid
#-------------------------- Required --------------------------
Homebrew
python3
Django


#-------------------------- Project Setup --------------------------

1).  Install Homebrew
cmd:- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2) Install python3
cmd: brew install python3

3) Install And Create virtualEnv
cmd: python3 -m venv venv

4) Activate Virtualenv 
cmd: source venv/bin/activate

5) Install Django
cmd: pip install Django==5.0

6) Upgrade Django
cmd: pip install --upgrade django

7) Create App
cmd: django-admin startproject App

8) Run App
python manage.py runserver

9) Test URL
http://127.0.0.1:8000/

#-------------------------- Project Setup Done --------------------------

#Views
Create a view to handle POST API and return required response.

#URLs
Add url path to maping view function to url path.



