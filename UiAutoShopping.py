#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018-12-15'
"""


from utils.Util import AndroidTool
from utils.Util import Mail
from utils.Log import Log
from unittest import TestCase


class UiAutoShopping(TestCase):

    L = Log("UiAutoShopping")
    at = AndroidTool()

    def test0001(self):
        try:
            apk_path = '/Users/hengxin/Downloads/苗叔-20181130\(v1.0.24\).apk'
            self.at.launch_app_by_apk(apk_path)
            self.at.login_miaoshu("18602832572", "888888")
            self.at.enter_shop("自动化刷单勿删")
            self.at.pay_product()
            self.at.tear_down_miaoshu()
            Mail().send_html_email()
            self.L.logger.info("测试完成, 邮件发送成功")
        except Exception as e:
            self.at.get_screen_shot()
            self.L.logger.debug("错误信息: %s" % e)
            self.at.tear_down_miaoshu()
