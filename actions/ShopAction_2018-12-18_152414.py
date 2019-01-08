# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class shopAction(object):

    def __init__(self, shop):
        self.log = Log('shop')
        self.request = Request()
        self.shop = shop

    def _admin_report_shop_business_report(self, begin, end):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'begin': begin, 'end': end}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/admin/report/shop-business-report', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_shop_count(self):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/admin/report/shop-count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_address_add(self, addressId, shopId, lng, lat, province, city, area, address):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'addressId': addressId, 'shopId': shopId, 'lng': lng, 'lat': lat, 'province': province, 'city': city, 'area': area, 'address': address}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/address/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_freightTemplate_list_by_ids(self, ids):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'ids': ids}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/freightTemplate/list-by-ids', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_freightTemplate_list_by_shopid(self, shopId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/freightTemplate/list-by-shopid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shippingAddress_detail(self, addressId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'addressId': addressId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shippingAddress/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shippingAddress_get_default(self, userId, lat, lng):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'userId': userId, 'lat': lat, 'lng': lng}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shippingAddress/get-default', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_calculate_freight(self, lng, lat, sellerId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'lng': lng, 'lat': lat, 'sellerId': sellerId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/calculate-freight', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_check_{shopId}(self, shopId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/check/{shopId}', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_close_shop(self, sellerId, type):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': sellerId, 'type': type}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/close-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_find_nearby_shop(self, lng, lat, distance, pn, ps):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'lng': lng, 'lat': lat, 'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/find-nearby-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_freeze_shop(self, sellerId, type):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': sellerId, 'type': type}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/freeze-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_get_by_seller(self, sellerId, type):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': sellerId, 'type': type}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/get-by-seller', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_get_{shopId}(self, shopId, isSimpleInfo):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId, 'isSimpleInfo': isSimpleInfo}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/get/{shopId}', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_init_shop(self, sellerId, mobile, type):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': sellerId, 'mobile': mobile, 'type': type}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/init-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_list_for_distance(self, ids, lng, lat):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'ids': ids, 'lng': lng, 'lat': lat}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/list-for-distance', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_list_ids(self, shopIds):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopIds': shopIds}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/list-ids', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_list_sellers_and_type(self, sellers, type):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellers': sellers, 'type': type}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/list-sellers-and-type', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_thirty_days_order_sta(self, shopId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/thirty-days-order-sta', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_add(self, addressId, shopId, lng, lat, province, city, area, address):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'addressId': addressId, 'shopId': shopId, 'lng': lng, 'lat': lat, 'province': province, 'city': city, 'area': area, 'address': address}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/address/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_history(self, shopId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/address/history', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_delivery_update(self, shopId, freeDistance, perKmPrice, freePrice):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId, 'freeDistance': freeDistance, 'perKmPrice': perKmPrice, 'freePrice': freePrice}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/delivery/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_add(self, shopId, id, title, freighPerKm, freePrice, freeDistance, freePriceStatus, freeDistanceStatus):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId, 'id': id, 'title': title, 'freighPerKm': freighPerKm, 'freePrice': freePrice, 'freeDistance': freeDistance, 'freePriceStatus': freePriceStatus, 'freeDistanceStatus': freeDistanceStatus}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_all(self, shopId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/all', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_delete(self, id, shopId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'id': id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/delete', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_edit(self, shopId, id, title, freighPerKm, freePrice, freeDistance, freePriceStatus, freeDistanceStatus):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId, 'id': id, 'title': title, 'freighPerKm': freighPerKm, 'freePrice': freePrice, 'freeDistance': freeDistance, 'freePriceStatus': freePriceStatus, 'freeDistanceStatus': freeDistanceStatus}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_get_{id}(self, id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/get/{id}', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_save_or_update(self, shopId, id, title, freighPerKm, freePrice, freeDistance, freePriceStatus, freeDistanceStatus):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId, 'id': id, 'title': title, 'freighPerKm': freighPerKm, 'freePrice': freePrice, 'freeDistance': freeDistance, 'freePriceStatus': freePriceStatus, 'freeDistanceStatus': freeDistanceStatus}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/save-or-update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_find_nearby_shop(self, lng, lat, distance, pn, ps):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'lng': lng, 'lat': lat, 'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/find-nearby-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_get(self, shopId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/get', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_get_by_type(self, sellerId, type):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': sellerId, 'type': type}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/get-by-type', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_get_{id}(self, id, lng, lat):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'id': id, 'lng': lng, 'lat': lat}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/get/{id}', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_refreshPVUV_{shopId}_{deviceId}(self, shopId, deviceId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId, 'deviceId': deviceId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/refreshPVUV/{shopId}/{deviceId}', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_search(self, keyword, lng, lat, pn, ps):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'keyword': keyword, 'lng': lng, 'lat': lat, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/search', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_send_verify_code(self, mobile):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'mobile': mobile}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/send-verify-code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_server_close_plant_server(self):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/server/close-plant-server', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_server_close_upkeep_server(self):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/server/close-upkeep-server', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_server_open_plant_server(self):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/server/open-plant-server', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_server_open_upkeep_server(self):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/server/open-upkeep-server', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_server_server(self, type, status):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'type': type, 'status': status}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/server/server', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_switch_status(self, status, check, shopId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'status': status, 'check': check, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/switch-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_update_mobile(self, mobile, verifyCode, shopId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'mobile': mobile, 'verifyCode': verifyCode, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_update_shop_info(self, shopId, sellerId, name, mobile, contact, avatar):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId, 'sellerId': sellerId, 'name': name, 'mobile': mobile, 'contact': contact, 'avatar': avatar}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/update-shop-info', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_upload_avatar(self, avatar):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'avatar': avatar}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/upload-avatar', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supplier_update_address(self, sellerId, province, city, area, areaName, address, lng, lat):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': sellerId, 'province': province, 'city': city, 'area': area, 'areaName': areaName, 'address': address, 'lng': lng, 'lat': lat}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/supplier/update-address', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_report_shop_seles_report(self, shopId, begin, end):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shopId, 'begin': begin, 'end': end}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/web/report/shop-seles-report', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
