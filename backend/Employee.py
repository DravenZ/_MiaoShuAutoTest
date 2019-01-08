#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'yangluyao'
__date__ = '2018/11/14'
"""


from utils.Util import Request
from utils.Log import Log
from backend.Tool import Tool
from backend.Session import EmployeeSession
import json
from utils.Config import Config


class Employee(object):
    hosts = Config('config').data['hosts'][Config('config').data['run']]

    def __init__(self, account, password, Etype = 1):
        self.log = Log('Employee')
        self.tool = Tool()
        self.request = Request()
        emp = EmployeeSession(account, password)
        self.password = emp.password
        self.token, self.deviceId = emp.token, emp.deviceId
        if Etype == 1:
            self.employee_info = self.tool.miaoshu_query_user_info_by_mobile(account, 2)
            # self.log.logger.debug("员工信息：%s" % self.employee_info)
        elif Etype == 2:
            self.employee_info = self.tool.miaoshu_query_user_info_by_email(account, 2)
        else:
            return
        if self.employee_info != ():
            self.employee_info = self.employee_info[0]
            self.employee_id = self.employee_info["id"]
            self.employee_real_name = self.employee_info["real_name"]
            self.employee_nickname = self.employee_info["nickname"]
            self.employee_sex = self.employee_info["sex"]
            self.employee_mobile = self.employee_info["mobile"]
            self.employee_email = self.employee_info["email"]
            self.employee_account_status = self.employee_info["account_status"]
            self.employee_account_type = self.employee_info["account_type"]
            self.employee_head_img = self.employee_info["head_img"]
            self.employee_register_time = self.employee_info["create_time"]
            self.employee_edit_time = self.employee_info["edit_time"]
            self.employee_channel_shop_id = None

    def employee_logout(self):
        """
        员工退出登录
        :return:
        """
        data = {
             "token": self.token}
        response = Request().post(url=self.hosts['MS_PASSPORT'] + "/admin/service/logout", data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")


if __name__ == '__main__':
    #emp = Employee("18919028888", "123456")
    Elogout = Employee("18328433208", "123456")
    Elogout.employee_logout()
