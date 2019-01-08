#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'xiujuan.chen'
__date__ = '2018/11/16'
"""


from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
from utils.Util import DataBaseOperate
from utils.Config import Config
import datetime


class DistributorAction(object):
    hosts = Config('config').data['hosts'][Config('config').data['run']]

    def __init__(self, distributor):
        self.log = Log('DistributorAction')
        self.distributor = distributor
        self.db = DataBaseOperate()
        self.request = Request()
        self.tool = Tool()
        self.ps = 10

    def upload_channel(self, address, name):
        """
            上传渠道商身份证照片
            :return:
            """
        response = self.request.post_file(url=self.hosts['MS_USER'] + '/mobile/channel/upload',
                                          file_path=address,
                                          data_dict={"_tk_": self.distributor.token,
                                                     "_deviceId_": self.distributor.device_id,
                                                     "identityFile": name}, file_key="identityFile")
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            assert json_response["content"].startswith("https://zyp-farm-")
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def update_channel(self):
        """
        提交渠道商身份证认证资料
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "userId": self.distributor.user_id,
                     "positive": "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data"
                                 "/ms-user/IDImg/channel/1542332224926.png",
                     "negative": "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/"
                                 "ms-user/IDImg/channel/1542332224926.png"}
        rul = self.hosts['MS_USER'] + "/mobile/channel/update"
        data = bind_data
        response = self.request.post(rul, data)
        json_response = json.loads(response)
        query_re = self.tool.ms_query_channel_zz_by_user_id(self.distributor.user_id)
        if query_re is not None:
            query_re = query_re[0]
        if json_response["status"] == "OK":
            assert query_re['positive'] == "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/" \
                                           "data/ms-user/IDImg/channel/1542332224926.png"
            assert query_re['negative'] == "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/" \
                                           "ms-user/IDImg/channel/1542332224926.png"
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def shop_get(self):
        """
        通过当前用户，获取店铺信息
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id}
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/get',
                                     data=bind_data)
        json_response = json.loads(response)
        db_shop_info = Tool.ms_query_shop_info_by_seller_id(self.distributor.user_id, current=True)[0]
        if json_response["status"] == "OK":
            assert json_response["content"]["address"]["address"] == db_shop_info["address"]
            assert json_response["content"]["address"]["area"] == db_shop_info["area"]
            assert json_response["content"]["address"]["city"] == db_shop_info["city"]
            assert json_response["content"]["address"]["lng"] == db_shop_info["lng"]
            assert json_response["content"]["address"]["province"] == db_shop_info["province"]
            assert json_response["content"]["address"]["shopId"] == db_shop_info["shop_id"]
            assert json_response["content"]["address"]["status"] == db_shop_info["status"]
            assert json_response["content"]["avatar"] == db_shop_info["avatar"]
            assert json_response["content"]["contact"] == db_shop_info["contact"]
            assert json_response["content"]["mobile"] == db_shop_info["mobile"]
            assert json_response["content"]["name"] == db_shop_info["name"]
            # assert json_response["content"]["pv"] == db_shop_info["pv"]
            assert json_response["content"]["sellerId"] == db_shop_info["seller_id"]
            assert json_response["content"]["shopId"] == db_shop_info["shop_id"]
            assert json_response["content"]["status"] == db_shop_info["status"]
            assert json_response["content"]["type"] == db_shop_info["type"]
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def get_fail_channel(self):
        """
        获取未通过的渠道商身份认证资料
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "userId": self.distributor.user_id}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/channel/get-fail',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def upload_avatar(self):
        """
        上传店铺头像
        :return:
        """
        response = self.request.post_file(url=self.hosts['MS_SHOP'] + '/mobile/shop/upload-avatar',
                                          file_path='./picture/1.png',
                                          data_dict={"_tk_": self.distributor.token,
                                                     "_deviceId_": self.distributor.device_id,
                                                     "avatar": "test.png"}, file_key="avatar")
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            assert json_response["content"].startswith("http://dnkj-family-")
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def shop_send_verify_code(self):
        """
        发送修改店铺联系电话验证码
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "mobile": "12300000000"}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/shop/send-verify-code",
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def shop_update_mobile(self, mobile, code):
        """
        提交修改店铺联系电话验证码
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "mobile": mobile,
                     "verifyCode": code}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/shop/update-mobile",
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def update_shop_info(self, shop):
        """
        张鹏飞:更新店铺信息
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "sellerId": self.distributor.user_id,
                     "name": shop.name,
                     "shopId": self.distributor.channel_shop_id,
                     # "mobile": shop.mobile,
                     "contact": shop.contact,
                     "avatar": shop.avatar}
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/update-shop-info',
                                     data=bind_data)
        json_response = json.loads(response)
        update_shop_info = self.tool.ms_query_update_shop_info_by_seller_id(self.distributor.user_id)[0]
        if json_response["status"] == "OK":
            assert update_shop_info["name"] == bind_data['name']
            # assert update_shop_info["mobile"] == bind_data['mobile']
            assert update_shop_info["contact"] == bind_data['contact']
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def switch_status(self, shop_id, status=10, check="true"):
        """
        更新店铺营业状态（10 营业中 20 休息）
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "shopId": shop_id,
                     "status": status,
                     "check": check}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/shop/switch-status", data=bind_data)
        json_response = json.loads(response)
        update_shop_info = self.tool.ms_query_update_shop_info_by_seller_id(self.distributor.user_id)[0]
        if json_response["status"] == "OK":
            assert update_shop_info["status"] == status
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def add_address(self, shop):
        """
        新增地址
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "_language_": 'zh',
                     "shopId": shop.shopId,
                     "lng": shop.lng,
                     "lat": shop.lat,
                     "province": shop.province,
                     "city": shop.city,
                     "area": shop.area,
                     "address": shop.address}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/address/add", data=bind_data)
        add_address_info = self.tool.ms_query_latest_address_info_by_shop_id(self.get_shop_id_by_type(
            self.distributor.user_id).get('content').get('shopId'))[0]
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            # pass
            assert add_address_info["lng"] == shop.lng
            assert add_address_info["lat"] == shop.lat
            assert add_address_info["province"] == shop.province
            assert add_address_info["city"] == shop.city
            assert add_address_info["area"] == shop.area
            assert add_address_info["address"] == shop.address
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def history_address(self):
        """
        获取历史地址列表
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     }
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/address/history", data=bind_data)
        address_info = self.tool.ms_query_all_address_info_by_shop_id(self.shop_get()["shopId"])
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            # pass
            assert len(json_response["content"]) == len(address_info)
            for n in range(len(address_info)):
                assert json_response["content"][n]["address"] == address_info[n]["address"]
                assert json_response["content"][n]["area"] == address_info[n]["area"]
                assert json_response["content"][n]["city"] == address_info[n]["city"]
                assert json_response["content"][n]["lat"] == address_info[n]["lat"]
                assert json_response["content"][n]["lng"] == address_info[n]["lng"]
                assert json_response["content"][n]["province"] == address_info[n]["province"]
                assert json_response["content"][n]["shopId"] == address_info[n]["shop_id"]
                assert json_response["content"][n]["status"] == address_info[n]["status"]
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def upload_img_product(self):
        """
        图片上传
        :return:
        """
        response = self.request.post_file(url=self.hosts['MS_PRODUCT'] + '/common/product/upload-img',
                                          file_path='./picture/1.png',
                                          data_dict={"_tk_": self.distributor.token,
                                                     "_deviceId_": self.distributor.device_id,
                                                     "file": "test.png"}, file_key="file")
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def product_save(self, product):
        """
        上架新商品
        :param product: 传入商品对象，Product.py
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "parentId": product.parent_category_id,
                     "categoryId": product.category_id,
                     "name": product.name,
                     "shopId": product.channel_shop_id,
                     "price": product.price,
                     "storeUnitId": product.unit_id,
                     "content": product.content,
                     "store": product.store,
                     "freightId": product.freight_id,
                     "status": product.status,
                     "serviceType": product.product_serviceType,
                     "imgs": product.image}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/save", data=bind_data)
        product_info = self.tool.ms_query_channel_product_info_by_shop_id(self.get_shop_id_by_type(
            self.distributor.user_id).get('content').get('shopId'))
        json_response = json.loads(response)
        if json_response["status"] == "OK":
                assert product_info[0]["name"] == product.name
                assert product_info[0]["shop_id"] == product.channel_shop_id
                assert product_info[0]["price"] == product.price
                assert product_info[0]["store_unit_id"] == product.unit_id
                assert product_info[0]["content"] == product.content
                assert product_info[0]["store"] == product.store
                assert product_info[0]["status"] == product.status
                assert product_info[0]["service_type"] == product.product_serviceType
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def list_all_category(self):
        """
        所有分类列表
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/category/list-all", data=bind_data)
        product_category_info = self.tool.ms_query_channel_product_category_info_by_id_delete(10)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            for n in range(len(product_category_info)):
                assert json_response["content"][n]["id"] == product_category_info[n]["id"]
                assert json_response["content"][n]["name"] == product_category_info[n]["name"]
                assert json_response["content"][n]["parent"] == product_category_info[n]["parent"]
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def list_category(self, category, search):
        """
        根据条件查找分类列表
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "categoryId": category,
                     "search": search
                     }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/category/list", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def find_product(self, pcode):
        """
        商品详情
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "pcode": pcode
                     }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/find", data=bind_data)
        product_info = self.tool.ms_query_channel_search_product_by_product_code(pcode)[0]
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            assert json_response["content"]["categoryId"] == product_info["category_id"]
            assert json_response["content"]["categoryName"] == product_info["name"]
            assert json_response["content"]["content"] == product_info["content"]
            assert json_response["content"]["freightId"] == product_info["freight_id"]
            assert json_response["content"]["fullName"] == product_info["full_name"]
            assert json_response["content"]["imgs"] == product_info["url"]
            # assert json_response["content"]["name"] == product_info["name"]
            assert json_response["content"]["pcode"] == product_info["pcode"]
            assert json_response["content"]["price"] == product_info["price"]
            assert json_response["content"]["sales"] == product_info["sales"]
            assert json_response["content"]["shopId"] == product_info["shop_id"]
            assert json_response["content"]["status"] == product_info["status"]
            assert json_response["content"]["storeUnitId"] == product_info["store_unit_id"]
            # assert json_response["content"]["storeUnitName"] == product_info["name"]

        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def list_product(self, product, service_type=20, status=10, sort=1, search=None, pn=1, ps=20):
        """
        根据条件查询商品列表
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "serviceType": service_type,
                     "shopId": product.channel_shop_id,
                     "parentId": product.parent_category_id,
                     "categoryId": product.category_id,
                     "status": status,
                     "sort": sort,
                     "search": search,
                     "pn": pn,
                     "ps": ps
                     }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/list", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def status_list_product(self):
        """
        商品状态列表
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/status-list", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def status_update_product(self, pro_code, pro_status=10):
        """
        商品上架/下架/删除
        :param pro_code: 商品的编码
        :param pro_status: 操作码(10：上架；20：下架; 30：删除)
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "pcode": pro_code,
                     "operation": pro_status
                     }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/status-update", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def store_list_product(self, product, sort=1, search=None, pn=1, ps=20):
        """
        渠道商库存列表
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "shopId": product.channel_shop_id,
                     "parentId": product.parent_category_id,
                     "categoryId": product.category_id,
                     "search": search,
                     "sort": sort,
                     "pn": pn,
                     "ps": ps
                     }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/store-list", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def store_update_product(self, pro_code, pro_num=15):
        """
        库存更新
        :return:
        """
        data = '[{"pcode": %s, "store": %s}]' % (pro_code, pro_num)
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "stores": data
                     }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/store-update", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def update_product(self):
        """
        更新商品
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "pcode": 200014000119,
                     "parentId": 0,
                     "categoryId": 14,
                     "name": "小红",
                     "shopId": 164,
                     "price": 130,
                     "storeUnit": 200,
                     "content": "好看",
                     "store": "250",
                     "freightId": "-1",
                     "status": "20",
                     "serviceType": "20",
                     "imgs": self.upload_img_product()}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/update", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def list_store_unit(self):
        """
        查看库存单位列表
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     }
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/store-unit/list", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def freight_save_or_update(self, shop_id, title, freighPerKm, freePrice, freeDistance):
        """
        张鹏飞:新建或者编辑运费模板
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "shopId": shop_id,
                     "title": title,
                     "freighPerKm": freighPerKm,
                     "freePrice": freePrice,
                     "freeDistance": freeDistance,
                     }
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/freightTemplate/save-or-update", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def delete_freight(self, freight_id):
        """
        删除模板
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "id": freight_id
                     }
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/freightTemplate/delete", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def get_freight(self, freight_id):
        """
        获取单个运费模板
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "id": freight_id
                     }
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/freightTemplate/get/{id}", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def all_freight(self):
        """
        获取全部运费模板
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "shopId": self.distributor.channel_shop_id
                     }
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/freightTemplate/all", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def pending_count_order(self):
        """
        张鹏飞:待处理订单总数
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "shopId": "169"
                     }
        response = self.request.post(url=self.hosts['MS_ORDER'] + "/mobile/channel/order/pending-count",
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def list_order(self, order_status):
        """
        张鹏飞:订单列表
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "orderStatus": order_status
                     }
        response = self.request.post(url=self.hosts['MS_ORDER'] + "/mobile/channel/order/list", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def shopping_order_detail(self, order_no):
        """
        张鹏飞:订单详情
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "orderNo": order_no
                     }
        response = self.request.post(url=self.hosts['MS_ORDER'] + "/mobile/channel/order/detail", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            json_response = json_response.get('content')
            query_order_detail = self.tool.ms_query_seller_shop_order_detail_by_order_no(order_no)[0]
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
            assert query_order_detail.get('receiveAddress') == json_response.get('receiveAddress')
            assert query_order_detail.get('receiveLat') == json_response.get('receiveLat')
            assert query_order_detail.get('receiveLng') == json_response.get('receiveLng')
            assert query_order_detail.get('receiveMobile') == json_response.get('receiveMobile')
            assert query_order_detail.get('receiveName') == json_response.get('receiveName')
            assert query_order_detail.get('tradeNo') == json_response.get('tradeNo')
            assert "送货上门" == json_response.get('sendTypeDes')
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def finish_send_order(self, order_no):
        """
        张鹏飞:完成配送
        :return:
        """
        bind_data = {"_tk_": self.distributor.token,
                     "_deviceId_": self.distributor.device_id,
                     "orderNo": order_no
                     }
        response = self.request.post(url=self.hosts['MS_ORDER'] + "/mobile/channel/order/finish-send", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def find_nearby_shop(self, lng, lat, distance, pn, ps):
        """
        移动端--根据经纬度和半径查找附近的店铺---已通
        :param lng:
        :param lat:
        :param distance:
        :param pn:
        :param ps:
        :return:
        """
        bind_data = {"lng": lng,
                     "lat": lat,
                     "distance": distance,
                     "pn": pn,
                     "ps": ps}
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/find-nearby-shop',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def get_city_list(self, pid=1):
        """
        获取城市列表---已通
        :param pid:
        :return:
        """
        bind_data = {'pid': pid}
        response = self.request.post(url=self.hosts['MS_KBMS'] + '/config/common/get-city-list',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            db_city_list = self.tool.ms_query_city_list_by_parent_id(pid)
            for a in range(len(db_city_list)):
                assert db_city_list[a]["id"] == json_response["content"][a]["id"]
                assert db_city_list[a]["name"] == json_response["content"][a]["name"]
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def get_shop_info_by_shop_id(self, shop_id, lng=None, lat=None):
        """
        移动端---使用店铺ID，获取店铺信息（不用登录）---已通
        :param shop_id: 商店ID <= ms-shop.t_shop.id
        :param lng:
        :param lat:
        :return:
        """
        bind_data = {"id": shop_id,
                     "lng": lng,
                     "lat": lat}
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/get/%s' % str(shop_id),
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            db_shop_list = self.tool.ms_shop_t_address_list_by_shop_id(shop_id)
            assert db_shop_list[0]["shop_id"] == json_response["content"]["shopId"]

        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def shop_refreshpvuv(self, shopId, deviceId):
        """
        移动端---刷新店铺PV和UV---已通
        :param shopId:
        :param deviceId:
        :return:
        """
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/refreshPVUV/%s/%s' % (shopId, deviceId), data={})
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def get_push_alias(self):
        """
        移动端-用户信息中心----获取推送别名---已通
        :return:
        """""
        bind_data = {}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/user/get-push-alias',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def role_list(self):
        """
        移动端-用户信息中心----获取身份列表----已通
         :param self:
         :return:
        """
        bind_data = {}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/user/role-list',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_channel_service_order_detail(self, orderNo):
        """
        张鹏飞:获取订单详情
        :param orderNo: 订单编号
        :return:
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'orderNo': orderNo}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/channel/service/order/detail', data=data)
        json_response = json.loads(response)

        if json_response["status"] == "OK":
            query_order_earn_info = self.tool.ms_query_seller_order_info_by_order_no(orderNo)[0]
            assert query_order_earn_info.get('content') == json_response['content']['content']
            assert query_order_earn_info.get('door_address') == json_response['content']['doorAddress']
            assert query_order_earn_info.get('door_time') == json_response['content']['doorTime']
            assert query_order_earn_info.get('earnest_money_price') == json_response['content'].get('earnestMoneyPrice')
            assert query_order_earn_info.get('order_status') == json_response['content']['orderStatus']
            assert query_order_earn_info.get('orderStatusDesc') == json_response['content']['orderStatusDesc']
            assert query_order_earn_info.get('service_type') == json_response['content']['serviceType']
            assert query_order_earn_info.get('mobile') == json_response['content']['buyerMobile']
            assert query_order_earn_info.get('trade_no') == json_response['content']['earnestMoneyTradeNo']
            assert query_order_earn_info.get('earnestMoneyPayStatus') == json_response['content'].get('earnestMoneyPayStatus')
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

    def _mobile_channel_service_order_finish_door(self, orderNo, tailMoneyPrice):
        """
        张鹏飞:完成上门
        :param orderNo: 订单编号
        :param tailMoneyPrice: 尾款金额,单位分
        :return: 只返回操作的结果,OK
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'orderNo': orderNo, 'tailMoneyPrice': tailMoneyPrice}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/channel/service/order/finish-door', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_service_order_list(self, order_status, pn=1, ps=20):
        """
        张鹏飞:获取订单列表
        :param order_status: 订单状态,10:待下单, 20:待上门, 30:已结款, 40:已完成, 50: 已取消
        :param pn: 第几页
        :param ps: 一页多少条数据
        :return: 返回一个订单列表
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'orderStatus': order_status, 'pn': pn, 'ps': ps}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/channel/service/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            json_response = json_response['content']['datas']
            query_order_list = self.tool.ms_query_seller_id_order_list_by_user_id(self.distributor.user_id, order_status, ps, pn)
            for i in range(len(query_order_list)):
                if query_order_list[i].get('tail_money_price') is None:
                    assert query_order_list[i].get('earnest_money_price') == json_response[i].get('price')
                else:
                    assert query_order_list[i].get('tail_money_price') == json_response[i].get('price')
                assert query_order_list[i].get('orderStatus') == json_response[i]['orderStatus']
                assert query_order_list[i].get('orderStatusDesc') == json_response[i]['orderStatusDesc']
                assert query_order_list[i].get('buyerMobile') == json_response[i]['buyerMobile']
                assert query_order_list[i].get('orderNo') == json_response[i]['orderNo']
                assert query_order_list[i].get('serviceTypeDesc') == json_response[i].get('serviceTypeDesc')
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_service_order_submit(self, buyerId, shopId, serviceType, doorTime, content, earnestMoneyPrice, doorAddress=None, lng=None, lat=None):
        """
        张鹏飞:提交服务订单
        :param buyerId:  买家ID
        :param shopId:  channel_shop_id
        :param serviceType: 服务类型, 10:上门种植,20:上门养护
        :param doorTime: 上门时间,eg:2018-12-30 16:00
        :param content:养护需求
        :param earnestMoneyPrice:定金,单位为分
        :param doorAddress:上门地址
        :param lng:上门地址经度
        :param lat:上门地址纬度
        :return: 返回一个订单号,格式:{
                                    content (string, optional): 数据对象 ,
                                    errorCode (string, optional): 错误码 ,
                                    errorMsg (string, optional): 错误消息 ,
                                    status (string, optional): 状态:OK|ERROR
                                    }
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'buyerId': buyerId, 'shopId': shopId, 'serviceType': serviceType, 'doorTime': doorTime, 'doorAddress': doorAddress, 'lng': lng, 'lat': lat, 'content': content, 'earnestMoneyPrice': earnestMoneyPrice}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/channel/service/order/submit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_apply_channel(self):
        """
        苗叔申请() - 杨
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/apply/channel', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_apply_channel_status(self):
        """
        获取苗叔申请状态(已通)-杨
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/apply/channel-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_shop_server_server(self, type, status):
        """
        张鹏飞:开通或者关闭上门养护和上门种植服务
        :param type: 服务类型, 10:上门养护,20:上门种植
        :param status: 服务状态, 10 开通, 20 关闭
        :return:
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'type': type, 'status': status}
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/server/server', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def get_shop_id_by_type(self, seller_id, type=20):
        """
        张鹏飞:根据user_id获取店铺信息
        :param seller_id: user_id
        :param type: 店铺类型,20是苗叔,30是基地
        :return: 返回店铺的基本信息
        """
        data = {'_tk_': self.distributor.token,
                '_deviceId_': self.distributor.device_id,
                'sellerId': seller_id,
                'type': type
                }
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/get-by-type',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_channel_order_agree(self, order_no):
        """
        张鹏飞: 同意退款申请
        :param order_no: 订单编号
        :return:
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'orderNo': order_no}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/channel/order/agree', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_order_refuse(self, order_no):
        """
        张鹏飞:拒绝买家的取消订单
        :param order_no:
        :return:
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'orderNo': order_no}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/channel/order/refuse', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")


    def _mobile_supply_customer_order_submit_order(self, shopId, sellerId, buyerMemo, product, addressId, productPrice, isCheck):
        '''
        baiying:苗叔向基地下单
        :param shopId:
        :param sellerId:
        :param buyerMemo:
        :param product:
        :param addressId:
        :param productPrice:
        :param isCheck:
        :return:
        '''
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'shopId': shopId, 'sellerId': sellerId, 'buyerMemo': buyerMemo, 'product': product, 'addressId': addressId, 'productPrice': productPrice, 'isCheck': isCheck}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/submit-order', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response


    def _mobile_supply_customer_order_detail(self, orderNo):
        '''
        baiying:苗叔向基地购买商品详情页
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_supply_customer_order_list(self, orderStatus, pn, ps):
        '''
        白颖：苗叔订单列表
        :param orderStatus:
        :param pn:
        :param ps:
        :return:
        '''
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'orderStatus': orderStatus, 'pn': pn,
                'ps': ps}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_supply_customer_order_close(self, orderNo):
        '''
        baiying:苗叔未支付订单取消订单
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/close', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response
    def _mobile_cashier_index(self, tradeNos):
        """
        baiying:收银台
        :param tradeNos:
        :return:
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'tradeNos': tradeNos}
        response = self.request.post(url=self.hosts['MS_PAY'] + '/mobile/cashier/index', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_weipay_pay(self, tradeNos, channelId, channelAmount):
        """
        支付
        :param tradeNos:订单的交易号
        :param channelId:苗叔ID
        :param channelAmount:订单金额(分)
        :return:
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'tradeNos': tradeNos,
                'channelId': channelId, 'channelAmount': channelAmount}
        response = self.request.post(url=self.hosts['MS_PAY'] + '/mobile/weipay/pay', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
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

    def _mobile_supply_customer_order_apply_refund(self, orderNo):
        '''
        baiying:苗叔申请已付款订单取消订单
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/apply-refund', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_supply_customer_order_confirm_receive(self, orderNo):
        '''
        baiying:苗叔已完成订单
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/confirm-receive', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
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
            '_tk_': self.distributor.token,
            '_deviceId_': self.distributor.device_id
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

    def get_cart_list(self, cart_type=20):
        """
        获取购物车列表
        :param cart_type:
        :return: 返回一个列表{"content":{"productCount":0,"shopItem":[]},"status":"OK"}
        """
        data = {
            '_tk_': self.distributor.token,
            '_deviceId_': self.distributor.device_id,
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
            '_tk_': self.distributor.token,
            '_deviceId_': self.distributor.device_id,
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

    def cart_balance(self, cart_ids, address_id=None):
        """
        购物车结算
        :param cart_ids: 购物车内商品的购物车ID集合,用逗号分隔,eg:1,2,3
        :param address_id: 地址ID
        :return:
        """
        data = {
            '_tk_': self.distributor.token,
            '_deviceId_': self.distributor.device_id,
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

    def submit_order(self, order_data, is_check=0):
        """
        提交订单
        :param order_data: 订单的信息
        :param is_check: 是否check.默认不check
        :return: 返回订单号
        """
        data = {
            '_tk_': self.distributor.token,
            '_deviceId_': self.distributor.device_id
        }
        data.update(order_data)
        data['isCheck'] = is_check
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/supply/customer/order/submit-order',
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
            '_tk_': self.distributor.token,
            '_deviceId_': self.distributor.device_id,
            'orderNo': order_no
        }
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/mobile/customer/order/detail',
                                     data=data)
        json_response = json.loads(response)
        # if json_response["status"] == "OK":
        #     json_response = json_response.get('content')
        #     query_order_detail = self.tool.ms_query_buyer_shop_order_detail_by_order_no(order_no)[0]
        #     if query_order_detail.get('applyStatus') is not None:
        #         assert query_order_detail.get('applyStatus') == json_response.get('applyStatus')
        #         assert query_order_detail.get('applyStatusDesc') == json_response.get('applyStatusDesc')
        #     assert query_order_detail.get('buyerId') == json_response.get('buyerId')
        #     assert query_order_detail.get('buyerHeadImg') == json_response.get('buyerHeadImg')
        #     assert query_order_detail.get('createTime') == json_response.get('createTime')
        #     assert query_order_detail.get('freight') == json_response.get('freight')
        #     assert query_order_detail.get('orderStatus') == json_response.get('orderStatus')
        #     assert query_order_detail.get('orderStatusDesc') == json_response.get('orderStatusDesc')
        #     assert query_order_detail.get('priceTotal') == json_response.get('priceTotal')
        #     if query_order_detail.get('payTime') is not None:
        #         assert query_order_detail.get('payTime') == json_response.get('payTime')
        #         assert query_order_detail.get('priceReal') == json_response.get('priceReal')
        #     assert query_order_detail.get('receiveAddress') == json_response.get('receiveAddress')
        #     assert query_order_detail.get('receiveLat') == json_response.get('receiveLat')
        #     assert query_order_detail.get('receiveLng') == json_response.get('receiveLng')
        #     assert query_order_detail.get('receiveMobile') == json_response.get('receiveMobile')
        #     assert query_order_detail.get('receiveName') == json_response.get('receiveName')
        #     if query_order_detail.get('orderStatus') == 40:
        #         assert query_order_detail.get('receiveTime') == json_response.get('receiveTime')
        #     assert query_order_detail.get('sendMobile') == json_response.get('sendMobile')
        #     assert query_order_detail.get('sendName') == json_response.get('sendName')
        #     assert query_order_detail.get('shopContact') == json_response.get('shopContact')
        #     assert query_order_detail.get('shopContactMobile') == json_response.get('shopContactMobile')
        #     assert query_order_detail.get('shopName') == json_response.get('shopName')
        #     assert query_order_detail.get('tradeNo') == json_response.get('tradeNo')
        #     assert query_order_detail.get('validDate') == json_response.get('validDate')
        #
        # elif json_response["status"] == "ERROR":
        #     raise Exception("status返回ERROR")
        # else:
        #     raise Exception("status未返回OK或ERROR")
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
        data['_tk_'] = self.distributor.token
        data['_deviceId_'] = self.distributor.device_id
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
        data['_tk_'] = self.distributor.token
        data['_deviceId_'] = self.distributor.device_id
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

    def _mobile_address_list(self):
        """
        chenxiujuan:获取地址列表
        :return:
        """
        data = {'_tk_': self.distributor.token, '_deviceId_': self.distributor.device_id}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/address/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
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


if __name__ == '__main__':
    from backend.User import User
    seller = User("18582549267")
    da = DistributorAction(seller)
    # order = da._mobile_supply_customer_order_submit_order(146, 1210, "哈哈哈这是一个备注", '[{"cartId":"58","pCode":"306066000446","num":83 ,"image":"www.baidu.com"}]', 151, 15, 'false')
    # da. _mobile_supply_customer_order_detail("JDSP2018121911181295506002")
    # da._mobile_supply_customer_order_list(50, 2, 2)
    # da._mobile_supply_customer_order_close("JDSP2018121816172747206002")
    # order_pay_info = da._mobile_cashier_index(order['content']['tradeNo'])
    # da._mobile_weipay_pay(order['content']['tradeNo'], order_pay_info['content']['channelList'][0]['id'],
    #                    order_pay_info['content']['amount'])
    # da.pay_callback(order['content']['tradeNo'], order_pay_info['content']['amount'])
    # da._mobile_supply_customer_order_apply_refund("JDSP2018121911191917806004")
    # da._mobile_supply_customer_order_confirm_receive("JDSP2018121911191917806004")
    da.history_address()
#     da._mobile_channel_service_order_submit(buyerId=1184, shopId=1,
# serviceType=10, doorTime='2019-12-16 08:00', content='养猪', earnestMoneyPrice=2187, doorAddress='ce', lng=103,lat=40)

