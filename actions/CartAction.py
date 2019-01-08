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
        data = {'_tk_': self.cart.token,
                '_deviceId_': self.cart.device_id,
                'pcodes': pcodes,
                'amounts': amounts,
                'addressId': addressId,
                'buyerId': buyerId,
                'userType': userType}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/api/freight/calc', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_add(self, pcode, amount):
        """
        买家端加入购物车
        :param pcode:
        :param amount:
        :return:
        """
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
        """
        买家端购物车结算
        :param cartIds:
        :param addressId:
        :return:
        """
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
        """
        买家批量删除购物车商品
        :param cartIds:
        :return:
        """
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
        """
        删除购物车商品
        :param cartId:
        :return:
        """
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
        """
        买家编辑库存数量
        :param cartId:
        :param amount:
        :return:
        """
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id, 'cartId': cartId, 'amount': amount}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/editAmount', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_list(self):
        """
        买家获取购物车列表
        :return:
        """
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_purchase(self, pcode, amount, addressId):
        """
        买家直接购买
        :param pcode:
        :param amount:
        :param addressId:
        :return:
        """
        data = {'_tk_': self.cart.token, '_deviceId_': self.cart.device_id, 'pcode': pcode, 'amount': amount, 'addressId': addressId}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/purchase', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
