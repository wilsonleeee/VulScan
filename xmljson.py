#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from create_db import VulTaskInfo
from xml.dom import minidom
from create_db import db


# WVS结果过滤
filter = {

    "color_white_list": ["orange", "red"],               # green,blue,orange,red四种级别

    "bug_black_list":
    [						                                            # 漏洞黑名单，过滤掉一些危害等级高，但没什么卵用的洞
    	"User credentials are sent in clear text"
    ],
}

                                                                        #解析扫描结果（XML格式）并存储数据库
class xml_db:

    def __init__(self,target,task_id):

        self.target = target

        self.task_id = task_id

    def parse_xml(self):

        bug_list = {}
        try:

            file = r'D:/Demo/' + str(self.target) + '/export.xml'           #读取本地存储的文件

            f = open(file)

            root = minidom.parse(f).documentElement

            ReportItem_list = root.getElementsByTagName('ReportItem')           #进行解析

            bug_list['bug'] = []

            bug_list['time'] = root.getElementsByTagName('ScanTime')[0].firstChild.data.encode('utf-8')       #读取相关的字段，格式是list

            bug_list['StartTime'] = root.getElementsByTagName('StartTime')[0].firstChild.data.encode('utf-8')

            bug_list['StartURL'] = root.getElementsByTagName('StartURL')[0].firstChild.data.encode('utf-8')

            if ReportItem_list:

                for node in ReportItem_list:

                    color = node.getAttribute("color")

                    name = node.getElementsByTagName("Name")[0].firstChild.data.encode('utf-8')

                    if color in filter['color_white_list'] and name not in filter['bug_black_list']:

                        temp = {}

                        temp['name'] = name

                        temp['color'] = color.encode('utf-8')

                        temp['details'] = node.getElementsByTagName("Details")[0].firstChild.data.encode('utf-8')

                        temp['affect'] = node.getElementsByTagName("Affects")[0].firstChild.data.encode('utf-8')

                        bug_list['bug'].append(temp)


        except Exception, e:

            sys.exit("Error in parse_xml: %s" % e)

        for i in range(0,len(bug_list['bug'])):

            color = bug_list['bug'][i]['color']
            if bug_list['bug'][i]['affect'] != '/':
                affect = bug_list['bug'][i]['affect']
            else:
                affect = bug_list['bug'][i-1]['affect']
            name = bug_list['bug'][i]['name']
            details = bug_list['bug'][i]['details']

            info = VulTaskInfo(task_id=self.task_id,target=bug_list['StartURL'], color=color, affect=affect, names=name ,details=details, StartURL=bug_list['StartURL'], ScanTime=bug_list['time'], StartTime=bug_list['StartTime'],FinishTime=bug_list['StartTime'],status='success')

            db.session.add(info)

            db.session.commit()

