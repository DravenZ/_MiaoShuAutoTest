#! /usr/bin/env python 3
# -*- coding: UTF-8 -*-

"""
__author__ = 'guochao.fu'
__date__ = '2018/12/15'
"""

from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json



class Stock(object):
    def __init__(self, product):
        self.log = Log('Stock')
        self.tool = Tool()
        self.request = Request()
        self.ps = 10
        self.product = product



    def common_product_upload_img(self):
        '''
        guochao.fu:商品头图上传
        :return:
        '''
        response = self.request.post_file(url='http://dev.ms.product.sjnc.com/common/product/upload-img',
                                          file_path='./Picture/1.png',
                                          file_key='file')
        json_response = json.loads(response)
        print(json_response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def common_product_upload_info_img(self):
        '''
        guochao.fu:商品详情图片上传
        :return:
        '''
        response = self.request.post_file(url='http://dev.ms.product.sjnc.com/common/product/upload-img',
                                          file_path='./Picture/1.png',
                                          file_key='file')
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_category_list(self, categoryId, search):
        '''
        guochao.fu:根据条件查询分类列表
        :param categoryId:
        :param search:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'categoryId': categoryId, 'search': search}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/category/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_category_list_all(self):
        '''
        guochao.fu:所有分类列表
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/category/list-all', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_product_find(self, pcode):
        '''
        guochao.fu:商品详情
        :param pcode:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/find', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_product_list(self, shopId, serviceType, parentId, categoryId, status, sort, search, pn, ps):
        '''
        guochao.fu:根据条件查询商品列表
        :param shopId:
        :param serviceType:
        :param parentId:
        :param categoryId:
        :param status:
        :param sort:
        :param search:
        :param pn:
        :param ps:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId, 'serviceType': serviceType, 'parentId': parentId, 'categoryId': categoryId, 'status': status, 'sort': sort, 'search': search, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_product_save(self, parentId, categoryId, name, shopId, price, storeUnitId, content, store, freightId, status, serviceType, imgs,infoImgs):
        '''
        guochao.fu:上传新商品
        :param parentId:
        :param categoryId:
        :param name:
        :param shopId:
        :param price:
        :param storeUnitId:
        :param content:
        :param store:
        :param freightId:
        :param status:
        :param serviceType:
        :param imgs:
        :param infoImgs:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'parentId': parentId, 'categoryId': categoryId, 'name': name, 'shopId': shopId, 'price': price, 'storeUnitId': storeUnitId, 'content': content, 'store': store, 'freightId': freightId, 'status': status, 'serviceType': serviceType, 'imgs': imgs,'infoImgs':infoImgs}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/save', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_product_status_list(self):
        '''
        guochao.fu:商品状态列表
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/status-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_product_status_update(self, pcode, operation):
        '''
        guochao.fu:商品上架/下架/删除
        :param pcode:
        :param operation:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode, 'operation': operation}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/status-update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_product_store_list(self, shopId, parentId, categoryId, search, pn, ps):
        '''
        guochao.fu:库存列表
        :param shopId:
        :param parentId:
        :param categoryId:
        :param search:
        :param pn:
        :param ps:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId, 'parentId': parentId, 'categoryId': categoryId, 'search': search, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/store-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_product_store_update(self, stores):
        '''
        guochao.fu:库存更新
        :param stores:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'stores': stores}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/store-update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_store_unit_list(self):
        '''
        guochao.fu:查询库存单位列表
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/store-unit/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_freightTemplate_add(self, shopId,  title, freighPerKm, freePrice, freeDistance, freePriceStatus, freeDistanceStatus):
        '''
        guochao.fu:新建运费模板
        :param shopId:
        :param id:
        :param title:
        :param freighPerKm:
        :param freePrice:
        :param freeDistance:
        :param freePriceStatus:
        :param freeDistanceStatus:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId, 'title': title, 'freighPerKm': freighPerKm, 'freePrice': freePrice, 'freeDistance': freeDistance, 'freePriceStatus': freePriceStatus, 'freeDistanceStatus': freeDistanceStatus}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_freightTemplate_all(self, shopId):
        '''
        guochao.fu:获取全部模板
        :param shopId:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/all', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_freightTemplate_delete(self, id, shopId):
        '''
        guochao.fu:删除模板
        :param id:
        :param shopId:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'id': id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/delete', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_freightTemplate_edit(self, shopId, id, title, freighPerKm, freePrice, freeDistance, freePriceStatus, freeDistanceStatus):
        '''
        guochao.fu:修改运费模板
        :param shopId:
        :param id:
        :param title:
        :param freighPerKm:
        :param freePrice:
        :param freeDistance:
        :param freePriceStatus:
        :param freeDistanceStatus:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId, 'id': id, 'title': title, 'freighPerKm': freighPerKm, 'freePrice': freePrice, 'freeDistance': freeDistance, 'freePriceStatus': freePriceStatus, 'freeDistanceStatus': freeDistanceStatus}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

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
        response = self.request.post(url='http://192.168.62.253:31009/mobile/shop/get/%s' % str(shop_id),
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


    def mobile_freightTemplate_get_id(self, id):
        '''
        guochao.fu:获取单个运费模板
        :param id:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/get/%s' % str(id), data=data)
        json_response = json.loads(response)
        print(json_response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_suppler_address_add(self, address_id, shop_id, lng, lat, province, city, area, address):
        """
        guochao.fu::新增基地地址
        :param addressId:地址ID，新增修改，不用填写
        :param shopId:店铺id
        :param lng:
        :param lat:
        :param province:
        :param city:
        :param area:区域（如：高新区）
        :param address:地址（如：软件园E3-9楼）
        :return: content": true,"status": "OK"
        """
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'addressId': address_id, 'shopId':shop_id,
                'lng': lng, 'lat': lat, 'province': province, 'city': city, 'area': area, 'address': address}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/address/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_suppler_address_history(self, shop_id):
        """
        杨露瑶:获取历史接单点地址列表
        :param shop_id:
        :return: 返回店铺接点单历史地址
        """
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/address/history', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_add(self, user_id, receiver, contact_number, province, city, address, door_number, lng, lat, is_default):
        '''
        guochao.fu:苗叔添加收货地址
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
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'userId': user_id, 'receiver': receiver,
                'contactNumber': contact_number, 'province': province, 'city': city, 'address': address,
                'doorNumber': door_number, 'lng': lng, 'lat': lat, 'isDefault': is_default}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/address/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def cart_purchase(self, pro_code, amount, address_id):
        '''
        guochao.fu:苗叔立即购买基地商品
        :param pro_code:
        :param amount:
        :param address_id:
        :return:
        '''
        data = {
            '_tk_': self.product.token,
            '_deviceId_': self.product.device_id,
            'pcode': pro_code,
            'amount': amount,
            'addressId': address_id
        }
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/purchase',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_cart_add(self, pcode, amount):
        '''
        guochao.fu:苗叔添加购物车
        :param pcode:
        :param amount:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode, 'amount': amount}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cart_balance(self, cartIds, addressId):
        '''
        guochao.fu:苗叔购物车结算
        :param cartIds:
        :param addressId:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'cartIds': cartIds, 'addressId': addressId}
        response = self.request.post(url='http://dev.ms.cart.sjnc.com/mobile/cart/balance', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_category_page(self, search, pn, ps):
        '''
        guochao.fu:根据关键字查找二级分类列表-分页
        :param search:
        :param pn:
        :param ps:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'search': search, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/category/page', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")


    def _mobile_product_detail(self, pcode):
        """
        guochao.fu:买家查看商品详情
        :param pcode:
        :return:
        """
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_product_shop_products(self, shopId):
        """
        guochao.fu:买家查询店铺所有商品
        :param shopId:
        :return:
        """
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/shop-products', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_product_update(self, pcode, parentId, categoryId, name, shopId, price, storeUnitId, content, store, freightId, status, serviceType, imgs):
        '''
        guochao.fu:苗叔更新商品
        :param pcode:
        :param parentId:
        :param categoryId:
        :param name:
        :param shopId:
        :param price:
        :param storeUnitId:
        :param content:
        :param store:
        :param freightId:
        :param status:
        :param serviceType:
        :param imgs:
        :param infoImgs:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode, 'parentId': parentId, 'categoryId': categoryId, 'name': name, 'shopId': shopId, 'price': price, 'storeUnitId': storeUnitId, 'content': content, 'store': store, 'freightId': freightId, 'status': status, 'serviceType': serviceType, 'imgs': imgs}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")


    def _mobile_delivery_update(self, shop_id, freeDistance, perKmPrice, freePrice):
        '''
        guochao.fu:更新配送策略
        :param shop_id:
        :param freeDistance:
        :param perKmPrice:
        :param freePrice:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shop_id, 'freeDistance': freeDistance, 'perKmPrice': perKmPrice, 'freePrice': freePrice}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/delivery/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_category_add(self, type, name, categoryStatus, parentId, tags):
        '''
        guochao.fu:新增二级分类
        :param type:
        :param name:
        :param categoryStatus:
        :param orders:
        :param parentId:
        :param tags:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'type': type, 'name': name, 'categoryStatus': categoryStatus,  'parentId': parentId, 'tags': tags}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/category/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_freightTemplate_save_or_update(self, shopId,  title, freighPerKm, freePrice, freeDistance, freePriceStatus, freeDistanceStatus):
        '''
        guochao.fu:新建/编辑运费模板【可对字段】
        :param shopId:
        :param title:
        :param freighPerKm:
        :param freePrice:
        :param freeDistance:
        :param freePriceStatus:
        :param freeDistanceStatus:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId, 'title': title, 'freighPerKm': freighPerKm, 'freePrice': freePrice, 'freeDistance': freeDistance, 'freePriceStatus': freePriceStatus, 'freeDistanceStatus': freeDistanceStatus}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_add(self, mobile, real_name, role, email):
        '''
        guochao.fu:新建后台账号
        :param mobile:
        :param real_name:
        :param role:
        :param email:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'mobile': mobile, 'realName': real_name,
                'role': role, 'email': email}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_del(self, user_id):
        '''
        guochao.fu:删除后台账号
        :param user_id:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_edit(self, user_id, mobile, real_name, role, email):
        '''
        guochao.fu:编辑后台账号
        :param user_id:
        :param mobile:
        :param real_name:
        :param role:
        :param email:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'userId': user_id, 'mobile': mobile,
                'realName': real_name, 'role': role, 'email': email}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_freeze(self, user_id, reason):
        '''
        guochao.fu:冻结后台运维账号
        :param user_id:
        :param reason:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'userId': user_id, 'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/freeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_unfreeze(self, user_id, reason):
        '''
        guochao.fu:解冻后台运维账号
        :param user_id:
        :param reason:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'userId': user_id, 'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/unfreeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_get_basic_info(self):
        '''
         guochao.fu:获取当前登录后台用户基础信息
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/get-basic-info', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_list(self, pn, ps, status=None, role=None, real_name=None, email=None, mobile=18736513665):
        '''
        guochao.fu:查询运营后台账号列表
        :param pn:
        :param ps:
        :param status:
        :param role:
        :param real_name:
        :param email:
        :param mobile:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'pn': pn, 'ps': ps, 'status': status,
                'role': role, 'realName': real_name, 'email': email, 'mobile': mobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_reset_password(self, user_id):
        '''
        guochao.fu:重置后台帐号密码
        :param user_id:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/reset-password', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_save(self, id):
        """
        guochao.fu:审核保存
        :param id:
        :param positive:
        :param negative:
        :param name:
        :param gender:
        :param birthday:
        :param id_num:
        :param province:
        :param city:
        :param district:
        :param address:
        :return:
        """
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'id': id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/save', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_log_auth_log(self, pn, ps, operate_role, user_id):
        '''
        guochao.fu:获取用户审核日志
        :param pn:
        :param ps:
        :param operate_role:
        :param user_id:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'pn': pn, 'ps': ps,
                'operateRole': operate_role, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/log/auth-log', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_log_user_log(self, pn, ps, user_id):
        '''
        guochao.fu:获取账号操作日志
        :param pn:
        :param ps:
        :param user_id:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'pn': pn, 'ps': ps, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/log/user-log', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_service_get_accid(self):
        '''
        guochao.fu:登录后获取自身IM账号
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/service/get-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_service_update_service_status(self, service_id, service_status):
        '''
        guochao.fu:在线诊断-客服上线下线状态修改
        :param service_id:
        :param service_status:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'serviceId': service_id,
                'serviceStatus': service_status}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/service/update-service-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_count(self):
        '''
        guochao.fu:用户分类数量统计
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_default_head_img(self, head_img, head_img_type):
        '''
        guochao.fu:默认用户头像上传（请勿随意使用）
        :param head_img:
        :param head_img_type:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'headImg': head_img,
                'headImgType': head_img_type}
        # response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/default-head-img', data=data)
        response = self.request.post_file(url='http://dev.ms.user.sjnc.com/admin/user/default-head-img?'
                                              '_tk_=%s&_deviceId_=%s'
                                              % (self.product.token, self.product.deviceId),
                                          file_key='headImg', file_path=head_img, data_dict=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_detail(self, user_id):
        '''
        guochao.fu:用户账号详情
        :param user_id:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_freeze(self, user_id, role_type, reason):
        '''
        guochao.fu:冻结角色
        :param user_id:
        :param role_type:
        :param reason:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'userId': user_id, 'roleType': role_type,
                'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/freeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_unfreeze(self, user_id, role_type, reason):
        '''
        guochao.fu:解冻角色
        :param user_id:
        :param role_type:
        :param reason:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'userId': user_id, 'roleType': role_type,
                'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/unfreeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_list(self, pn, ps, status, nickname=None, role=None, mobile=None):
        '''
        guochao.fu:查询用户账号列表
        :param pn:
        :param ps:
        :param status:
        :param nickname:
        :param role:
        :param mobile:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'pn': pn, 'ps': ps, 'status': status,
                'nickname': nickname, 'role': role, 'mobile': mobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_update_mobile(self, old_mobile, new_mobile):
        '''
        guochao.fu:为销号手机用户更改手机号
        :param old_mobile:
        :param new_mobile:
        :return:
        '''
        data = {'_tk_': self.product.token, '_deviceId_': self.product.deviceId, 'oldMobile': old_mobile,
                'newMobile': new_mobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

        def _mobile_address_history(self, shop_id):
            """
            杨露瑶:获取历史接单点地址列表
            :param shop_id:
            :return: 返回店铺接点单历史地址
            """
            data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id}
            response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/address/history', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        def _mobile_product_detail(self, pcode):
            """
            买家查看商品详情
            :param pcode:
            :return:
            """
            data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode}
            response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/detail', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")


if __name__ == '__main__':
    # 苗叔,基地登录
    from backend.User import User
    seller_tmp = User("18382373185")
    seller = Stock(seller_tmp)
    print(seller_tmp.user_id)
    # 以下为后台admin登录 18736513665 61918v
    from backend.Session import EmployeeSession
    service_user1=EmployeeSession("admin","123456")
    service_user = Stock(service_user1)

    # 以下为苗叔和基地库存

    # 商品头图上传---已通
    # seller.common_product_upload_img()
    # 商品详情图片上传---已通
    # seller.common_product_upload_info_img()
    #根据条件查询分类列表---已通
    # seller.mobile_category_list(0,"大")
    # 所有分类列表---已通
    # seller.mobile_category_list_all()
    # 商品详情---已通
    # seller.mobile_product_find("306970000701")
    #根据条件查询商品列表---已通
    # seller. mobile_product_list(144, 20, 0, 0, 0, 0, " ", 1, 20)
    # 苗叔上传新商品---已通
    # seller.mobile_product_save(60, 66, "渠道端苹果", 144, 15, 43, "冻结后添加的大苹果", 111, 2, 10, 20, 'http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-product/product-img/1544861185297.png')
    # seller.mobile_product_save(60, 66, "12.18,运费模板id为2的苹果", 144, 15, 43, "12.18添加测试购买", 500, 2, 10, 20,'http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-product/product-img/1544861185297.png')
    # seller.mobile_product_save(60, 66, "详情页图片", 144, 15, 43, "详情图片为草莓", 500, 2, 10, 20,'http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-product/product-img/1545293199735.jpg','[{"url":"http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-product/product-img/1545293199735.jpg","size":"56,89"}]')
    # 基地账号给苗叔添加商品:seller.mobile_product_save(60,66,"基地账号添加苗叔商品",144,15, 43, "添加成功就是错误的", 200, 2, 10, 20,'http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-product/product-img/1544861185297.png')
    # 基地上传商品---已通
    # 绿植--绿萝seller.mobile_product_save(58, 62, "基地绿萝", 146, 15, 43, "基地添加商品,名字为绿萝", 9999, -1, 10, 30, 'http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-product/product-img/1544861185297.png')
    # 蔬菜--白菜seller.mobile_product_save(59, 63, "基地白菜", 146, 15, 43, "基地添加蔬菜,名字为白菜", 9999, -1, 10, 30,'http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-product/product-img/1544861185297.png')
    # seller.mobile_product_save(69, 70, "基地西红柿", 146, 15, 43, "基地添加果蔬,名字为西红柿", 9999, -1, 10, 30,'http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-product/product-img/1544861185297.png')
    # 商品状态列表---已通
    # seller.mobile_product_status_list()
    # 商品上架/下架/删除---已通
    # seller.mobile_product_status_update(205963000380, 10)
    #库存列表---已通
    # seller.mobile_product_store_list(144, 0, 0, "菜", 1, 20)
    #库存更新---已通
    # seller.mobile_product_store_update('[{"pcode":205963000385,"store":888}]')
    # 查询库存单位列表---已通
    # seller.mobile_store_unit_list()
    # 新建运费模板---已通
    # seller.mobile_freightTemplate_add(144, "测试模板1", 3, 3, 500, 10, 20)
    # seller.mobile_freightTemplate_add(144, "测试模板2", 5, 500, 500, 10, 20)
    # seller.mobile_freightTemplate_add(144, "测试模板3", 5, 500, 500, 10, 20)
    # 获取全部模板---已通
    # seller.mobile_freightTemplate_all(144)
    # 删除模板---已通
    # seller.mobile_freightTemplate_delete(3, 144)
    # 修改运费模板---已通
    # seller.mobile_freightTemplate_edit(144, 2, "苗叔专用勿删", 55, 88, 500, 10, 30)
    # 获取单个运费模板--已通
    # seller.mobile_freightTemplate_get_id(2)
    # 新建/编辑运费模板【可对字段】---已通
    # seller.mobile_freightTemplate_save_or_update(144, "save_or_update接口", 300, 300, 5000, 10, 20)
    # 基地添加收货地址
    # seller._mobile_suppler_address_add('', '146', '104.059', '30.5408', '41', '4101', '高新区', '银泰城基地据点')
    # 基地获取历史基地地址
    # seller._mobile_suppler_address_history(146)


    # 以下为苗叔添加购物车,结算购物车

    # 苗叔添加收货地址--已通
    # seller._mobile_address_add(1213,"大火车","18582549267",41,4101,"高新区苗叔收货地址,勿改谢谢","铁皮村 888号",104.06,30.54,1)
    # 苗叔直接购买基地商品--已通
    # seller.cart_purchase(306066000446,10001,151)
    # 苗叔添加购物车--已通
    # seller. _mobile_cart_add(306066000446,50)
    # seller._mobile_cart_add(306066000446, 99999)
    # seller._mobile_cart_add(306066000446, 33)
    # 苗叔购物车结算----已通
    # seller._mobile_cart_balance(19,151)
    # 根据关键字查找二级分类列表---已通
    # seller._mobile_category_page("花",1,20)
    # 买家查看商品详情---已通
    # seller._mobile_product_detail(206066000468)
    # seller._mobile_cart_add(seller._mobile_product_detail(206066000468)["content"]["pcode"],1)
    # result=seller._mobile_cart_add(seller._mobile_product_detail(206066000468)["content"]["pcode"],1)
    # 买家查询店铺所有商品---已通
    # seller._mobile_product_shop_products(144)
    # 苗叔更新商品---已通
    # seller._mobile_product_update(206066000398,60,67,"更改为香蕉的苹果",144,100,41,"原为水果下的苹果,更改为水果下的香蕉",500,2,10,20,'http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-product/product-img/1544861185297.png')
    # 更新配送策略---本期不用了
    # seller._mobile_delivery_update(144,5000,500,50000)


    # 以下为后台运营部分
    # 苗叔账号:user_id=1213  shop_id=144  mobile=18582549267
    # 基地账号:user_id=1210  shop_id=146  mobile=18382373185
    # 后台账号:user_id=1256  mobile=18736513665  password=61918v
    # 后台添加用户---已通/手机格式错误,为空,已经注册的手机号码,邮箱非本公司格式---12.19
    # service_user._admin_backstage_add("18582549266","后台添加测试用户",1,"1953270624@qq.com")
    # service_user._admin_backstage_add("18736513666", "后台添加测试用户", 1, "guochaoa.fu@worldfarm.com")
    # service_user._admin_backstage_add("18736513667", "测试删除的账号", 1, "guochaob.fu@worldfarm.com")
    # service_user._admin_backstage_add("18736513669", "测试冻结的账号", 1, "freeze.fu@worldfarm.com")
    # service_user._admin_backstage_add("18736513652", "本地化测试", 1, "@worldfarm.com")
    # 删除后台账号---已通/多次删除同一个账号,不存在的账号
    # service_user._admin_backstage_del(1269)
    # 编辑后台账号--已通/如下场景已验证:手机号为已注册,邮箱为已注册,手机号为空
    # service_user._admin_backstage_edit(1271,"18736513651","编辑更改类型", 2, "@worldfarm.com")
    # 冻结后台账号---已通
    # service_user. _admin_backstage_freeze(1256,"测试冻结后台账号功能")
    # 解冻后台运维账户---已通
    # service_user._admin_backstage_unfreeze(1256,"测试解冻")
    # 获取当前登录后台用户基础信息---已通
    # service_user._admin_backstage_get_basic_info()
    # 查询运营后台账号列表---已通
    # service_user._admin_backstage_list(1,5)
    # 重置后台帐号密码---已通
    # service_user._admin_backstage_reset_password(1256)
    # 审核保存---已通
    # service_user._admin_audit_save(144)
    # 获取用户审核日志---已通
    # service_user._admin_log_auth_log(1,20,2,1213)
    # 获取账号操作日志---已通
    # service_user._admin_log_user_log(1,20,1256)
    # 登录后获取自身IM账号---已通
    # seller._admin_service_get_accid()
    # service_user._admin_service_get_accid()
    # 在线诊断-客服上线下线状态修改---已通
    # service_user._admin_service_update_service_status(1256,0)
    # 用户分类数量统计---已通
    # service_user._admin_user_count()
    # 默认用户头像上传（请勿随意使用）---已通
    # service_user._admin_user_default_head_img('./../Picture/doctor.jpg',3)
    # 用户账号详情---已通/查询非后台人员-----12.20
    # service_user._admin_user_detail(1251)
    # 冻结角色---已通/消费者，苗叔，基地三种已通
    # service_user._admin_user_freeze(1213,1,"冻结消费者角色测试")
    # service_user._admin_user_freeze(1213, 2, "冻结苗叔角色测试")
    # service_user._admin_user_freeze(1210, 3, "冻结基地角色测试")
    # 解冻角色---已通/消费者，苗叔，基地三种已通
    # service_user._admin_user_unfreeze(1213,1,"解冻消费者角色测试")
    # service_user._admin_user_unfreeze(1213, 2, "解冻渠道端角色测试")
    # service_user._admin_user_unfreeze(1210, 3, "冻结基地角色测试")
    # 查询用户账号列表---已通
    # service_user._admin_user_list(1,20,2)
    # 为销号手机用户更改手机号---已通
    # service_user._admin_user_update_mobile("18582549222","18582549267")





    # 后台新增商品一级分类
    # seller._admin_category_add(2, "测试一级分类", 10, 69, "丰富的维C")
    # 后台新增商品二级分类---已通
    # seller._admin_category_add(2,"西红柿",10,69,"丰富的维C")
