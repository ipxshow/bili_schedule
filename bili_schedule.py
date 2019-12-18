#!/usr/bin/env python
# coding=utf-8
import schedule
import time
import os
import requests


'''user config'''
# 用户密码
password = ''
'''
server酱的sckey
在这里申请http://sc.ftqq.com/3.version
留空则不推送到微信
'''
sckey = ''
'''
定义开始和结束时间
格式为00:00
'''
start_time = '13:18'  
stop_time = '13:19'  


class BiliSchedule():
    def __init__(self, start_time, stop_time, password, sckey):
        self.__start_time = start_time
        self.__stop_time = stop_time
        self.__password = password
        self.__sckey = sckey
        self.__send_message_url = 'https://sc.ftqq.com/{}.send'.format(sckey)

    def bili_service_start(self):
        status = os.system("systemctl is-active mysqld")
        # print(type(status))
        if status == 0:
            print("服务正在运行中...")
        else:
            print("启动服务")
            res = os.system(
                "echo {}|sudo -S systemctl start mysqld".format(self.__password))
            if res == 0:
                print("服务启动成功")
                message = {'text': '服务启动成功'}
                self.send_to_wechat(message)

    def bili_service_stop(self):
        print("停止biliHelper脚本")
        res = os.system(
            "echo {}|sudo -S systemctl stop mysqld".format(self.__password))
        if res == 0:
            print("服务停止成功")
            message = {'text': '服务停止成功'}
            self.send_to_wechat(message)

    def send_to_wechat(self, message):
        # message ={"text":"服务器测试"}
        if self.__sckey:
            res = requests.post(self.__send_message_url, params=message)
            # print(res.text)

    def do_schedule(self):
        schedule.every().day.at(self.__start_time).do(self.bili_service_start)
        schedule.every().day.at(self.__stop_time).do(self.bili_service_stop)


bili = BiliSchedule(start_time, stop_time, password, sckey)
bili.do_schedule()
while True:
    schedule.run_pending()
    time.sleep(1)

