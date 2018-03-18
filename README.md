# APiRest Todo list.

- Create the project directory  
$ mkdir tutorial  
$ cd tutorial

- Create a virtualenv to isolate our package dependencies locally  
$ virtualenv -p python3 env
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


