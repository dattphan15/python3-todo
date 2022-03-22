# Django Docker - Python3-todo
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:dattphan15/python3-todo.git
$ cd python3-todo
```

In the root folder `python3-todo/` , launch and build the docker containers:

```sh
$ docker-compose up --build
```

Upon success, the above command should launch 3 containers (nginx, app, postgres), and automatically make and run migrations.

To view running containers:
```sh
$ docker ps
```

Shut down docker and remove all volumes attached:
```sh
$ docker-compose down -v --rmi all
```

Note: Postgres is configured in this docker container to run on port 5432, so make sure that port isn't occupied by anything else. If another instance of postgres is running, kill the process and then proceed to launch docker.


### To Do List
`http://0.0.0.0:8000/tasks`.

### Admin
`http://0.0.0.0:8000/admin`


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
