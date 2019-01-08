#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
__author__ = ""
__date__ = ""
"""
from actions.SearchAction import searchAction
import unittest
from utils.Log import Log
from faker import Faker


class SearchMain(unittest.TestCase):
    """
    接口地址: http://dev.ms.search.sjnc.com/swagger-ui.html
    """
    searchTest = searchAction()
    faker_zh=Faker(locals='zh_CN')
    log = Log('SearchMain').logger
    log.info("开始执行搜索类接口测试")

    def test0001(self):
        """
        绿植,果树,蔬菜,枸杞,花椒页面搜索附近基地-关雅馨
        接口路径:POST /mobile/search/search-nearby-supplier-shop
        :return:
        """
        self.log.info("开始执行绿植,果树,蔬菜,枸杞,花椒页面搜索附近基地测试，接口路径/mobile/search/search-nearby-supplier-shop")
        self.searchTest.set_user("15283855883")
        self.searchTest._mobile_search_search_nearby_supplier_shop(30.538003, 104.070098, 30000, 1, 20)

    def test0002(self):
        """
        (未登录的情况)基地页面搜索商品和商品所属店铺-关雅馨
         接口路径:POST /mobile/search/search-supplier-shop-product
        :return:
        """
        self.log.info("(未登录的情况)基地页面搜索商品和商品所属店铺测试，接口路径/mobile/search/search-supplier-shop-product")
        # self.searchTest.set_user("15282644233")
        self.searchTest._mobile_search_search_supplier_shop_product("苹果", None, None, None, None, 30.5670647764,
                                                                    104.0665340424, 1500, 1, 20)

    def test0003(self):
        """
        (已登录的情况)基地页面搜索商品和商品所属店铺-关雅馨
         接口路径:POST /mobile/search/search-supplier-shop-product-login
        :return:
        """
        self.log.info("(已登录的情况)基地页面搜索商品和商品所属店铺测试，接口路径/mobile/search/search-supplier-shop-product-login")
        self.searchTest.set_user("15283855883")
        self.searchTest._mobile_search_search_supplier_shop_product_login("苹果", None, None, None, None,
                                                                          30.5670647764, 104.0665340424, 1500, 1, 20)

    def test0004(self):
        """
        苗木购买,上门养护,上门种植3个页面,搜索附近苗叔-关雅馨
        接口路径:POST /mobile/search/search-nearby-shop
        :return:
        """
        self.log.info("苗木购买,上门养护,上门种植3个页面,搜索附近苗叔测试，接口路径/mobile/search/search-nearby-shop")
        self.searchTest.set_user("18380581402")
        self.searchTest._mobile_search_search_nearby_shop(None, None, None, None, None,
                                                          30.5670647764, 104.0665340424, 30000, 1, 20)

    def test0005(self):
        """
        苗叔页面搜索商品和商品所属店铺-关雅馨
        接口路径:POST /mobile/search/search-shop-product
        :return:
        """
        self.log.info("苗叔页面搜索商品和商品所属店铺测试，接口路径/mobile/search/search-shop-product")
        self.searchTest.set_user("15283855883")
        self.searchTest._mobile_search_search_shop_product("苹果", None, None, None, None,
                                                           30.5670647764, 104.0665340424, 30000, 1, 20)
