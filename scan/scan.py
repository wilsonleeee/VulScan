#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask ,jsonify
from flask import render_template  ,request
from engine import wvs_scan
from engine.create_db import VulTaskInfo
from multiprocessing import Process, Queue

import random
import logging

queue_waiting = Queue()
queue_scaning = Queue(10000)

logging = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/' ,methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/scan',methods=['POST'])
def add_task():
    targets = request.form['target'].split(' ')
    token = request.form['token']

    task_id = random.randint(1, 1000000)

    if not token or token == "":
        return jsonify(result=u'Please input token!')

    for target in targets:
        tar = [target, task_id]
        queue_waiting.put(tar)

    return jsonify(task_id=task_id, message='success', tagets=targets)

def queue_get(queue_waiting, queue_scaning):

    while True:
        tar = queue_waiting.get()
        target = tar[0]
        task_id = tar[1]
        queue_scaning.put(1)
        result = wvs_scan.wvs_scan(target, task_id)
        result.do_scan()


if __name__ == '__main__':

    Process(target=queue_get,args=(queue_waiting, queue_scaning)).start()
    app.run()