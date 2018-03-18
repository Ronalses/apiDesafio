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

# OAuth

- Remove db.sqli3
- migrate  
  $ python manage.py makemigrations.  
  $ python manage.py migrate.

- Create user
  $ python manage.py createsuperuser --email admin@example.com --username admin.
- Register an application  
  go to http://localhost:8000/admin

  $ http://localhost:8000/api/applications/  

  Click on the link to create a new application and fill the form with the following data:  
  Name: just a name of your choice  
  Client Type: confidential  
  Authorization Grant Type: Resource owner password-based
- Get your token and use your API
  - curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/
- Response should be something like  
  {  
    "access_token": "<your_access_token>",  
    "token_type": "Bearer",  
    "expires_in": 36000,  
    "refresh_token": "<your_refresh_token>",  
    "scope": "read write groups"  
  }

- Grab your access_token and start using your new OAuth2 API:
  - curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/


