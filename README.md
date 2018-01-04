# djjet-template
my django 2.0 (py 3.6) + django-jet + django-smoke-tests starting template

rename: hours (or _template) -> myapp
  - in folder names
  - in manage.py

- start virtualenv: . ve_myapp/bin/activate

- pip install -U -r requirements.txt

- ./manage.py startapp
- ./manage.py migrate

- change secretkey in myapp_site/.env: ./manage.py generate_secret_key (copy from file and remove it)

- run smoke tests (admin get tests): ./manage.py smoke_tests -g
