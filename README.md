# Book Store

This is an Online Book Store Concept created using Django Web Framework.


## Features

* Created user registrations and sending activation link for email and activating user through that link and reset password ,logoin ,logout user
* CURD Operations for BOOK done by only if user is staff
* CURD Operations with CART by user
* CURD Operations with WISHLIST by user
* Placing ORDER and getting order details 
* Templates for registration, login and logout user


## Prerequisites

Be sure you have the following installed on your development machine:

+ Python = 3.8
+ Django rest framework
+ Redis Server
+ Git
+ pip
+ Virtualenv

## Requirements

* Requirements added in requirements.txt file

## Install Redis Server

[Redis Quick Start](https://redis.io/topics/quickstart)

Run Redis server
```bash
redis-cli
```

## Project Installation

To setup a local development environment:

Create a virtual environment in which to install Python pip packages. With [virtualenv](https://pypi.python.org/pypi/virtualenv),
```bash
virtualenv venv            # create a virtualenv
source venv/bin/activate   # activate the Python virtualenv 
```

Install development dependencies,
```bash
pip install -r requirements.txt
```

Migrate Database,
```bash
python manage.py migrate
```

Run the web application locally,
```bash
python manage.py runserver #127.0.0.1:8000
```

Create Superuser,
```bash
python manage.py createsuperuser
```
Running Tests
```bash
 python manage.py test
 ```
