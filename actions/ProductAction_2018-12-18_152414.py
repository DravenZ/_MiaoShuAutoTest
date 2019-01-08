# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class productAction(object):

    def __init__(self, product):
        self.log = Log('product')
        self.request = Request()
        self.product = product

    def _admin_category_add(self, type, name, categoryStatus, orders, parentId, tags):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'type': type, 'name': name, 'categoryStatus': categoryStatus, 'orders': orders, 'parentId': parentId, 'tags': tags}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/category/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_category_del(self, type, id):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'type': type, 'id': id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/category/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_category_detail(self, type, id):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'type': type, 'id': id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/category/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_category_edit(self, type, id, name, categoryStatus, orders, parentId, tags):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'type': type, 'id': id, 'name': name, 'categoryStatus': categoryStatus, 'orders': orders, 'parentId': parentId, 'tags': tags}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/category/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_category_list(self, type, firstCategoryId, secondCategoryStatus, name, pn, ps):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'type': type, 'firstCategoryId': firstCategoryId, 'secondCategoryStatus': secondCategoryStatus, 'name': name, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/category/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_category_update_status(self, type, id, categoryStatus):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'type': type, 'id': id, 'categoryStatus': categoryStatus}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/category/update-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_all_store_stats(self):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/report/all-store-stats', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_category_sales_stats(self, start, end, serviceType, topNum):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'start': start, 'end': end, 'serviceType': serviceType, 'topNum': topNum}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/report/category-sales-stats', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_category_store_stats(self):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/report/category-store-stats', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_product_sales_stats(self, start, end, shopId, topNum):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'start': start, 'end': end, 'shopId': shopId, 'topNum': topNum}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/report/product-sales-stats', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_store_unit_add(self, name):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'name': name}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/store-unit/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_store_unit_del(self, id):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/store-unit/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_store_unit_detail(self, id):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/store-unit/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_store_unit_edit(self, id, name):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'id': id, 'name': name}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/store-unit/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_store_unit_list(self, pn, ps):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/admin/store-unit/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_category_shop_tags(self, shopId):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/api/category/shop-tags', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_category_shops_tags(self, shopIds):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopIds': shopIds}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/api/category/shops-tags', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_product_list(self, pcodes):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcodes': pcodes}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/api/product/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_product_list_by_freight(self, shopId, freightId):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId, 'freightId': freightId}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/api/product/list-by-freight', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_product_shop_product_amount(self, shopId, status):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId, 'status': status}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/api/product/shop-product-amount', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_product_shop_product_amount_list(self, shopIds, status):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopIds': shopIds, 'status': status}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/api/product/shop-product-amount-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_product_snapshot_list(self, snapshotIds):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'snapshotIds': snapshotIds}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/api/product/snapshot/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_product_store(self, pcode):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/api/product/store', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_product_store_operate(self, stores):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'stores': stores}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/api/product/store-operate', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _common_product_upload_img(self, file):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'file': file}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/common/product/upload-img', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _common_product_upload_info_img(self, file):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'file': file}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/common/product/upload-info-img', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_category_list(self, categoryId, search):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'categoryId': categoryId, 'search': search}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/category/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_category_list_all(self):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/category/list-all', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_category_page(self, search, pn, ps):
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
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_product_find(self, pcode):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/find', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_product_list(self, shopId, serviceType, parentId, categoryId, status, sort, search, pn, ps):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId, 'serviceType': serviceType, 'parentId': parentId, 'categoryId': categoryId, 'status': status, 'sort': sort, 'search': search, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_product_save(self, parentId, categoryId, name, shopId, price, storeUnitId, content, store, freightId, status, serviceType, imgs, infoImgs):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'parentId': parentId, 'categoryId': categoryId, 'name': name, 'shopId': shopId, 'price': price, 'storeUnitId': storeUnitId, 'content': content, 'store': store, 'freightId': freightId, 'status': status, 'serviceType': serviceType, 'imgs': imgs, 'infoImgs': infoImgs}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/save', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_product_shop_products(self, shopId):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/shop-products', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_product_status_list(self):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/status-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_product_status_update(self, pcode, operation):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode, 'operation': operation}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/status-update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_product_store_list(self, shopId, parentId, categoryId, search, pn, ps):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'shopId': shopId, 'parentId': parentId, 'categoryId': categoryId, 'search': search, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/store-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_product_store_update(self, stores):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'stores': stores}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/store-update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_product_update(self, pcode, parentId, categoryId, name, shopId, price, storeUnitId, content, store, freightId, status, serviceType, imgs, infoImgs):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id, 'pcode': pcode, 'parentId': parentId, 'categoryId': categoryId, 'name': name, 'shopId': shopId, 'price': price, 'storeUnitId': storeUnitId, 'content': content, 'store': store, 'freightId': freightId, 'status': status, 'serviceType': serviceType, 'imgs': imgs, 'infoImgs': infoImgs}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/product/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_store_unit_list(self):
        data = {'_tk_': self.product.token, '_deviceId_': self.product.device_id}
        response = self.request.post(url='http://dev.ms.product.sjnc.com/mobile/store-unit/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
