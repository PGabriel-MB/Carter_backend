# Carter (Backend API)

### Django Back-end api for Carter Project

This project was made for provide a RESTful API service for a Car Shop.

## Motivation

This project was created to study API back-end development and possibly have future earnings with it.

## Technologies

- Django
- Django REST Framework
- PostgreSQL

## Front-End Application

The front-end project for this application is [here](https://github.com/PGabriel-MB/TinnovaTeste)

## Documentation

The documentation was develop with **Postman**.

## Installation

First of all, create a **virtualenv** for this python Project.

```sh
python -m venv <VIRTUAENV_NAME>
```

Active your virtualenv:

```sh
source <VIRTUALENV_NAME>/bin/activate
```

After that, install all required project dependencies:

```sh
pip install -r requirements.txt
```

Then, run the project

```sh
python manage.py runserver
```

That's It!

## Environments Variables

```sh
SECRET_KEY=

ENVIRONMENT= # TEST for development and PROD for production

DB_NAME=
DB_USER=
DB_PASS=
DB_HOST=

EMAIL_BACKEND=
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=

```
