#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/11/6'
"""


from utils.Util import Request, Redis
from backend.Tool import Tool
from utils.Log import Log
from utils.Util import DataBaseOperate
import json
from utils.Config import Config


class SupplierAction(object):
    hosts = Config('config').data['hosts'][Config('config').data['run']]

    def __init__(self, supplier):
        self.log = Log('SupplierAction')
        self.supplier = supplier
        self.request = Request()
        self.tool = Tool()
        self.redis = Redis()
        self.db = DataBaseOperate()
        self.ps = 10

    def supp_upload(self, address, name):
            """
            上传供应商身份证照片
            :return:
            """
            response = self.request.post_file(url=self.hosts['MS_USER'] + '/mobile/supplier/upload',
                                              file_path=address,
                                              data_dict={"_tk_": self.supplier.token,
                                                         "_deviceId_": self.supplier.device_id,
                                                         "identityFile": name}, file_key="identityFile")
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                raise Exception("status返回ERROR")
            else:
                raise Exception("status未返回OK或ERROR")
            return json_response["content"]

    def supp_update(self, positive_img, negative_img):
        """
        提交供应商身份证认证资料
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "userId": self.supplier.user_id,
                     "positive": positive_img,
                     "negative": negative_img}
        rul = self.hosts['MS_USER'] + "/mobile/supplier/update"
        data = bind_data
        response = self.request.post(rul, data)
        json_response = json.loads(response)
        query_re = self.tool.ms_query_supplier_supp_update_by_user_id(self.supplier.user_id)
        if query_re is not None:
            query_re = query_re[0]
        if json_response["status"] == "OK":
            assert query_re['positive'] == positive_img
            assert query_re['negative'] == negative_img
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def supp_get_fail(self):
        """
        获取未通过的供应商身份认证资料
        断言需优化
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "userId": self.supplier.user_id}
        rul = self.hosts['MS_USER'] + "/mobile/supplier/get-fail"
        data = bind_data
        response = self.request.post(rul, data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def shop_get(self):
        """
        通过当前用户，获取店铺信息
        断言需优化
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id}
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/get',
                                     data=bind_data)
        json_response = json.loads(response)
        query_re = self.tool.ms_query_supplier_shop_get_by_user_id(self.supplier.user_id)
        if query_re is not None:
            query_re = query_re[0]
        if json_response["status"] == "OK":
            assert query_re['id'] == json_response["content"]["shopId"]
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def upload_avatar(self, address, name):
        """
        上传店铺头像
        :return:
        """
        response = self.request.post_file(url=self.hosts['MS_SHOP'] + '/mobile/shop/upload-avatar',
                                          file_path=address,
                                          data_dict={"_tk_": self.supplier.token,
                                                     "_deviceId_": self.supplier.device_id,
                                                     "avatar": name}, file_key='avatar')
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def shop_send_verify_code(self, shop_mobile):
        """
        发送修改店铺联系电话验证码
        断言需优化
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "mobile": shop_mobile}
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

    def shop_update_mobile(self, shop_mobile):
        """
        提交修改店铺联系电话验证码
        断言需优化
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "mobile": shop_mobile,
                     "verifyCode": int(self.redis.get('ShopManagerImpl:modify_shop_mobile:%s_%s'
                                                      % (str(self.supplier.user_id), str(shop_mobile))))}
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
        更新店铺信息
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "sellerId": self.supplier.user_id,
                     "name": shop.name,
                     "shopId": self.supplier.supplier_shop_id,
                     # "mobile": shop.mobile,
                     "contact": shop.contact,
                     "avatar": shop.avatar}
        response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/update-shop-info',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def update_address(self, province, city, area, address):
        """
        更新供应商店铺地址
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "sellerId": self.supplier.user_id,
                     "province": province,
                     "city": city,
                     "area": area,
                     "address": address}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/supplier/update-address", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_update_address_by_shop_id(self.shop_get()["shopId"])
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['province'] == province
                assert query_re['city'] == city
                assert query_re['area'] == area
                assert query_re['address'] == address
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def switch_status(self, switch_status):
        """
        更新店铺营业状态（10 营业中 20 休息）
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "status": switch_status,
                     "check": "true"}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/shop/switch-status", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_switch_status_by_shop_id(self.shop_get()["shopId"])
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['status'] == switch_status
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def category_list(self, category_id):
        """
        查询分类
        :return:
        """
        bind_data = {"categoryId": category_id}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/category/list", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_category_list_by_category_id(category_id)
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['count(*)'] == len(json_response['content'])
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def category_list_all(self):
        """
        查询所有分类
        :return:
        """
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/category/list", data={})
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_category_list_all_by_status(10)
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['count(*)'] == len(json_response['content'])
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def store_unit_list(self):
        """
        查询库存单位列表
        :return:
        """
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/store-unit/list", data={})
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_store_unit_list_by_is_delete(0)
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['count(*)'] == len(json_response['content'])
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"][0]["id"]

    def freight_template_all(self):
        """
        获取运费模板
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/freightTemplate/all", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_freight_template_all_by_shop_id(self.shop_get()["shopId"])
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['count(*)'] == len(json_response['content'])
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def freight_template_add(self, title, freigh_per_km, free_price, free_distance,
                             free_price_status, free_distance_status):
        """
        新建运费模板
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "title": title,
                     "freighPerKm": freigh_per_km,
                     "freePrice": free_price,
                     "freeDistance": free_distance,
                     "freePriceStatus": free_price_status,
                     "freeDistanceStatus": free_distance_status}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/freightTemplate/add", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_freight_template_add_by_freight_id(json_response["content"])
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                # assert query_re['shop_id'] == self.shop_get()["shopId"]
                # assert query_re['title'] == title
                # assert query_re['freigh_per_km'] == freigh_per_km
                # assert query_re['free_price'] == free_price
                # assert query_re['free_distance'] == free_distance
                # assert query_re['free_price_status'] == free_price_status
                # assert query_re['free_distance_status'] == free_distance_status
                pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def freight_template_delete(self, freight_id):
        """
        删除运费模板
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "id": freight_id}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/freightTemplate/delete", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_freight_template_delete_by_freight_id(freight_id)
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['shop_id'] == self.shop_get()["shopId"]
                assert query_re['id'] == freight_id
                assert query_re['is_delete'] == 1
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def freight_template_edit(self, freight_id, title=None, freigh_per_km=None, free_price=None,
                              free_distance=None, free_price_status=None, free_distance_status=None):
        """
        修改运费模板
        :return:
        """
        query_re = self.tool.ms_query_supplier_freight_template_edit_by_freight_id(freight_id)[0]
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "id": freight_id}
        if title is None:
            bind_data['title'] = query_re['title']
        else:
            bind_data['title'] = title
        if freigh_per_km is None:
            bind_data['freighPerKm'] = query_re['freigh_per_km']
        else:
            bind_data['freighPerKm'] = freigh_per_km
        if free_price is None:
            bind_data['freePrice'] = query_re['free_price']
        else:
            bind_data['freePrice'] = free_price
        if free_price is None:
            bind_data['freeDistance'] = query_re['free_distance']
        else:
            bind_data['freeDistance'] = free_distance
        if free_price is None:
            bind_data['freePriceStatus'] = query_re['free_price_status']
        else:
            bind_data['freePriceStatus'] = free_price_status
        if free_price is None:
            bind_data['freeDistanceStatus'] = query_re['free_distance_status']
        else:
            bind_data['freeDistanceStatus'] = free_price
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/freightTemplate/edit", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_freight_template_edit_by_freight_id(freight_id)
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                if bind_data['title'] != query_re['title']:
                    assert query_re['title'] == title
                if bind_data['freighPerKm'] != query_re['freigh_per_km']:
                    assert query_re['freigh_per_km'] == freigh_per_km
                if bind_data['freePrice'] != query_re['free_price']:
                    assert query_re['free_price'] == free_price
                if bind_data['freeDistance'] != query_re['free_distance']:
                    assert query_re['free_distance'] == free_distance
                if bind_data['freePriceStatus'] != query_re['free_price_status']:
                    assert query_re['free_price_status'] == free_price_status
                if bind_data['freeDistanceStatus'] != query_re['free_distance_status']:
                    assert query_re['free_distance_status'] == free_distance_status
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def freight_template_get(self, freight_id):
        """
        获取单个运费模板
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "id": freight_id}
        url = self.hosts['MS_SHOP'] + "/mobile/freightTemplate/get/%s" % str(freight_id)
        response = self.request.post(url=url, data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_freight_template_get_by_freight_id(freight_id)
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['title'] == json_response["content"]["title"]
                assert query_re['freigh_per_km'] == json_response["content"]["freighPerKm"]
                assert query_re['free_price'] == json_response["content"]["freePrice"]
                assert query_re['free_distance'] == json_response["content"]["freeDistance"]
                assert query_re['free_price_status'] == json_response["content"]["freePriceStatus"]
                assert query_re['free_distance_status'] == json_response["content"]["freeDistanceStatus"]
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def upload_img(self, img_address, img_name):
        """
        上传图片
        :return:
        """
        response = self.request.post_file(url=self.hosts['MS_PRODUCT'] + '/common/product/upload-img',
                                          file_path=img_address,
                                          data_dict={"_tk_": self.supplier.token,
                                                     "_deviceId_": self.supplier.device_id,
                                                     "file": img_name}, file_key="file")
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def status_list(self):
        """
        查询商品状态
        :return:
        """
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/status-list", data={})
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            assert json_response["content"][0]["id"] == 0
            assert json_response["content"][1]["id"] == 10
            assert json_response["content"][2]["id"] == 20
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]


    def product_list(self, parent_id=None, category_id=None, status=None, sort=None, search=None):
        """
        供应商商品列表
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "shopId": self.shop_get()["shopId"],
                     "parentId": parent_id,
                     "categoryId": category_id,
                     "status": status,
                     "sort": sort,
                     "search": search}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/list", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_product_list_by_shop_id(self.shop_get()["shopId"])
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['count(*)'] == json_response["content"]["tc"]
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]["datas"]

    def product_find(self, product_pcode):
        """
        供应商商品详情
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "pcode": product_pcode}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/find", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

    def status_update(self, product_pcode, product_operation):
        """
        商品上架/下架/删除
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "pcode": product_pcode,
                     "operation": product_operation}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/status-update", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_status_update_by_product_pcode(product_pcode)
            if query_re is not None:
                query_re = query_re[0]
                if product_operation == 30:
                    assert query_re['is_delete'] == 1
                else:
                    assert query_re['status'] == product_operation
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def product_update(self, pn, parent_id=None, category_id=None, product_name=None, store_unit_id=None,
                       product_content=None, price=None, store=None, freight_id=None, status=None, img=None):
        """
        更新商品信息
        :return:
        """
        query_re = self.tool.ms_query_supplier_product_update_by_pcode(self.product_list()[pn]["pcode"])[0]
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "shopId": self.shop_get()["shopId"],
                     "pcode":  self.product_list()[pn]["pcode"],
                     "parentId": parent_id,
                     "categoryId": category_id,
                     "name": product_name,
                     "storeUnitId": store_unit_id,
                     "content": product_content,
                     "price": price,
                     "store": store,
                     "freightId": freight_id,
                     "status": status,
                     "serviceType": 30,
                     "imgs": img}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/update", data=bind_data)
        if parent_id is None:
            bind_data['parentId'] = query_re['parent']
        else:
            bind_data['parentId'] = parent_id
        if category_id is None:
            bind_data['categoryId'] = query_re['category_id']
        else:
            bind_data['categoryId'] = category_id
        if product_name is None:
            bind_data['name'] = query_re['name']
        else:
            bind_data['name'] = product_name
        if store_unit_id is None:
            bind_data['storeUnitId'] = query_re['store_unit_id']
        else:
            bind_data['storeUnitId'] = store_unit_id
        if product_content is None:
            bind_data['content'] = query_re['content']
        else:
            bind_data['content'] = product_content
        if price is None:
            bind_data['price'] = query_re['price']
        else:
            bind_data['price'] = price
        if store is None:
            bind_data['store'] = query_re['store']
        else:
            bind_data['store'] = store
        if freight_id is None:
            bind_data['freightId'] = query_re['freight_id']
        else:
            bind_data['freightId'] = freight_id
        if status is None:
            bind_data['status'] = query_re['STATUS']
        else:
            bind_data['status'] = status
        if img is None:
            bind_data['imgs'] = query_re['url']
        else:
            bind_data['imgs'] = img
        response = self.request.post(url="http://192.168.62.253:31005/mobile/product/update", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            if json_response["status"] == "OK":
                query_re = self.tool.ms_query_supplier_product_update_by_pcode(self.product_list()[pn]["pcode"])[0]
                if bind_data['parentId'] != query_re['parent']:
                    assert query_re['parent'] == parent_id
                if bind_data['categoryId'] != query_re['category_id']:
                    assert query_re['category_id'] == category_id
                if bind_data['name'] != query_re['name']:
                    assert query_re['name'] == product_name
                if bind_data['storeUnitId'] != query_re['store_unit_id']:
                    assert query_re['store_unit_id'] == store_unit_id
                if bind_data['content'] != query_re['content']:
                    assert query_re['content'] == product_content
                if bind_data['price'] != query_re['price']:
                    assert query_re['price'] == price
                if bind_data['store'] != query_re['store']:
                    assert query_re['store'] == store
                if bind_data['freightId'] != query_re['freight_id']:
                    assert query_re['freight_id'] == freight_id
                if bind_data['status'] != query_re['STATUS']:
                    assert query_re['STATUS'] == status
                if bind_data['imgs'] != query_re['url']:
                    assert query_re['url'] == img
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def store_list(self):
        """
        库存列表
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,"shopId": self.shop_get()["shopId"],
                     "pn": 1,
                     "ps": 20}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/store-list", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_store_list_by_shop_id(self.shop_get()["shopId"])
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['count(*)'] == json_response["content"]["tc"]
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]["datas"]

    def store_update(self, stores):
        """
        库存更新
        断言需优化
        :return:
        """

        response = self.request.post(url=self.hosts['MS_PRODUCT'] + "/mobile/product/store-update",
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "shopId": self.shop_get()["shopId"],
                     "stores": stores})
        pcode_list = []
        for i in list(stores):
            pcode_list.append(i['pcode'])
        store_list = []
        for j in list(stores):
            store_list.append(j['store'])
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_re = self.tool.ms_query_supplier_store_update_by_pcode(pcode_list)
            if query_re is not None:
                query_re = query_re[0]
            if json_response["status"] == "OK":
                assert query_re['store'] == store_list
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def supp_order_list(self):
        """
        供应商订单列表
        断言需优化
        :return:
        """
        bind_data = {"shopId": self.shop_get()["shopId"]}
        response = self.request.post(url=self.hosts['MS_ORDER'] + "/mobile/supply/order/list", data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_channel_order_list(self, orderStatus, pn, ps):
        '''
        baiying:基地查看商品列表
        :param orderStatus:
        :param pn:
        :param ps:
        :return:
        '''
        data = {'_tk_': self.supplier.token, '_deviceId_': self.supplier.device_id, 'orderStatus': orderStatus, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_supply_channel_order_detail(self, orderNo):
        '''
        baiying:基地查看订单详情
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.supplier.token, '_deviceId_': self.supplier.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_supply_channel_order_refuse(self, orderNo):
        '''
        baiying：基地拒绝苗叔的取消订单申请
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.supplier.token, '_deviceId_': self.supplier.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/refuse', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_supply_channel_order_agree(self, orderNo):
        '''
        baiying:基地同意苗叔的取消订单申请
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.supplier.token, '_deviceId_': self.supplier.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/agree', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_supply_channel_order_finish_send(self, orderNo):
        '''
        baiying:基地完成配送订单
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.supplier.token, '_deviceId_': self.supplier.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/finish-send', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_channel_order_pending_count(self, shopId):
        data = {'_tk_': self.supplier.token, '_deviceId_': self.supplier.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/pending-count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def get_shop_id_by_type(self, seller_id, type=30):
        """
        张鹏飞:根据user_id获取店铺信息
        :param seller_id: user_id
        :param type: 店铺类型,20是苗叔,30是基地
        :return: 返回店铺的基本信息
        """
        data = {'_tk_': self.supplier.token,
                '_deviceId_': self.supplier.device_id,
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

    # def update_shop_info(self, shop):
    #     """
    #     张鹏飞:更新店铺信息
    #     :return:
    #     """
    #     bind_data = {"_tk_": self.supplier.token,
    #                  "_deviceId_": self.supplier.device_id,
    #                  "sellerId": self.supplier.user_id,
    #                  "name": shop.name,
    #                  "shopId": self.supplier.channel_shop_id,
    #                  # "mobile": shop.mobile,
    #                  "contact": shop.contact,
    #                  "avatar": shop.avatar}
    #     response = self.request.post(url=self.hosts['MS_SHOP'] + '/mobile/shop/update-shop-info',
    #                                  data=bind_data)
    #     json_response = json.loads(response)
    #     update_shop_info = self.tool.ms_query_update_shop_info_by_seller_id(self.supplier.user_id)[0]
    #     if json_response["status"] == "OK":
    #         assert update_shop_info["name"] == bind_data['name']
    #         # assert update_shop_info["mobile"] == bind_data['mobile']
    #         assert update_shop_info["contact"] == bind_data['contact']
    #     elif json_response["status"] == "ERROR":
    #         raise Exception("status返回ERROR")
    #     else:
    #         raise Exception("status未返回OK或ERROR")
    #     return json_response["content"]

    def product_save(self, product):
        """
        上架新商品
        :param product: 传入商品对象，Product.py
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "parentId": product.parent_category_id,
                     "categoryId": product.category_id,
                     "name": product.name,
                     "shopId": product.supplier_shop_id,
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
            self.supplier.user_id).get('content').get('shopId'))
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def add_address(self, shop):
        """
        新增地址
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "_language_": 'zh',
                     "addressId":shop.addressId,
                     "shopId": shop.shopId,
                     "lng": shop.lng,
                     "lat": shop.lat,
                     "province": shop.province,
                     "city": shop.city,
                     "area": shop.area,
                     "address": shop.address}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/address/add", data=bind_data)
        add_address_info = self.tool.ms_query_latest_address_info_by_shop_id(self.get_shop_id_by_type(
            self.supplier.user_id).get('content').get('shopId'))[0]
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def switch_status(self, shop_id, status=10, check="true"):
        """
        更新店铺营业状态（10 营业中 20 休息）
        :return:
        """
        bind_data = {"_tk_": self.supplier.token,
                     "_deviceId_": self.supplier.device_id,
                     "shopId": shop_id,
                     "status": status,
                     "check": check}
        response = self.request.post(url=self.hosts['MS_SHOP'] + "/mobile/shop/switch-status", data=bind_data)
        json_response = json.loads(response)
        update_shop_info = self.tool.ms_query_update_shop_info_by_seller_id(self.supplier.user_id)[0]
        if json_response["status"] == "OK":
            assert update_shop_info["status"] == status
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response["content"]

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
        data = {'_tk_': self.supplier.token, '_deviceId_': self.supplier.device_id,
                'receiver': receiver, 'contactNumber': contact_number, 'province': province, 'city': city,
                'address': address, 'doorNumber': door_number, 'lng': lng, 'lat': lat, 'isDefault': is_default}
        response = self.request.post(url=self.hosts['MS_USER'] + '/mobile/address/add', data=data)
        print(response)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def history_address(self, shop_id):
        """
        获取历史地址列表
        :return:
        """
        data = {"_tk_": self.supplier.token,
                "_deviceId_": self.supplier.device_id,
                "shopId": shop_id
                }
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/address/history', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response


if __name__ == '__main__':
    from backend.User import User
    seller = User("18382373185")
    da = SupplierAction(seller)
    # da._mobile_supply_channel_order_list(20, 1, 2)
    # da._mobile_supply_channel_order_detail('JDSP2018121911181295506002')
    # da._mobile_supply_channel_order_refuse("JDSP2018121911191917806004")
    # da._mobile_supply_channel_order_agree("JDSP2018121911181295506002")
    # da._mobile_supply_channel_order_finish_send("JDSP2018121914191079106010")
    # da._mobile_supply_channel_order_pending_count(146)
    # da.supp_upload('E:/MiaoShuAutoTest31/utils/picture/1.jpeg', '1.jpeg')
    # da.supp_update(da.supp_upload('./../actions/1.jpeg', '1.jpeg'),
    #                da.supp_upload('./../actions/1.jpg', '1.jpg'))
    # da.supp_get_fail()
    #seller.change_identity(3)
    # da.shop_get()
    # da.upload_avatar('E:/MiaoShuAutoTest31/utils/picture/1.jpeg', '1.jpeg')
    # da.shop_send_verify_code("13400000000")
    # da.shop_update_mobile("13400000000")
    # da.update_shop_info("路漫漫", "13400000000", "么西么西",
    #                     'E:/MiaoShuAutoTest31/utils/picture/3.jpeg', '3.jpeg')
    # da.update_address(41, 4101, 2501, "银泰城2号门")
    # da.switch_status(10)
    # da.category_list_all()
    # da.category_list(0)
    # print(da.category_list(0)[3]["id"])
    # print(da.category_list(da.category_list(0)[3]["id"])[0]["id"])
    # da.store_unit_list()
    # da.freight_template_all()
    # da.freight_template_add("绿植模板咿呀哟", 500, 326, 200, 10, 10)
    # da.freight_template_delete(da.freight_template_all()[0]["id"])
    # da.freight_template_edit(da.freight_template_all()[1]["id"], title="草莓专属模板", freigh_per_km=100)
    # da.freight_template_get(da.freight_template_all()[1]["id"])
    # da.upload_img('E:/MiaoShuAutoTest31/utils/picture/4.jpg', '4.jpg')
    # da.status_list()
    # da.product_save(da.category_list(0)[3]["id"], da.category_list(da.category_list(0)[3]["id"])[0]["id"], "牡丹",
    #                 da.store_unit_list(), "国花真呀嘛真美丽", 35, 161, -1, da.status_list()[1]["id"],
    #                 'E:/MiaoShuAutoTest31/utils/picture/4.jpg', '4.jpg')
    # da.product_list()
    # print(da.product_list()[0]["pcode"])
    #da.product_find(da.product_list()[0]["pcode"])
    # da.status_update(da.product_list()[0]["pcode"], 20)
    # da.status_update(da.product_list()[1]["pcode"], 30)
    # da.status_update(da.product_list()[0]["pcode"], 10)
    # da.product_update(0, price=35)
    # da.store_list()
    # da.store_update('[{"pcode":%s, "store":67},{"pcode": %s, "store":68}]'
    #                 % (str(da.store_list()[0]["pcode"]), str(da.store_list()[1]["pcode"])))
    # da.supp_order_list()
    # da.get_shop_id_by_type(1210)
    da.history_address(146)
