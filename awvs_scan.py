#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
from flask import jsonify

'''
    创建扫描任务
    post json to http://url/scan
    example:
        {
            "token": "34b9a295d037d47eec3952e9dcdb6b2b",              // must, client token
            "target": "https://ops.100tal.com",                       // must, gitlab url
            "config": "kill",                                         // must, the project cmd
        }
'''                                                        #创建扫描类
class wvs_scan:

    def __init__(self ,target,task_id,config1,config2,config3):
        self.target = target.strip()
        self.config1 = config1.strip()
        self.config2 = config2.strip()
        self.config3 = config3.strip()
        self.task_id = task_id
        self.save_dir = 'D:\Demo\%s' % str(self.task_id)
        self.scan_cmd = 'D:\Web Vulnerability Scanner 10\wvs_console.exe /Profile default /SaveFolder D:\Demo\%s /GenerateReport /ReportFormat HTML /Verbose /ExportXML /Scan ' % str(self.task_id)
        self.filename = 'export.xml'
        self.pid = None

                                                           #扫描的主函数
    def do_scan(self):
                                                           #判断文件并且创建文件
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)

                                                           #执行命令，创建子进程
        cmd = self.scan_cmd + self.target
        res = subprocess.Popen(cmd)

        process_pid = res.pid                              #获取进程ID

        return jsonify(status=res, pid=process_pid)        #返回信息
        # res.wait()                                       #等待子进程执行结束

                                                           #关闭扫描进程
    def kill_scan(self):

        if self.config2 == "kill":

            pid = self.pid                                #获取进程ID进行分析
            killer = os.kill(pid)                         #执行关闭进程操作

            return jsonify(status=killer, pid=pid)





















