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
    log.info("开始执行服务咨询接口测试")
    invite_mobile = faker_zh.phone_number()

    def test001(self):
        """
        陈秀娟:获取自身IM账号
        接口路径:POST /mobile/service/get-accid
        :return:
        """
        self.log.info('获取自身的IM账号')
        # user = User('18382373185')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_service_get_accid()

    def test002(self):
        """
        陈秀娟:获取商家的IM账号
        接口路径:POST /mobile/service/get-seller-accid
        :return:
        """
        self.log.info('获取商家的IM账号')
        self.messageTest.set_user('18582549167')
        self.messageTest._mobile_service_get_seller_accid(144)

    def test003(self):
        """
        陈秀娟:获取在线客服的IM账号
        接口路径:POST /mobile/service/get-service-accid
        :return:
        """
        self.log.info('获取在线客服的IM账号')
        # ser = User('13828898130')
        self.messageTest.set_user('18380581402')
        self.messageTest._mobile_service_get_service_accid()

    def test004(self):
        """
        陈秀娟:获取未读消息量
        接口路径:POST /mobile/message/unread
        :return:
        """
        self.log.info('获取未读消息量')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_message_unread()

    def test005(self):
        """
        陈秀娟:更新未读为已读
        接口路径:POST /mobile/message/read
        :return:
        """
        self.log.info('更新未读为已读')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_message_read()

    def test006(self):
        """
        陈秀娟:查询消息列表
        接口路径:POST /mobile/message/list
        :return:
        """
        self.log.info('查询消息列表')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_message_list()

    def test007(self):
        """
        陈秀娟:删除消息
        接口路径:POST /mobile/message/del
        :return:
        """
        self.log.info('删除消息')
        self.messageTest.set_user('19982917912')
        self.messageTest._mobile_message_del()

