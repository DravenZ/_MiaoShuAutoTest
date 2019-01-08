# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class checkerAction(object):

    def __init__(self, checker):
        self.log = Log('checker')
        self.request = Request()
        self.checker = checker

    def _admin_check_bill_detail_detail(self, id):
        data = {'_tk_': self.checker.token, '_deviceId_': self.checker.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.checker.sjnc.com/admin/check-bill-detail/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_check_bill_detail_list(self, pn, ps, platform, channel, billTime, platformNo, channelNo, checkStatus, differType, handleStatus):
        data = {'_tk_': self.checker.token, '_deviceId_': self.checker.device_id, 'pn': pn, 'ps': ps, 'platform': platform, 'channel': channel, 'billTime': billTime, 'platformNo': platformNo, 'channelNo': channelNo, 'checkStatus': checkStatus, 'differType': differType, 'handleStatus': handleStatus}
        response = self.request.post(url='http://dev.ms.checker.sjnc.com/admin/check-bill-detail/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_check_bill_result_list(self, pn, ps, platform, channel, billDate, checkStatus):
        data = {'_tk_': self.checker.token, '_deviceId_': self.checker.device_id, 'pn': pn, 'ps': ps, 'platform': platform, 'channel': channel, 'billDate': billDate, 'checkStatus': checkStatus}
        response = self.request.post(url='http://dev.ms.checker.sjnc.com/admin/check-bill-result/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_check_bill_task_check_bill(self, platform, channel, billDate):
        data = {'_tk_': self.checker.token, '_deviceId_': self.checker.device_id, 'platform': platform, 'channel': channel, 'billDate': billDate}
        response = self.request.post(url='http://dev.ms.checker.sjnc.com/admin/check-bill-task/check-bill', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_check_bill_task_list(self, pn, ps, platform, channel, billDate, checkStatus):
        data = {'_tk_': self.checker.token, '_deviceId_': self.checker.device_id, 'pn': pn, 'ps': ps, 'platform': platform, 'channel': channel, 'billDate': billDate, 'checkStatus': checkStatus}
        response = self.request.post(url='http://dev.ms.checker.sjnc.com/admin/check-bill-task/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_check_bill_task_re_check_bill(self, 任务ID):
        data = {'_tk_': self.checker.token, '_deviceId_': self.checker.device_id, '任务ID': 任务ID}
        response = self.request.post(url='http://dev.ms.checker.sjnc.com/admin/check-bill-task/re-check-bill', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
