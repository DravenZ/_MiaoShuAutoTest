#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/11/5'
"""

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
import datetime


class PurchaserAction(object):
    hosts = Config('config').data['hosts'][Config('config').data['run']]

    def __init__(self, purchaser):
        self.log = Log('PurchaserAction')
        self.purchaser = purchaser
        self.request = Request()
        self.tool = Tool()
        self.ps = 10

    def get_basic_info(self):
        """
        chenxiujuan:获取当前用户的基础信息
        :return:
        """
        bind_data = {"_tk_": self.purchaser.token,
                     "_deviceId_": self.purchaser.device_id}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/user/get-basic-info',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
            # query_user_info = self.tool.miaoshu_query_user_info_by_mobile(self.purchaser.mobile, 1)
            # if query_user_info is not None:
            #     query_user_info = query_user_info[0]
            # assert query_user_info['account_status'] == json_response['content']['accountStatus']
            # assert query_user_info['account_type'] == json_response['content']['accountType']
            # assert query_user_info['id'] == json_response['content']['id']
            # assert query_user_info['last_role'] == json_response['content']['lastRole']
            # assert query_user_info['mobile'] == json_response['content']['mobile']
            # assert query_user_info['nickname'] == json_response['content']['nickname']
            # assert query_user_info['password'] == json_response['content']['password']
            # assert query_user_info['real_name'] == json_response['content']['realName']
            # assert query_user_info['self_set'] == json_response['content']['selfSet']
            # assert query_user_info['real_name'] == json_response['content']['realName']
            # if json_response['content']['supplierExamineStatus'] == 1:
            #     assert query_user_info['supplier_status'] is None
            # if json_response['content']['channelExamineStatus'] == 1:
            #     assert query_user_info['channel_status'] is None
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def update_nickname(self, nick_name):
        """
        chenxiujuan:修改用户的昵称
        :param nick_name: 昵称
        :return:
        """
        bind_data = {"_tk_": self.purchaser.token,
                     "_deviceId_": self.purchaser.device_id,
                     "userId": self.purchaser.user_id,
                     "nickName": nick_name}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/user/update-nickname',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_user_info = self.tool.miaoshu_query_user_info_by_mobile(self.purchaser.mobile, 1)
            if query_user_info is not None:
                query_user_info = query_user_info[0]
            assert query_user_info['nickname'] == bind_data['nickName']
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def upload_img(self):
        response = Request().post_file(url=self.hosts['MS_USER'] + "/mobile/user/upload-headImg", data_dict={},
                                       file_path="./picture/1.jpg", file_key="headImgFile")
        json_response = json.loads(response)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response['content']

    def update_head_img(self):
        """
        修改用户头像
        :return:
        """
        bind_data = {"_tk_": self.purchaser.token,
                     "_deviceId_": self.purchaser.device_id,
                     "userId": self.purchaser.user_id,
                     "headImg": self.upload_img()}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/user/update-headImg',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_user_info = self.tool.miaoshu_query_user_info_by_mobile(self.purchaser.mobile, 1)
            if query_user_info is not None:
                query_user_info = query_user_info[0]
            assert query_user_info['head_img'] == bind_data['headImg']
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def product_search(self, key_word, lat=30.5445, lng=104.075):
        """
        根据关键字查询店铺列表
        :param key_word: 关键字搜索
        :param lat: 维度
        :param lng: 经度
        :return:
        """
        data = {
            'keyword': key_word,
            'lat': lat, 'lng': lng,
            "distance": '300000',
            "ps": 20,
            "pn": 1
        }
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/product/products',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def get_shop_info_by_id(self, shop_id, lat=30.5445, lng=104.075):
        """
        根据查询店铺信息
        :param shop_id: 店铺ID
        :param lat: 纬度
        :param lng: 经度
        :return:
        """
        data = {
            'id': shop_id,
            'lat': lat, 'lng': lng,
        }
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/get/%s' % str(shop_id),
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def shop_search(self, key_word, lat=30.5445, lng=104.075):
        """
        根据关键字查询店铺列表
        :param key_word: 关键字搜索
        :param lat: 维度
        :param lng: 经度
        :return:
        """
        data = {
            'keyword': key_word,
            'lat': lat, 'lng': lng,
            "ps": 20,
            "pn": 1
        }
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/search',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def get_shop_products_by_shop_id(self, shop_id):
        """
        根据店铺ID查询店铺内所有的商品
        :param shop_id: 店铺ID
        :return: 店铺内所有商品
        """
        data = {'shopId': shop_id}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/mobile/product/shop-products',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def get_product_detail(self, pro_code):
        """
        根据商品p_code查询商品详情
        :param pro_code: 商品编码
        :return: 商品的详情
        """
        data = {'pcode': pro_code}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/mobile/product/detail',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def cart_add(self, pro_code, amount=1):
        """
        添加购物车
        :param pro_code: 商品的pro_code
        :param amount:  商品数量
        :return:
        """
        data = {
            'pcode': pro_code,
            'amount': amount,
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id
        }
        response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/add',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def get_cart_list(self, cart_type=10):
        """
        获取购物车列表
        :param cart_type:
        :return: 返回一个列表{"content":{"productCount":0,"shopItem":[]},"status":"OK"}
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            'type': cart_type
        }
        response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/list',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def cart_del(self, cart_id):
        """
        根据购物车内商品的购物车ID来删除购物车内的商品
        :param cart_id: 购物车内的购物车ID
        :return:
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            'cartId': cart_id
        }
        response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/delete',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def cart_batch_del(self, cart_ids):
        """
        批量删除购物车内的商品
        :param cart_ids: 购物车内的购物车ID,按逗号分隔,eg:1,2,3
        :return:
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            'cartIds': cart_ids
        }
        response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/batch-delete',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def cart_balance(self, cart_ids, address_id=None):
        """
        购物车结算
        :param cart_ids: 购物车内商品的购物车ID集合,用逗号分隔,eg:1,2,3
        :param address_id: 地址ID
        :return:
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            'cartIds': cart_ids,
            'addressId': address_id
        }
        response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/balance',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def cart_edit_amount(self, cart_id, amount):
        """
        编辑购物车内单个商品的数量
        :param cart_id: 购物车内商品的购物车ID
        :param amount: 修改后的数量
        :return:
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            'cartId': cart_id,
            'amount': amount
        }
        response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/editAmount',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def cart_purchase(self, pro_code, amount, address_id):
        """
        从商品详情页中直接购买
        :param pro_code: 商品pro_code
        :param amount: 购买的商品数量
        :param address_id: 地址ID
        :return:{
                  "content": {
                    "deliveryDate": "2018-11-16T02:29:19.846Z",
                    "deliveryDateText": "string", 配送日期
                    "deliveryName": "string",配送名字
                    "deliveryPrice": 0,运费
                    "deliveryType": 0,配送类型
                    "deliveryTypeName": "string",配送类型名字
                    "products": [
                      {
                        "amount": 0,
                        "cartId": 0,
                        "freightTemplateId": 0,运费模板ID
                        "imgs": [
                          "string"
                        ],
                        "name": "string",
                        "pcode": 0,
                        "price": 0,
                        "saleType": 0,
                        "saleTypeName": 0,
                        "shopId": 0,
                        "snapshotId": 0,
                        "status": 0,
                        "statusName": 0
                      }
                    ],
                    "shippingAddressDto": {
                      "address": "string",
                      "contractNumber": "string",
                      "id": 0,
                      "lat": 0,
                      "lng": 0,
                      "receiver": "string"
                    },
                    "shop": {
                      "address": {
                        "address": "string",
                        "area": "string",
                        "city": 0,
                        "lat": 0,
                        "lng": 0,
                        "province": 0,
                        "shopId": 0,
                        "status": 0
                      },
                      "contact": "string",
                      "name": "string",
                      "sellerId": 0,
                      "shopId": 0,
                      "status": 0,
                      "type": 0
                    },
                    "totalPrice": 0
                  },
                  "errorCode": "string",
                  "errorMsg": "string",
                  "status": "string"
                }
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            'pcode': pro_code,
            'amount': amount,
            'addressId': address_id
        }
        response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/purchase',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def submit_order(self, order_data, is_check=0):
        """
        提交订单
        :param order_data: 订单的信息
        :param is_check: 是否check.默认不check
        :return: 返回订单号
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id
        }
        data.update(order_data)
        data['isCheck'] = is_check
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/order/submit-order',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def order_close(self, order_no):
        """
        张鹏飞:关闭订单
        :param order_no: 订单号
        :return:
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            'orderNo': order_no
        }
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/order/close',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def confirm_receive(self, order_no):
        """
        张鹏飞:确认收货
        :param order_no: 订单号
        :return:
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            'orderNo': order_no
        }
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/order/confirm-receive',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def order_detail(self, order_no):
        """
        张鹏飞:订单详情
        :param order_no: 订单号
        :return:
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            'orderNo': order_no
        }
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/order/detail',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            json_response = json_response.get('content')
            query_order_detail = self.tool.ms_query_buyer_shop_order_detail_by_order_no(order_no)[0]
            if query_order_detail.get('applyStatus') is not None:
                assert query_order_detail.get('applyStatus') == json_response.get('applyStatus')
                assert query_order_detail.get('applyStatusDesc') == json_response.get('applyStatusDesc')
            assert query_order_detail.get('buyerId') == json_response.get('buyerId')
            assert query_order_detail.get('buyerHeadImg') == json_response.get('buyerHeadImg')
            assert query_order_detail.get('createTime') == json_response.get('createTime')
            assert query_order_detail.get('freight') == json_response.get('freight')
            assert query_order_detail.get('orderStatus') == json_response.get('orderStatus')
            assert query_order_detail.get('orderStatusDesc') == json_response.get('orderStatusDesc')
            assert query_order_detail.get('priceTotal') == json_response.get('priceTotal')
            if query_order_detail.get('payTime') is not None:
                assert query_order_detail.get('payTime') == json_response.get('payTime')
                assert query_order_detail.get('priceReal') == json_response.get('priceReal')
            assert query_order_detail.get('receiveAddress') == json_response.get('receiveAddress')
            assert query_order_detail.get('receiveLat') == json_response.get('receiveLat')
            assert query_order_detail.get('receiveLng') == json_response.get('receiveLng')
            assert query_order_detail.get('receiveMobile') == json_response.get('receiveMobile')
            assert query_order_detail.get('receiveName') == json_response.get('receiveName')
            if query_order_detail.get('orderStatus') == 40:
                assert query_order_detail.get('receiveTime') == json_response.get('receiveTime')
            assert query_order_detail.get('sendMobile') == json_response.get('sendMobile')
            assert query_order_detail.get('sendName') == json_response.get('sendName')
            assert query_order_detail.get('shopContact') == json_response.get('shopContact')
            assert query_order_detail.get('shopContactMobile') == json_response.get('shopContactMobile')
            assert query_order_detail.get('shopName') == json_response.get('shopName')
            assert query_order_detail.get('tradeNo') == json_response.get('tradeNo')
            assert query_order_detail.get('validDate') == json_response.get('validDate')

        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def order_list(self, order_status):
        """
        张鹏飞:订单列表
        :param order_status: 订单状态:待付款10 待收货20,30 交易成功40
        :return:
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            'order_status': order_status
        }
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/order/list',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def hot_recommend(self):
        """
        热品推荐
        :return:
        """
        data = {}
        response = self.request.post(url=self.hosts['MS_KBMS'] + '/mobile/resource-activity/item/hot-recommend',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def search_category(self, search):
        """
        根据关键字查找二级分类列表
        :param search: 关键字
        :return:
        """
        data = {
            '_tk_': self.purchaser.token,
            '_deviceId_': self.purchaser.device_id,
            "search": search,
            "ps": 20,
            "pn": 1
        }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/mobile/category/page',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def nearby_shop_products(self, search, lat=30.5445, lng=104.075):
        """
        分页查找附近店铺及商品
        :param search: 关键字
        :param lat: 纬度
        :param lng: 经度
        :return:
        """
        data = {
            'search': search,
            'lat': lat,
            'lng': lng,
            "distance": 300000,
            "ps": 20,
            "pn": 1
        }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/mobile/product/nearby-shop-products',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def cashier_index(self, trade_nos):
        """
        收银台
        :param trade_nos:  订单的交易号
        :return:
        """
        data = {
            'tradeNos': trade_nos
            # '_tk_': self.purchaser.token,
            # '_deviceId_': self.purchaser.device_id
        }
        # if Config('config').data['run'] == 'QA':
        data['_tk_'] = self.purchaser.token
        data['_deviceId_'] = self.purchaser.device_id
        response = self.request.post(url=self.hosts['MS_PAY'] + '/mobile/cashier/index',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def weipay_pay(self, trade_nos, channel_id, channel_amount):
        """
        支付接口
        :param trade_nos:  订单的交易号
        :param channel_id: 渠道ID
        :param channel_amount: 订单金额(分)
        :return:
        """
        data = {
            'tradeNos': trade_nos,
            "channelId": channel_id,
            "channelAmount": channel_amount
            # '_tk_': self.purchaser.token,
            # '_deviceId_': self.purchaser.device_id
        }
        # if Config('config').data['run'] == 'QA':
        data['_tk_'] = self.purchaser.token
        data['_deviceId_'] = self.purchaser.device_id
        response = self.request.post(url=self.hosts['MS_PAY'] + '/mobile/weipay/pay',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def pay_callback(self, out_trade_no, amount):
        """
        支付回调接口
        :param out_trade_no:  t_channel_bill.id(通过ms-order.t_order.trade_no→ms-pay.t_channel_bill.biz_num)
        :return:
        """
        channel_bill_id = self.tool.ms_query_channel_bill_id_by_trade_no(out_trade_no)[-1]['submit_id']
        data = '<xml>' \
               '<appid><![CDATA[wxd671c7f5343b1390]]></appid>' \
               '<bank_type><![CDATA[CFT]]></bank_type>' \
               '<cash_fee><![CDATA[1]]></cash_fee>' \
               '<fee_type><![CDATA[CNY]]></fee_type>' \
               '<is_subscribe><![CDATA[N]]></is_subscribe>' \
               '<mch_id><![CDATA[1516283721]]></mch_id>' \
               '<mch_id><![CDATA[1516283721]]></mch_id>' \
               '<nonce_str><![CDATA[0.3152113520610267]]></nonce_str>' \
               '<openid><![CDATA[oXcOU0roMiF1x8srzActZJNZH0ks]]></openid>' \
               '<result_code><![CDATA[SUCCESS]]></result_code>' \
               '<return_code><![CDATA[SUCCESS]]></return_code>' \
               '<time_end><![CDATA[20181113142514]]></time_end>' \
               '<total_fee>%s</total_fee>' \
               '<trade_type><![CDATA[APP]]></trade_type>' \
               '<out_trade_no><![CDATA[%s]]></out_trade_no>' \
               '<transaction_id><![CDATA[4200000228%s8497]]></transaction_id>' \
               '</xml>' % (str(amount), str(channel_bill_id), datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        data_byte = data
        headers = {
            "Content-Type": "charset=UTF-8,*/*",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/68.0.3440.106 Safari/537.36"
        }
        response = self.request.post(url=self.hosts['MS_PAY'] + '/notify/test/2/notice',
                                     data=data_byte, headers=headers)
        return response

    def _mobile_customer_service_order_cancel(self, orderNo):
        '''
        baiying：买家服务单取消订单
        :param orderNo:订单编号
        :return:
        '''
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'orderNo': orderNo}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/service/order/cancel', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_customer_service_order_detail(self, orderNo):
        """
        baiying:买家服务单订单详情
        :param orderNo:
        :return:
        """
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'orderNo': orderNo}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/service/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_order_earn_info = self.tool.ms_query_buyer_order_info_by_order_no(orderNo)[0]
            assert query_order_earn_info.get('content') == json_response['content']['content']
            assert query_order_earn_info.get('door_address') == json_response['content']['doorAddress']
            assert query_order_earn_info.get('door_time') == json_response['content']['doorTime']
            assert query_order_earn_info.get('earnest_money_price') == json_response['content'].get('earnestMoneyPrice')
            assert query_order_earn_info.get('order_status') == json_response['content']['orderStatus']
            assert query_order_earn_info.get('orderStatusDesc') == json_response['content']['orderStatusDesc']
            assert query_order_earn_info.get('service_type') == json_response['content']['serviceType']
            assert query_order_earn_info.get('mobile') == json_response['content']['sellerMobile']
            assert query_order_earn_info.get('trade_no') == json_response['content']['earnestMoneyTradeNo']
            assert query_order_earn_info.get('earnestMoneyPayStatus') == json_response['content'].get(
                'earnestMoneyPayStatus')
            if len(self.tool.ms_query_buyer_order_info_by_order_no(orderNo)) == 2:
                query_order_tail_info = self.tool.ms_query_buyer_order_info_by_order_no(orderNo)[1]
                assert query_order_tail_info.get('tailMoneyPayStatus') == json_response['content'].get(
                    'tailMoneyPayStatus')
                assert query_order_tail_info.get('tail_money_price') == json_response['content'].get(
                    'tailMoneyPrice')
                assert query_order_tail_info.get('trade_no') == json_response['content'].get(
                    'tailMoneyTradeNo')
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_customer_service_order_list(self, orderStatus, pn=1, ps=20):
        '''
        baiying:买家服务单订单列表
        :param orderStatus:
        :param pn:
        :param ps:
        :return:
        '''
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'orderStatus': orderStatus, 'pn': pn,
                'ps': ps}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/service/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_customer_service_order_unpaid_tail_money(self):
        '''
        baiying:获取用户未支付尾款的订单编号
        :return:
        '''
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/service/order/unpaid-tail-money',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _admin_report_service_order_service_data_card(self, startTime, endTime):
        '''
        baiying:服务数据卡片
        :param startTime:开始时间
        :param endTime:结束时间
        :return:
        '''
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/admin/report/service-order/service-data-card', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_address_add(self, receiver, contact_number, province, city, address, door_number, lng, lat,
                            is_default):
        """
        陈秀娟:添加收货地址
        :param receiver:
        :param contact_number:
        :param province:
        :param city:
        :param address:
        :param door_number:
        :param lng:
        :param lat:
        :param is_default:
        :return:
        """
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id,
                'receiver': receiver, 'contactNumber': contact_number, 'province': province, 'city': city,
                'address': address, 'doorNumber': door_number, 'lng': lng, 'lat': lat, 'isDefault': is_default}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/address/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_del(self, address_id):
        """
        chenxiujuan:删除收货地址
        :param address_id:地址id
        :return:
        """
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'addressId': address_id}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/address/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_edit(self, id, user_id, receiver, contact_number, province, city, address, door_number, lng,
                             lat,
                             is_default):
        """
        chenxiujuan:编辑地址
        :param id:
        :param user_id:
        :param receiver:
        :param contact_number:
        :param province:
        :param city:
        :param address:
        :param door_number:
        :param lng:
        :param lat:
        :param is_default:
        :return:
        """
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'id': id, 'userId': user_id, 'receiver':
                receiver, 'contactNumber': contact_number, 'province': province, 'city': city, 'address': address,
                'doorNumber': door_number, 'lng': lng, 'lat': lat, 'isDefault': is_default}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/address/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_list(self):
        """
        chenxiujuan:获取地址列表
        :return:
        """
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/address/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_address_set_default(self, address_id, user_id):
        """
        chenxiujuan:设置默认地址
        :param address_id:
        :param user_id:
        :return:
        """
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'addressId': address_id, 'userId': user_id}
        response = self.request.post(url=self.hosts['MS_USER'] + 'mobile/address/set-default', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_find_nearby_shop(self, lng, lat, distance, pn, ps):
        """
        chenxiujuan:搜索附近苗叔
        :param lng:
        :param lat:
        :param distance:
        :param pn:
        :param ps:
        :return:
        """
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'lng': lng, 'lat': lat, 'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/find-nearby-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_search_search_nearby_shop(self, searchContent, shopTag, secondCategoryId, upKeepServer, plantServer,
                                              lat, lng, distance, pn, ps):
            """
            chenxiujuan:苗木购买,搜索附近苗叔
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
            data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id,
                    'searchContent': searchContent, 'shopTag': shopTag, 'secondCategoryId': secondCategoryId,
                    'upKeepServer': upKeepServer, 'plantServer': plantServer, 'lat': lat, 'lng': lng,
                    'distance': distance, 'pn': pn, 'ps': ps}
            response = self.request.post(url=self.hosts['MS_SEARCH'] + '/mobile/search/search-nearby-shop',
                                         data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

    def _mobile_search_search_shop_product(self, searchContent, shopTag, secondCategoryId, upKeepServer,
                                               plantServer,
                                               lat, lng, distance, pn, ps):
            """
            chenxiujuan:搜索店铺商品和商品所属店铺
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
            data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id,
                    'searchContent': searchContent,
                    'shopTag': shopTag, 'secondCategoryId': secondCategoryId, 'upKeepServer': upKeepServer,
                    'plantServer': plantServer, 'lat': lat, 'lng': lng, 'distance': distance, 'pn': pn, 'ps': ps}
            response = self.request.post(url=self.hosts['MS_SEARCH'] + '/mobile/search/search-shop-product',
                                         data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

    def _mobile_product_shop_products(self, shopId):
            """
            chenxiujuan:查询店铺所有商品
            :param shopId:
            :return:
            """
            data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'shopId': shopId}
            response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/mobile/product/shop-products', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")
            return json_response

    def _mobile_product_detail(self, pcode):
            """
            chenxiujuan:查看商品详情
            :param pcode:商品编码
            :return:
            """
            data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'pcode': pcode}
            response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/mobile/product/detail', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

    def _mobile_cart_add(self, pcode, amount):
            """
            chenxiujuan:加入购物车
            :param pcode:
            :param amount:
            :return:
            """
            data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'pcode': pcode,
                    'amount': amount}
            response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/add', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

    def _mobile_cart_balance(self, cartIds, addressId):
            """
            chenxiujuan:购物车结算
            :param cartIds:
            :param addressId:
            :return:
            """
            data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'cartIds': cartIds,
                    'addressId': addressId}
            response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/balance', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

    def _mobile_cart_delete(self, cartId):
            """
            chenxiujuan:删除购物车商品
            :param cartId:
            :return:
            """
            data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'cartId': cartId}
            response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/delete', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

    def _mobile_cart_batch_delete(self, cartIds):
        """
        chenxiujuan:批量删除购物车商品
        :param cartIds:
        :return:
        """
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'cartIds': cartIds}
        response = self.request.post(url=self.hosts['MS_CART'] + '/cart/batch-delete', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_editAmount(self, cartId, amount):
            """
            chenxiujuan:编辑库存数量
            :param cartId:
            :param amount:
            :return:
            """
            data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'cartId': cartId,
                    'amount': amount}
            response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/editAmount', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

    def _mobile_cart_list(self, type):
            """
            chenxiujuan:获取购物车列表
            :return:
            """
            data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'type':type}
            response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

    def _mobile_cart_purchase(self, pcode, amount, addressId):
            """
            chenxiujuan:买家直接购买
            :param pcode:
            :param amount:
            :param addressId:
            :return:
            """
            data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'pcode': pcode,
                    'amount': amount, 'addressId': addressId}
            response = self.request.post(url=self.hosts['MS_CART'] + '/mobile/cart/purchase', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

    # def _mobile_customer_order_submit_order(self, shopId, sellerId, buyerMemo, product, addressId,
    #                                         freight, productPrice, isCheck):
    #     """
    #     张鹏飞:确认下单
    #     :param shopId:店铺id
    #     :param sellerId:卖家id
    #     :param buyerMemo:买家备注
    #     :param product:商品信息json字符串
    #     :param addressId:收货地址
    #     :param freight:运费
    #     :param productPrice:商品总金额
    #     :param isCheck:是否检查商品和运费价格变动,默认检查
    #     :return:
    #     """
    #     data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'shopId': shopId,
    #             'sellerId': sellerId, 'buyerMemo': buyerMemo, 'product': product, 'addressId': addressId,
    #             'freight': freight, 'productPrice': productPrice, 'isCheck': isCheck}
    #     response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/order/submit-order', data=data)
    #     json_response = json.loads(response)
    #     if json_response["status"] == "OK":
    #         pass
    #     elif json_response["status"] == "ERROR":
    #         pass
    #     else:
    #         raise Exception("status未返回OK或ERROR")

    def _mobile_customer_order_apply_refund(self, order_no):
        """
        张鹏飞:已付款订单申请取消
        :param orderNo: 订单编号
        :return:
        """
        data = {'_tk_': self.purchaser.token, '_deviceId_': self.purchaser.device_id, 'orderNo': order_no}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/order/apply-refund', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")



if __name__ == '__main__':
    from backend.User import User
    # 登录
    buyer = User('18582549267')
    pa = PurchaserAction(buyer)
    # pa._mobile_customer_service_order_detail()
# if __name__ == '__main__':
#     from backend.User import User
#     # 登录
#     buyer = User('18380581401')
#     pa = PurchaserAction(buyer)
#     pa.order_detail('MSSP2018121911285625106006')

    # 新增地址
    pa._mobile_address_add(1211, 'hello', '19982917912', '41', '4101', '天府五街', 'E3-9', '104.069',
                           '30.539', 1)
    # 删除地址
    # pa._mobile_address_del(1)
    # 编辑地址
    # pa._mobile_address_edit(36, '陈', '19982917912', '41', '4101', '天府五街', 'E3-9', '116.397128', '39.916527', 0)
    # 获取地址列表
    # pa._mobile_address_list(1211)
    # 设置默认地址
    # pa._mobile_address_set_default(1, 1185)
    # 搜索附近苗叔
    # pa._mobile_shop_find_nearby_shop('104.069', '30.539', 30, 1, 20)
    # pa._mobile_search_search_nearby_shop('大白菜', '蔬菜', '63', '', '', '30.539', '104.069', 30, 1, 20)
    # # 搜索苗叔店铺商品
    # pa._mobile_search_search_shop_product('正常运费模板北方大苹果', '', '66', '', '', '30.539', '104.069', 30, 1, 20)
    # p_code =pa._mobile_search_search_shop_product('content')
    # 查询所有商品
    # pa._mobile_product_shop_products(144)
    # 查看商品详情
    # pa._mobile_product_detail(206066000468)
    # 加入购物车
    # pa._mobile_cart_add(206066000468, 3)
    # 购物车结算
    # pa._mobile_cart_balance(8, 152)
    # 删除购物车商品
    # pa._mobile_cart_delete()
    # 批量删除购物车商品
    # pa._mobile_cart_batch_delete()
    # 编辑库存数量
    # pa._mobile_cart_editAmount()
    # 获取购物车列表
    # pa._mobile_cart_list(10)
    # 直接购买
    # pa._mobile_cart_purchase(206066000404, 2, 8)
    # 确认下单
    # pa._mobile_customer_order_submit_order(144, 1213, '陈',
    #                                        '[{"cartId": "8", "pCode": "206066000468", "num": "3", "image":"http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-product/product-img/1544861185297.png"}]',
    #                                        '152', '0', '45', 'true')
    # 收银台
    # pa._mobile_cashier_index(102018121810064710608032)
    #支付
    # pa._mobile_weipay_pay(102018121810064710608032, 144, 45)
    # 支付回调
    # pa.pay_callback()






    # pa.order_list(20)
    # pa.order_detail()
    # pa._mobile_customer_service_order_unpaid_tail_money()
    # pa._mobile_customer_service_order_cancel

#     # 切换角色
#     buyer.change_identity()
#     pa = PurchaserAction(buyer)
#     print(pa.pay_callback("2018111910000000038"))
#     # # 获取用户基本信息
#       pa.get_basic_info()
#     # # 更新用户的昵称
#     # pa.update_nickname("DravenZ")
#     # # 用户添加收货地址
#     # pa.add_address()
#     # 查询地址列表
#     address_list = pa.get_address_list()
#     address = address_list['content'][0]
#     add_id = address['id']
#     # # pa.update_head_img()
#     # 查询店铺列表
#     shop_list = pa.shop_search('给哈哈')['content']['datas']
#     store_id = shop_list[0]['shopId']
#     # 店铺内商品列表
#     product_list = pa.get_shop_products_by_shop_id(store_id)
#     p_code = product_list['content'][1]['productList'][0]['pcode']
#     # # 商品详情
#     # pa.get_product_detail(p_code)
#     # # 从商品详情页购买确认订单
#     # sure_order = pa.cart_purchase(p_code, 1, add_id)
#     # # 确认提交订单
#     # pa.submit_order(pa.tool.order_info_change(sure_order))
#     # # 获取订单列表 订单状态:待付款10 待收货20,30 交易成功40
#     # pa.order_list(10)
#     # # 获取订单详情
#     # pa.order_detail("2018111602112047202006")
#     # pa.order_close("2018111602112047202006")
#
#     # 添加购物车
#     pa.cart_add(p_code)
#     # 购物车列表
#     cart_list = pa.get_cart_list()
#     # 编辑购物车
#     # pa.cart_edit_amount()
#     # 购物车结算
#     sure_order = pa.cart_balance(pa.tool.get_cart_ids_by_cart_list(cart_list), add_id)
#     # # 确认提交订单
#     order = pa.submit_order(pa.tool.order_info_change(sure_order))
#     # # 获取订单列表 订单状态:待付款10 待收货20,30 交易成功40
#     # pa.order_list(10)
#     pa.hot_recommend()
#     pa.cashier_index(order['content']['tradeNo'])

