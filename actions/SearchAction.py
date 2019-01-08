# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
from backend.User import User
 
class searchAction(object):

    def __init__(self):
        self.log = Log('search').logger
        self.request = Request()
        # self.search = search

    def set_user(self, user):
        self.search=User(user)
        return self.search

    def _api_search_update_shop_month_sales(self):
        data = {'_tk_': self.search.token, '_deviceId_': self.search.device_id}
        response = self.request.post(url='http://dev.ms.search.sjnc.com/api/search/update-shop-month-sales', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_search_add_batch(self, indexName, lastId):
        data = {'_tk_': self.search.token, '_deviceId_': self.search.device_id, 'indexName': indexName, 'lastId': lastId}
        response = self.request.post(url='http://dev.ms.search.sjnc.com/mobile/search/add-batch', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_search_search_nearby_shop(self, searchContent, shopTag, secondCategoryId, upKeepServer, plantServer, lat, lng, distance, pn, ps):
        """
        苗木购买,搜索附近苗叔
        :param searchContent:
        :param shopTag:
        :param secondCategoryId:
        :param upKeepServer:
        :param plantServer:
        :param lat:
        :param lng:
        :param distance:
        :param pn:
        :param ps:
        :return:
        """
        data = {'_tk_': self.search.token, '_deviceId_': self.search.device_id, 'searchContent': searchContent, 'shopTag': shopTag, 'secondCategoryId': secondCategoryId, 'upKeepServer': upKeepServer, 'plantServer': plantServer, 'lat': lat, 'lng': lng, 'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.search.sjnc.com/mobile/search/search-nearby-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_search_search_nearby_supplier_shop(self, lat, lng, distance, pn, ps):
        data = {'_tk_': self.search.token, '_deviceId_': self.search.device_id,  'lat': lat, 'lng': lng, 'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.search.sjnc.com/mobile/search/search-nearby-supplier-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_search_search_shop_product(self, searchContent, shopTag, secondCategoryId, upKeepServer, plantServer, lat, lng, distance, pn, ps):
        """
        买家端搜索店铺商品和商品所属店铺
        :param searchContent:
        :param shopTag:
        :param secondCategoryId:
        :param upKeepServer:
        :param plantServer:
        :param lat:
        :param lng:
        :param distance:
        :param pn:
        :param ps:
        :return:
        """
        data = {'_tk_': self.search.token, '_deviceId_': self.search.device_id, 'searchContent': searchContent, 'shopTag': shopTag, 'secondCategoryId': secondCategoryId, 'upKeepServer': upKeepServer, 'plantServer': plantServer, 'lat': lat, 'lng': lng, 'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.search.sjnc.com/mobile/search/search-shop-product', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_search_search_supplier_shop_product(self, searchContent, shopTag, secondCategoryId, upKeepServer, plantServer, lat, lng, distance, pn, ps):
        data = {'searchContent': searchContent, 'shopTag': shopTag, 'secondCategoryId': secondCategoryId, 'upKeepServer': upKeepServer, 'plantServer': plantServer, 'lat': lat, 'lng': lng, 'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.search.sjnc.com/mobile/search/search-supplier-shop-product', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_search_search_supplier_shop_product_login(self, searchContent, shopTag, secondCategoryId, upKeepServer, plantServer, lat, lng, distance, pn, ps):
        data = {'_tk_': self.search.token, '_deviceId_': self.search.device_id, 'searchContent': searchContent, 'shopTag': shopTag, 'secondCategoryId': secondCategoryId, 'upKeepServer': upKeepServer, 'plantServer': plantServer, 'lat': lat, 'lng': lng, 'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.search.sjnc.com/mobile/search/search-supplier-shop-product-login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
