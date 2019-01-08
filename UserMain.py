#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
__author__ = ""
__date__ = ""
"""
from actions.UserAction import userAction
from backend.User import User
import unittest
from utils.Log import Log
from utils.Util import DataBaseOperate
import time
from faker import Faker
import random


class MessageMain(unittest.TestCase):
    """
    接口地址：http://dev.ms.user.sjnc.com/swagger-ui.html
    """
    messageTest = userAction()
    faker_zh = Faker(locale='zh_CN')
    # faker_en = Faker(locale='en_GB')
    log = Log('MessageMain').logger
    log.info("开始执行用户信息中心接口测试")
    invite_mobile = faker_zh.phone_number()

    def test001(self):
        """
        陈秀娟:发送注册验证码
        接口路径:POST /mobile/user/register-verify-code
        :return:
        """
        self.log.info('发送注册验证码')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_user_register_verify_code('19982917912')

    def test002(self):
        """
        陈秀娟:验证当前用户手机
        接口路径:POST /mobile/user/validate-mobile
        :return:
        """
        self.log.info('验证当前用户手机号')
        # user = User('18382373185')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_user_validate_mobile('7230')

    def test003(self):
        """
        陈秀娟:上传用户头像
        接口路径:POST /mobile/user/upload-headImg
        :return:
        """
        self.log.info('上传用户头像')
        # ser = User('13828898130')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_user_upload_headImg('1.jpg')

    def test004(self):
        """
        陈秀娟:修改用户昵称
        接口路径:POST /mobile/user/update-nickname
        :return:
        """
        self.log.info('修改用户昵称')
        # ser = User('13828898130')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_user_update_nickname('哈哈')

    def test005(self):
        """
        陈秀娟:获取当前登录用户基础信息
        接口路径:POST /mobile/user/get-basic-info
        :return:
        """
        self.log.info('获取当前登录用户基础信息')
        # ser = User('13828898130')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_user_get_basic_info()

    def test006(self):
        """
        陈秀娟:修改用户昵称和头像
        接口路径:POST /mobile/user/modify
        :return:
        """
        self.log.info('修改用户昵称和头像')
        self.messageTest.set_user('19982917912')
        headImg = self.messageTest._mobile_user_upload_headImg('1.jpg')
        Img = headImg['content']
        self.messageTest._mobile_user_modify(Img, '柳叶')

    def test007(self):
        """
        陈秀娟:发送变更验证码
        接口路径:POST /mobile/user/change-verify-code
        :return:
        """
        self.log.info('发送变更验证码')
        # user = User('19982917912')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_user_change_verify_code('19982917912', 'VALIDATE_CURR')

    def test008(self):
        """
        陈秀娟:修改用户手机号
        接口路径:POST /mobile/user/update-mobile
        :return:
        """
        self.log.info('修改用户手机号')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_user_update_mobile('19982917912', '5135')

    def test009(self):
        """
        陈秀娟:获取推送别名
        接口路径:POST /mobile/user/get-push-alias
        :return:
        """
        self.log.info('获取推送别名')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_user_get_push_alias()

    # def test009(self):
    #     """
    #     陈秀娟:变更或绑定支付账号
    #     接口路径:POST /mobile/user-third/change-payaccount
    #     :return:
    #     """
    #     self.log.info('变更或绑定支付账号')
    #     self.messageTest.set_user('19982917912')
    #     self.messageTest._mobile_user_third_change_payaccount('4529')




