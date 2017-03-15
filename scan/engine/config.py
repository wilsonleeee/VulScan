#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

HOSTNAME = '127.0.0.1'
DATABASE = 'demo'
USERNAME = 'root'
PASSWORD = '123456'
DB_URL = 'mysql://{}:{}@{}/{}'.format(USERNAME, '123456', HOSTNAME, DATABASE)


