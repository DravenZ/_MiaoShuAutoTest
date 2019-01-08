#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
__author__ = "yong.guo"
__date__ = "20181218"
"""
import unittest
from actions.ProductAction import productAction
from backend.User import User
from backend.Employee import Employee
from utils.Log import Log
from faker import Faker
from utils.Util import DataBaseOperate
import time
import random

class ProductMain(unittest.TestCase):
    """
    接口地址：http://dev.ms.product.sjnc.com/swagger-ui.html
    """
    log = Log('ProductMain').logger
    log.info("开始执行商品类接口测试")
    faker_zh = Faker(locale='zh_CN')

    def __set_user(self, user, passwd="8888", employee=False):
        if employee is False:
            self.user_info = User(user)
            self.product_test = productAction(self.user_info)
        else:
            self.employee_info = Employee(user, passwd)
            self.product_test = productAction(self.employee_info)

    def test0001(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-新增分类.正向流程-郭勇
        接口路径:POST /admin/category/add
        :return:
        """
        # 随机生成商品名称
        # product_name = faker_zh.na
        # 随机生成
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-新增分类接口正向测试，接口路径/admin/category/add")
        category_name = self.faker_zh.word()
        self.product_test._admin_category_add(1, category_name, 20, int(time.time()), None, None)

    def test0002(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-删除分类.正向流程-郭勇
        接口路径:POST /admin/category/del
        :return:
        """
        self.__set_user(login_user_mobile, passwd, True)
        # 测试前，添加一个分类
        self.test0001()
        db_get_last_category_id = DataBaseOperate().operate("39.104.28.40", "ms-product",
                                                               "SELECT id FROM t_category WHERE `status` = 20 "
                                                               "AND is_delete = 0 ORDER BY id DESC LIMIT 1")
        self.log.info("开始执行运营后台端-删除分类接口正向测试，接口路径/admin/category/del")
        self.product_test._admin_category_del(1, db_get_last_category_id[0]["id"])

    def test0003(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-分类详情.正向流程-郭勇
        接口路径:POST /admin/category/detail
        :return:
        """
        # 随机获取一个一季分类信息
        db_get_category = DataBaseOperate().operate("39.104.28.40", "ms-product",
                                                            "SELECT id,parent FROM t_category "
                                                            "WHERE `status` = 10 AND is_delete = 0 LIMIT 50")
        random_category = random.choice(db_get_category)
        if random_category["parent"] != 0:
            category_type = 2
        else:
            category_type = 1

        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-分类详情接口正向测试，接口路径/admin/category/detail")
        self.log.info("查看%s级分类%s详情" % (category_type, random_category["id"]))
        self.product_test._admin_category_detail(category_type, random_category["id"])

    def test0004(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-编辑分类.正向流程-郭勇
        接口路径:POST /admin/category/edit
        :return:
        """
        # 随机获取一个一季分类信息
        category_name = self.faker_zh.word()
        category_status = random.choice([10, 20])
        db_get_category = DataBaseOperate().operate("39.104.28.40", "ms-product",
                                                    "SELECT id,parent FROM t_category "
                                                    "WHERE `status` = 10 AND is_delete = 0 LIMIT 50")
        random_category = random.choice(db_get_category)
        if random_category["parent"] != 0:
            current_category_type = 2
        else:
            current_category_type = 1

        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-编辑分类接口正向测试，接口路径/admin/category/edit")
        self.log.info("将id %s原有分类，名称修改为%s，状态修改为%s" % (random_category["id"], category_name, category_status))
        self.product_test._admin_category_edit(current_category_type, random_category["id"], category_name, category_status, int(time.time()), None, None)

    def test0005(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-分类列表.正向流程-郭勇
        接口路径:POST /admin/category/list
        :return:
        """
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-分类列表接口正向测试，接口路径/admin/category/list")
        self.product_test._admin_category_list(random.choice[1, 2], None, None, None, 1, 30)

    def test0006(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-分类上下架.正向流程-郭勇
        接口路径:POST /admin/category/update-status
        :return:
        """
        db_get_category = DataBaseOperate().operate("39.104.28.40", "ms-product",
                                                    "SELECT id,parent,orders FROM t_category "
                                                    "WHERE is_delete = 0 LIMIT 50")
        random_category = random.choice(db_get_category)
        if random_category["parent"] != 0:
            category_type = 2
        else:
            category_type = 1
        set_category_status = random.choice([10, 20])
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-分类上下架接口正向测试，接口路径/admin/category/update-status")
        self.log.info("将%s状态设置为%s" % (random_category["id"], set_category_status))
        self.product_test._admin_category_update_status(category_type, random_category["id"], set_category_status)

    def test0007(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-平台商品库存数量统计.正向流程-郭勇
        接口路径:POST /admin/report/all-store-stats
        :return:
        """
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-平台商品库存数量统计接口正向测试，接口路径/admin/report/all-store-stats")
        self.product_test._admin_report_all_store_stats()

    def test0008(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-二级分类销量top统计.正向流程-郭勇
        接口路径:POST /admin/report/category-sales-stats
        :return:
        """
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-二级分类销量top统计接口正向测试，接口路径/admin/report/category-sales-stats")
        self.product_test._admin_report_category_sales_stats(None, None, random.choice([20, 30]), None)

    def test0009(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-商品库存在一级分类分布图.正向流程-郭勇
        接口路径:POST /admin/report/category-store-stats
        :return:
        """
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-商品库存接口正向测试，接口路径/admin/report/category-store-stats")
        self.product_test._admin_report_category_store_stats()

    def test0010(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-店铺商品销量top统计.正向流程-郭勇
        接口路径:POST /admin/report/product-sales-stats
        :return:
        """
        db_get_shop = DataBaseOperate().operate("39.104.28.40", "ms-shop",
                                                    "SELECT id FROM t_shop "
                                                    "WHERE is_delete = 0 LIMIT 50")
        random_shop = random.choice(db_get_shop)
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-店铺商品销量top统计接口正向测试，接口路径/admin/report/product-sales-stats")
        self.product_test._admin_report_product_sales_stats(None, None, random_shop["id"], None)

    def test0011(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-新增商品单位.正向流程-郭勇
        接口路径:POST /admin/store-unit/add
        :return:
        """
        # 生成随机单位
        store_unit = random.choice(["个", "位", "条", "只", "匹", "头", "条", "峰", "个", "只", "颗", "根", "张", "片", "条", "棵", "株", "朵", "片", "条", "颗", "粒", "顿", "道", "片", "块", "根", "个", "粒", "张", "把", "条", "张", "台", "根", "个", "块", "盘"])
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-新增商品单位接口正向测试，接口路径/admin/store-unit/add")
        self.log.info("添加库存单位:%s" % store_unit)
        self.product_test._admin_store_unit_add(store_unit)

    def test0012(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-删除商品单位.正向流程-郭勇
        接口路径:POST /admin/store-unit/del
        :return:
        """
        db_get_store_unit = DataBaseOperate().operate("39.104.28.40", "ms-product",
                                                "SELECT id FROM t_store_unit "
                                                "WHERE is_delete = 0 ORDER BY id DESC LIMIT 5")
        random_store_unit = random.choice(db_get_store_unit)
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-新增分类接口正向测试，接口路径/admin/category/add")
        self.log.info("删除植物单位%s" % random_store_unit["id"])
        self.product_test._admin_store_unit_del(random_store_unit["id"])

    def test0013(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-商品单位详情.正向流程-郭勇
        接口路径:POST /admin/store-unit/detail
        :return:
        """
        db_get_store_unit = DataBaseOperate().operate("39.104.28.40", "ms-product",
                                                      "SELECT id FROM t_store_unit "
                                                      "WHERE is_delete = 0 ORDER BY id DESC LIMIT 10")
        random_store_unit = random.choice(db_get_store_unit)
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-商品单位详情接口正向测试，接口路径/admin/store-unit/detail")
        self.log.info("植物单位%s详情" % random_store_unit["id"])
        self.product_test._admin_store_unit_detail(random_store_unit["id"])

    def test0014(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-修改商品单位.正向流程-郭勇
        接口路径:POST /admin/store-unit/edit
        :return:
        """
        db_get_store_unit = DataBaseOperate().operate("39.104.28.40", "ms-product",
                                                      "SELECT id FROM t_store_unit "
                                                      "WHERE is_delete = 0 ORDER BY id DESC LIMIT 10")
        random_store_unit = random.choice(db_get_store_unit)
        store_unit = random.choice(["个", "位", "条", "只", "匹", "头", "条", "峰", "个", "只", "颗", "根", "张", "片", "条", "棵", "株", "朵", "片", "条", "颗", "粒", "顿", "道", "片", "块", "根", "个", "粒", "张", "把", "条", "张", "台", "根", "个", "块", "盘"])
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行运营后台端-修改商品单位接口正向测试，接口路径/admin/store-unit/edit")
        self.log.info("修改%s的单位为：%s" % (random_store_unit["id"], store_unit))
        self.product_test._admin_store_unit_edit(random_store_unit["id"], store_unit)

    def test0015(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        运营后台端-分页获取商品单位.正向流程-郭勇
        接口路径:POST /admin/store-unit/list
        :return:
        """
        self.__set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行 运营后台端-分页获取商品单位接口正向测试，接口路径/admin/store-unit/list")
        self.product_test._admin_store_unit_list(1, 100)
