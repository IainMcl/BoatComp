# Graphql API

Graphql api is built using [Graphene](https://graphene-python.org/) and run on
a [Flask](https://flask.palletsprojects.com/en/1.1.x/) server.

## Setting up the server

On Windows to set the Flask app use

```bash
set FLASK_APP=api.py
```

If the api host location changes this will also need to be moved.

## Running the server

To run the flask server, run

```bash
flask run
```

This will start development the server on `http://localhost:5000` by default.

With using a graphql api the only open end point for main interactions is
`/graphql`.
