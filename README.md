# EA Bot Backend

Django backend for the EA Bot.

## Installation

This project uses poetry to manage its dependencies. Installation instructions for poetry can be found
at https://python-poetry.org/docs/#installation. However, a `pyproject.toml` is present at the project root which can be
used to install the required dependencies.

If you're already using poetry use:

`poetry install`

## Setup server

To set up the server first create the DB migrations using:

```
python manage.py makemigrations
python manage.py migrate
```

## Run Server

Run using

`python manage.py runserver`

## Endpoints

### api/permalinks

Retrieves a json file containing all the permalinks from the permalinks.txt file.

## Google Cloud Storage

Google Cloud Storage is setup to retrieve the file that contains the permalinks saved by
the [reddit-meaningfu-carrers-bot](https://github.com/maximumpeaches/reddit-meaningful-careers-bot). You will need a key
file for the GCP service account used to access the GC Storage.
For now this file has to be stored in a `secrets` directory located on the root folder.

## ToDos

- [ ] Manage secrets (e.g. service account keys) via GC Secret Manager
- [ ] Deploy to GCP
- [ ] Change DB to PostgreSQL
- [ ] Setup GC SQL storage
- [ ] Configure Django to serve a Svelte frontend