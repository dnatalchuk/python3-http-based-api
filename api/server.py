#!/usr/bin/env python3

import flask
from flask import request, jsonify
import sqlite3
from sqlite3 import Error
from sqlalchemy import create_engine

app = flask.Flask(__name__)
db_connect = create_engine('sqlite:///users.db')


@app.route('/', methods=['GET'])
def api_all():
    conn = db_connect.connect()
    query = conn.execute('SELECT * FROM Users;')
    result = query.cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
