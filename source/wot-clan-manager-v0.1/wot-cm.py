__author__ = 'Andrzej Stroiński'
# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE = './db/wot-cm.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


print(__name__)

if __name__ == '__main__':
    app.run().globals()
    