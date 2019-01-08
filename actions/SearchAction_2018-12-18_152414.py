# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class searchAction(object):

    def __init__(self, search):
        self.log = Log('search')
        self.request = Request()
        self.search = search

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

    def _api_test_update_shop_month_sales(self):
        data = {'_tk_': self.search.token, '_deviceId_': self.search.device_id}
        response = self.request.post(url='http://dev.ms.search.sjnc.com/api/test/update-shop-month-sales', data=data)
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
        data = {'_tk_': self.search.token, '_deviceId_': self.search.device_id, 'searchContent': searchContent, 'shopTag': shopTag, 'secondCategoryId': secondCategoryId, 'upKeepServer': upKeepServer, 'plantServer': plantServer, 'lat': lat, 'lng': lng, 'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.search.sjnc.com/mobile/search/search-nearby-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_search_search_nearby_supplier_shop(self, searchContent, shopTag, secondCategoryId, upKeepServer, plantServer, lat, lng, distance, pn, ps):
        data = {'_tk_': self.search.token, '_deviceId_': self.search.device_id, 'searchContent': searchContent, 'shopTag': shopTag, 'secondCategoryId': secondCategoryId, 'upKeepServer': upKeepServer, 'plantServer': plantServer, 'lat': lat, 'lng': lng, 'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.search.sjnc.com/mobile/search/search-nearby-supplier-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_search_search_shop_product(self, searchContent, shopTag, secondCategoryId, upKeepServer, plantServer, lat, lng, distance, pn, ps):
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
        data = {'_tk_': self.search.token, '_deviceId_': self.search.device_id, 'searchContent': searchContent, 'shopTag': shopTag, 'secondCategoryId': secondCategoryId, 'upKeepServer': upKeepServer, 'plantServer': plantServer, 'lat': lat, 'lng': lng, 'distance': distance, 'pn': pn, 'ps': ps}
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
