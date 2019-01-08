# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class cartAction(object):

    def __init__(self, cart):
        self.log = Log('cart')
        self.request = Request()
        self.cart = cart

    def _api_freight_calc(self, pcodes, amounts, addressId, buyerId, userType):
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id, 'pcodes': pcodes, 'amounts': amounts, 'addressId': addressId, 'buyerId': buyerId, 'userType': userType}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/api/freight/calc', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_add(self, pcode, amount):
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id, 'pcode': pcode, 'amount': amount}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_balance(self, cartIds, addressId):
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id, 'cartIds': cartIds, 'addressId': addressId}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/balance', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_batch_delete(self, cartIds):
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id, 'cartIds': cartIds}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/batch-delete', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_delete(self, cartId):
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id, 'cartId': cartId}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/delete', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_editAmount(self, cartId, amount):
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id, 'cartId': cartId, 'amount': amount}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/editAmount', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_list(self, type):
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id, 'type': type}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_purchase(self, pcode, amount, addressId):
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id, 'pcode': pcode, 'amount': amount, 'addressId': addressId}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/purchase', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
