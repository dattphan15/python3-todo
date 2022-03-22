# Django Docker - Python3-todo
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:dattphan15/python3-todo.git
$ cd python3-todo
```

Note: Postgres is configured in this docker container to run on port 5432, so make sure that port isn't occupied by anything else. If another instance of postgres is running, kill the process and then proceed to launch docker.

In the root folder `python3-todo/` , launch and build the docker containers:

```sh
$ docker-compose up --build
```

Upon success, the above command should launch 3 containers (nginx, app, postgres), and automatically make and run migrations.

Next, you will need to login to the docker container and create a superuser to access the Django Admin `http://0.0.0.0:8000/admin` (steps below).

1. Find the docker container ID:
```sh
$ docker ps

CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS          PORTS                                       NAMES
3e9974669ee5   django-docker-compose_nginx   "/docker-entrypoint.…"   12 seconds ago   Up 11 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp           django-docker-compose_nginx_1
58064eafc2a8   django-docker-compose_app     "sh /entrypoint.sh p…"   12 seconds ago   Up 11 seconds   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   django-docker-compose_app_1
b601f871b587   postgres:12.2                 "docker-entrypoint.s…"   12 seconds ago   Up 12 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   db
```

2. Replace the [CONTAINERID] with the CONTAINER ID above.
```sh
$ docker exec -t -i [CONTAINERID] bash
//
$ docker exec -t -i 58064eafc2a8 bash
```

3. Create superuser, and follow prompts to provide your email, username and password.
```sh
root@58064eafc2a8:/app# python manage.py createsuperuser
```

4. Now you can access the Django Admin `http://0.0.0.0:8000/admin` with the credentials you just created.

5. To visit the main todo app, `http://0.0.0.0:8000/tasks`.


To shut down docker and remove all volumes attached:
```sh
$ docker-compose down -v --rmi all
```
___

### To Do List
`http://0.0.0.0:8000/tasks`.


![Registration](https://github.com/dattphan15/python3-todo/blob/master/docs/media/3.registration.PNG)


![Login](https://github.com/dattphan15/python3-todo/blob/master/docs/media/4.login.PNG)


![Task List](https://github.com/dattphan15/python3-todo/blob/master/docs/media/5.todo-tasks.PNG)


### Admin
`http://0.0.0.0:8000/admin`

![Django Admin](https://github.com/dattphan15/python3-todo/blob/master/docs/media/1.django-admin.PNG)

![Django Rest Auth](https://github.com/dattphan15/python3-todo/blob/master/docs/media/2.django-auth.PNG)

___

# Project Objectives
___
Overview  
You have three primary tasks:

A)	Create a TODO server app with Python, Django, and PostgreSQL. The primary interface is a REST API. Also provide an admin dashboard using Django’s Admin Site system. 

B)	Configure the app to run on a Gunicorn WSGI server, behind an NGINX instance acting as a reverse-proxy. Deploy all components — Django/Gunicorn, Postgres, NGINX — as Docker containers managed by docker-compose (i.e, docker-compose up should bring up the entire system and docker-compose down to shut everything down).

C)	Create a Python script which tests the REST API.  
Requirements:  
●	Python 3.8.x  
●	Django 3.x  
●	docker-compose 1.28.x  
●	Docker Engine 20.10.x  
●	Gunicorn 20.x  
●	NGINX 1.18.x  
●	PostgreSQL 12.x  
●	Ubuntu 18.04  

TODO Server App
Each TODO is composed of the following fields:

1.	Task ID
2.	User ID
3.	Task Title
4.	Task Description
5.	Task State  
a.	TODO  
b.	In Progress  
c.	Done  
6.	Task Due Date

The TODO server app should provide REST API endpoints to handle the following operations.

1.	Add a TODO. 
2.	Delete a TODO.
3.	Update a TODO.
4.	List all TODOs.  
a.	Filter TODOs by one or more fields.

For the list operation, add the ability to sort and filter by the TODO fields.
Admin Dashboard
Create an admin dashboard using Django’s Admin Site system. It should be able to create user accounts and display each user’s account info.
User Authentication
The Admin Dashboard should provide an API key for each newly created user account.
Test Script
Create a Python script which tests TODO app’s REST API as a normal user. The script should get the API key via an environment variable or a command-line parameter.

Note, this is different from a Django unit test as its purpose is to test the entire deployment whose entry point is NGINX.  
Deployment  
TODO Server App  
User docker-compose to deploy the TODO server app as a collection of Docker containers:

1.	Django/Gunicorn
2.	PostgreSQL
3.	NGINX

### Test Script  
Don’t use Docker for the test script. Instead, assume the test script will be run directly on an Ubuntu 18.04 VM with Python 3.8 and pip already installed and in the path. I.e., you may assume entering python in the terminal will run Python 3.8 interpreter. And if the script requires additional packages from PyPI, then use a virtualenv, specifically via Python 3’s venv. 
