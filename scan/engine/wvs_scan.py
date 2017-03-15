#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, time,subprocess

from xmljson import xml_db

#创建扫描类
class wvs_scan:

    def __init__(self ,target,task_id):
        self.target = target.strip()
        self.task_id = task_id
        self.save_dir = 'D:\Demo\%s' % self.target
        self.scan_cmd = 'C:\Program Files (x86)\Acunetix\Web Vulnerability Scanner 10\wvs_console.exe /Profile default /SaveFolder D:\Demo\%s /GenerateReport /ReportFormat HTML /Verbose /ExportXML /Scan ' % str(self.target)
        self.filename = 'export.xml'
        self.pid = None
        self.scan_status = None

    #扫描的主函数
    def do_scan(self):
        #判断文件并且创建文件
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)
        #执行命令，创建子进程
        cmd = self.scan_cmd + self.target
        res = subprocess.Popen(cmd)
        res.wait()                                                     #等待子进程执行结束
        self.pid = res.pid
        self.scan_status = res.returncode

        while(True):
            time.sleep(5)
            listend = subprocess.Popen.poll(res)
            if listend is not None:
                save = xml_db(self.target,self.task_id)
                save.parse_xml()
                break
