# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class schedulerAction(object):

    def __init__(self, scheduler):
        self.log = Log('scheduler')
        self.request = Request()
        self.scheduler = scheduler

    def _api_job_cron(self, corn, appName, taskId, callbackURL, jsonParam, needCallback, replaceOnExist, retry):
        data = {'_tk_': self.scheduler.token, '_deviceId_': self.scheduler.device_id, 'corn': corn, 'appName': appName, 'taskId': taskId, 'callbackURL': callbackURL, 'jsonParam': jsonParam, 'needCallback': needCallback, 'replaceOnExist': replaceOnExist, 'retry': retry}
        response = self.request.post(url='http://dev.ms.scheduler.sjnc.com/api/job/cron', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_job_once(self, triggerDateTime, appName, taskId, callbackURL, jsonParam, needCallback, replaceOnExist, retry):
        data = {'_tk_': self.scheduler.token, '_deviceId_': self.scheduler.device_id, 'triggerDateTime': triggerDateTime, 'appName': appName, 'taskId': taskId, 'callbackURL': callbackURL, 'jsonParam': jsonParam, 'needCallback': needCallback, 'replaceOnExist': replaceOnExist, 'retry': retry}
        response = self.request.post(url='http://dev.ms.scheduler.sjnc.com/api/job/once', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_job_repeat(self, repeat):
        data = {'_tk_': self.scheduler.token, '_deviceId_': self.scheduler.device_id, 'repeat': repeat}
        response = self.request.post(url='http://dev.ms.scheduler.sjnc.com/api/job/repeat', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
