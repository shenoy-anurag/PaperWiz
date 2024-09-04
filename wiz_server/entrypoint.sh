#!/bin/sh
export FLASK_APP=wsgi.py
export FLASK_DEBUG=1
# flask db migrate -m "Initial migration."
flask db upgrade
flask run --host=0.0.0.0 --port 5005
