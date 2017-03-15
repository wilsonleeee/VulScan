#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import INTEGER
from config import DB_URL

import time

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)

class VulTaskInfo(db.Model):

    __tablename__ = 'Final'
    __table_args__ = {'extend_existing': True}

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False,unique=True)
    task_id = db.Column(db.Integer, nullable=False, default=None)
    target = db.Column(db.String(255), nullable=False, default=None)
    color = db.Column(db.String(255), nullable=False, default=None)
    affect = db.Column(db.String(255), nullable=False, default=None)
    names = db.Column(db.String(255), nullable=False, default=None)
    details = db.Column(db.String(255), nullable=False, default=None)
    ScanTime = db.Column(db.String(255), nullable=False, default=None)
    StartTime = db.Column(db.String(255), nullable=False, default=None)
    FinishTime = db.Column(db.String(255), nullable=False, default=None)
    status = db.Column(db.String(255), nullable=False, default=None)
    created_at = db.Column(db.String(255), nullable=False, default=None)
    updated_at = db.Column(db.String(255), nullable=False, default=None)

    def __init__(self,task_id,target,color,affect,names,details,StartURL,ScanTime,StartTime,FinishTime,status,creatd_at=None,updated_at=None):

        """
        :rtype: object
        """
        self.task_id = task_id
        self.target = target
        self.StartURL = StartURL
        self.ScanTime = ScanTime
        self.StartTime = StartTime
        self.FinishTime = FinishTime
        self.color = color
        self.affect = affect
        self.names = names
        self.details = details
        self.status = status
        self.created_at = creatd_at
        self.updated_at = updated_at

        current_time = time.strftime('%Y-%m-%d %X', time.localtime())

        if creatd_at is None:
            self.created_at = current_time
        else:
            self.created_at = creatd_at
        if updated_at is None:
            self.updated_at = current_time
        else:
            self.updated_at = updated_at

    def __repr__(self):
        return '<task_info %r - %r>' % (self.id, self.target)

db.create_all()