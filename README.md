# APiRest Todo list.

- Create the project directory  
$ mkdir tutorial  
$ cd tutorial

- Create a virtualenv to isolate our package dependencies locally  
$ virtualenv env  
$ source env/bin/activate  
$ git clone repository.  
$ cd repository.

- install dependencies  
$ pip install -r requirements.txt

- migrate  
$ python manage.py makemigrations.  
$ python manage.py migrate.

- run project  
$ python manage.py runserver  
  go to http://127.0.0.1:8000/api/

- http://127.0.0.1:8000/api/users/
  - GET 
  - POST  
- http://127.0.0.1:8000/api/:userId/todo-list/
  - GET
  - POST
- http://127.0.0.1:8000/api/:userId/todo-list/:identifier/
  - GET
  - PUT

The api has Auth Token and oAuth Authentication.
see the branch tokenAuthentication and oauth.


# Auth

- Remove db.sqlite3
- migrate  
  $ python manage.py makemigrations.  
  $ python manage.py migrate.
- Create User
  - python manage.py createsuperuser --email admin@example.com --username admin
- run project  
  $ python manage.py runserver  
- Get Token
  - curl -d '{"username":"admin", "password":"adminadmin"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/token-auth/  
  {"token":"15914b435918b273c5cfaa2a898d2f761ade719b"}

  - Add in the Headers: "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"