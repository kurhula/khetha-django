khetha-django
=============

Quickstart
----------

Collect static assets (``build/assets``):

```shell
npm install
./build-assets.sh
```

Start PostgreSQL:

```
docker-compose up
```

Set up database tables first time you set up the database

```
docker-compose run --rm web django-admin migrate
docker-compose run --rm web django-admin createsuperuser
```

Load some development data

```
docker-compose run --rm web django-admin loaddata /root/.local/lib/python3.7/site-packages/khetha/fixtures/sample-task-data.json
```

To attach a `psql` shell:

    docker-compose exec --user postgres db psql

Run the tests:

```
tox
```

Create an environment and run a development server:

```
cp -p .env.example .env

pipenv shell
pipenv install --dev

django-admin check
django-admin runserver
```

(Or use PyCharm.)


Updating dependencies
---------------------

Use Pipenv, and run [requirements-update.sh] after any Pipfile.lock update.

[requirements-update.sh]: requirements-update.sh


Working with data
-----------------

To dump the task data, or update [src/khetha/fixtures/sample-task-data.json]:

```shell
django-admin dumpdata --indent 2 khetha.task khetha.question khetha.answeroption

meld <(django-admin dumpdata --indent 2 khetha.task khetha.question khetha.answeroption) src/khetha/fixtures/sample-task-data.json
```

[src/khetha/fixtures/sample-task-data.json]: src/khetha/fixtures/sample-task-data.json
