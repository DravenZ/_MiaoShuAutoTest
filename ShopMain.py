#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
__author__ = ""
__date__ = ""
"""
from actions.ShopAction import shopAction
import unittest
from utils.Log import Log
from faker import Faker

class ShopMain(unittest.TestCase):
    """
    接口地址: http://192.168.62.253:31009/swagger-ui.html#/
    """
    shopTest = shopAction()
    faker_zh = Faker(locals='zh_CN')
    log = Log('ShopMain').logger
    log.info("开始执行店铺类接口测试")

    def test0001(self):
        """
        店铺数据-关雅馨
        接口路径:POST POST /admin/report/shop-business-report
        :return:
        """
        self.log.info("开始执行获取店铺数据测试，接口路径/admin/report/shop-business-report")
        self.shopTest.set_user("15283855883")
        self.shopTest._admin_report_shop_business_report("2018-12-15", "2018-12-20")

    def test0002(self):
        """
        店铺统计数据-关雅馨
        接口路径:POST /admin/report/shop-count
        :return:
        """
        self.log.info("开始执行获取店铺统计数据测试，接口路径/admin/report/shop-count")
        self.shopTest.set_user("18380581411")
        self.shopTest._admin_report_shop_count()

    def test0003(self):
        """
        提交修改店铺联系电话验证码-关雅馨
        接口路径: POST /mobile/shop/update-mobile
        :return:
        """
        self.log.info("开始执行提交修改店铺联系电话验证码测试，接口路径/mobile/shop/update-mobile")
        self.shopTest.set_user("15283855883")
        self.log.info("发送修改店铺联系电话验证码")
        self.shopTest._mobile_shop_send_verify_code("15200000000")
        self.log.info("提交修改店铺联系电话验证码测试")
        self.shopTest._mobile_shop_update_mobile("15200000000", 153)

    def test0004(self):
        """
        上传店铺头像-关雅馨
        接口路径：POST /mobile/shop/upload-avatar
        :return:
        """
        self.log.info("开始执行上传店铺头像测试，接口路径/mobile/shop/upload-avatar")
        self.shopTest.set_user("15283855883")
        self.shopTest._mobile_shop_upload_avatar("1.jpg")

    def test0005(self):
        """
        店铺经营数据报表-关雅馨
        接口路径：POST /web/report/shop-seles-report
        :return:
        """
        self.log.info("开始执行店铺经营数据报表测试，接口路径/web/report/shop-seles-report")
        self.shopTest.set_user("15283855883")
        self.shopTest._web_report_shop_seles_report(153, "2018-12-19", "2018-12-20")


