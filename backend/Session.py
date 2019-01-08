#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Pengfei'
__date__ = '2018/11/5'
"""


from utils.Util import Request
from utils.Config import Config
# from backend.Tool import Tool
import json


class SessionTool(object):
    hosts = Config('config').data['hosts'][Config('config').data['run']]

    def __init__(self):
        pass

    def get_user_session(self, mobile):
        """
        苗叔-短信验证登录
        :param mobile:
        :return:
        """
        data = {"mobile": mobile,
                "verifyCode": 8888,
                "deviceType": "ANDROID",
                "deviceId": "zhangpengfei",
                "accountType": "CUSTOMER",
                "appId": "MS_APP"
                }
        # data["verifyCode"] = Tool.get_short_massage_code(mobile)
        session = Request().post(url=self.hosts['MS_PASSPORT'] + "/mobile/sso/sms-login", data=data)
        return session

    def get_employee_session(self, account, password):
        """
        chenxiujuan:运营/后台-账号密码登录
        :param account: 账号
        :param password:密码
        :return:
        """
        data = {"appId": "MS_SYS",
                "deviceType": "WEB",
                "account": account,
                "password": password,
                "deviceId": "zhangpengfei"}
        session = Request().post(url=self.hosts['MS_PASSPORT'] + "/admin/service/account-login", data=data)
        return session

    def admin_service_logout(self, token):
        """
        chenxiujuan:运营/后台-退出登录
        :param token: token
        :return:
        """
        data = {"appId": "MS_SYS",
                "deviceType": "WEB",
                "token": token,
                "deviceId": "chenxiujuan"}
        session = Request().post(url=self.hosts['MS_PASSPORT'] + "/admin/service/logout", data=data)
        return session


class UserSession(object):
    def __init__(self, mobile):
        session = SessionTool().get_user_session(mobile)
        session_json = json.loads(session)
        self.token = str(session_json["content"]["token"])
        self.deviceId = str(session_json["content"]["deviceId"])
        self.encrypted_password = str(session_json["content"]["encryptedPwd"])


class EmployeeSession(object):
    def __init__(self, account, password):
        session = SessionTool().get_employee_session(account, password)
        session_json = json.loads(session)
        self.token = str(session_json["content"]["token"])
        self.deviceId = str(session_json["content"]["deviceId"])
        self.password = password


if __name__ == '__main__':
    st = SessionTool()
    # 运营后台账号密码登录
    # st.get_employee_session('18328433208', '123456')
    # 运营后台退出登录
    st.admin_service_logout("eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJ6aGFuZ3BlbmcgZmVpIiwiaXAiOiIxOTIuMTY4LjYyLjE5MCIsImlzcyI6IlpZUF9TU08iLCJ1c2VyIjoie1wiYXBwSWRcIjpcIjEwXCIsXCJkZXZpY2VUeXBlXCI6XCJXRUJcIixcImlkXCI6XCIxMTkxXCIsXCJtb2JpbGVcIjpcIjE4MzI4NDMzMjA4XCIsXCJwYXNzd29yZFwiOlwiMzA1MTVkNGYyOTNlOWY3MzMxYjY4YmZmZGYyOTk1Mjc5MWNmZWVjNFwiLFwicmVhbE5hbWVcIjpcIue9l-aWueWbvVwifSIsImlhdCI6MTU0NTEwNDY5MX0.I5wQhLaL6JMpk_4FIVm-7HWCeCZE954OnGrCvPLRtnZcNU2N93HbmWF1Wd-1jatp30Rr0WYqa1v9-ecJqQzb-w")
    # user = EmployeeSession('18328433208', '123456')
    # print(user.token, user.deviceId)
