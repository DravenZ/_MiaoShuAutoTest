#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Pengfei'
__date__ = '2018/11/5'
"""


from utils.Util import Request
from utils.Log import Log
from backend.Tool import Tool
from backend.Session import UserSession
from utils.Config import Config
import json


class User(object):
    hosts = Config('config').data['hosts'][Config('config').data['run']]

    def __init__(self, mobile):
        self.log = Log('User')
        self.tool = Tool()
        self.request = Request()
        # self.user_info = self.tool.miaoshu_query_user_info_by_mobile(mobile, 1)
        # if self.user_info != ():
        #     self.user_info = self.user_info[0]
        #     if self.user_info['channel_status'] is not None:
        #         self.tool.ms_delete_user_by_mobile(mobile)
        us = UserSession(mobile)
        self.encryptedPwd = us.encrypted_password
        self.token, self.device_id = us.token, us.deviceId
        self.user_info = self.tool.miaoshu_query_user_info_by_mobile(mobile, 1)
        if self.user_info != ():
            self.user_info = self.user_info[0]

            self.user_id = self.user_info["id"]
            self.real_name = self.user_info["real_name"]
            self.nickname = self.user_info["nickname"]
            self.sex = self.user_info["sex"]
            self.mobile = self.user_info["mobile"]
            self.email = self.user_info["email"]
            self.account_status = self.user_info["account_status"]
            self.account_type = self.user_info["account_type"]
            self.head_img = self.user_info["head_img"]
            self.register_time = self.user_info["create_time"]
            self.edit_time = self.user_info["edit_time"]
            self.channel_shop_id = None
            self.supplier_shop_id = None

    def automatic_login(self):
        """
        自动登录
        :return:
        """
        data = {'token': self.token,
                'deviceId': self.device_id,
                'encryptedPwd': self.encryptedPwd}
        response = Request().post(url=self.hosts['MS_PASSPORT'] + "/mobile/sso/automatic-login", data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            self.token = json_response['content']['token']
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def user_logout(self):
        """
        用户退出登录
        :return:
        """
        data = {"token": self.token}
        response = Request().post(url=self.hosts['MS_PASSPORT'] + "/mobile/sso/logout", data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def check_token(self):
        """
        验证用户token
        :return:
        """
        data = {'token': self.token,
                'deviceId': self.device_id}
        response = Request().post(url=self.hosts['MS_PASSPORT'] + "/api/sso/check-token", data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def clear_token(self, app_id='MS_APP'):
        """
        清除用户token
        :return:
        """
        data = {'userId': self.user_id,
                'appId': app_id}
        response = Request().post(url=self.hosts['MS_PASSPORT'] + "/api/sso/clear-token", data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_update_nickname(self, nickname):
        """
        张鹏飞: 新用户登录后,添加昵称调用
        :param nickname: 昵称
        :return:
        """
        data = {'_tk_': self.token, '_deviceId_': self.device_id, 'nickname': nickname}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/user/update-nickname', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")


if __name__ == '__main__':
    user = User("13572720546")
    # 自动登录
    # aulogin = user.automatic_login()
    # 退出登录
    # user.user_logout()
    # user.verify_code_get(18602832572, "MS_APP")
    # mcode = user.tool.get_short_massage_code(18602832572)
    # user.check_token()
    # user.clear_token()
    user._mobile_user_update_nickname("虫虫飞")
