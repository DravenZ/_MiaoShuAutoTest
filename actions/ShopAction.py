# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from utils.Util import Redis
from backend.Tool import Tool
from utils.Log import Log
import json
from backend.User import User
 
class shopAction(object):

    def __init__(self):
        self.log = Log('shop').logger
        self.request = Request()
        self.redis = Redis()

    def set_user(self, user):
        self.shop = User(user)
        return self.shop

    # def __init__(self, shop):
    #     self.log = Log('shop')
    #     self.request = Request()
    #     self.shop = shop

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

    def _admin_shippingAddress_get(self):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/admin/shippingAddress/get', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_address_add(self, address_id, shop_id, lng, lat, province, city, area, address):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'addressId': address_id, 'shopId': shop_id,
                'lng': lng, 'lat': lat, 'province': province, 'city': city, 'area': area, 'address': address}
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

    def _api_freightTemplate_list_by_shopid(self, shop_id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/freightTemplate/list-by-shopid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shippingAddress_detail(self, address_id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'addressId': address_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shippingAddress/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shippingAddress_get_default(self, user_id, lat, lng):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'userId': user_id, 'lat': lat, 'lng': lng}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shippingAddress/get-default', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_calculate_freight(self, lng, lat, seller_id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'lng': lng, 'lat': lat, 'sellerId': seller_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/calculate-freight', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_check_shopId(self, shop_id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/check/%s' % str(shop_id), data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_close_shop(self, seller_id, type):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': seller_id, 'type': type}
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

    def _api_shop_freeze_shop(self, seller_id, type):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': seller_id, 'type': type}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/freeze-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_get_by_seller(self, seller_id, type):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': seller_id, 'type': type}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/get-by-seller', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_get_shopId(self, shop_id, isSimpleInfo):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id, 'isSimpleInfo': isSimpleInfo}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/get/%s' % str(shop_id), data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shop_init_shop(self, seller_id, mobile, type):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': seller_id, 'mobile': mobile, 'type': type}
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

    def _api_shop_thirty_days_order_sta(self, shop_id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/api/shop/thirty-days-order-sta', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_add(self, address_id, shop_id, lng, lat, province, city, area, address):
        """
        杨露瑶:新增苗叔店铺接单点
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
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'addressId': address_id, 'shopId':shop_id,
                'lng': lng, 'lat': lat, 'province': province, 'city': city, 'area': area, 'address': address}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/address/add', data=data)
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

    def _mobile_delivery_update(self, shop_id, freeDistance, perKmPrice, freePrice):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id, 'freeDistance': freeDistance, 'perKmPrice': perKmPrice, 'freePrice': freePrice}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/delivery/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_add(self, shop_id, id, title, freighPerKm, freePrice, freeDistance, freePriceStatus, freeDistanceStatus):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id, 'id': id, 'title': title, 'freighPerKm': freighPerKm, 'freePrice': freePrice, 'freeDistance': freeDistance, 'freePriceStatus': freePriceStatus, 'freeDistanceStatus': freeDistanceStatus}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_all(self, shop_id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/all', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_delete(self, id, shop_id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'id': id, 'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/delete', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_edit(self, shop_id, id, title, freighPerKm, freePrice, freeDistance, freePriceStatus, freeDistanceStatus):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id, 'id': id, 'title': title, 'freighPerKm': freighPerKm, 'freePrice': freePrice, 'freeDistance': freeDistance, 'freePriceStatus': freePriceStatus, 'freeDistanceStatus': freeDistanceStatus}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_freightTemplate_get_id(self, id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/freightTemplate/get/%s' % str(id), data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shippingAddress_add(self, shop_id, receiver, contact_number, province, city, address, door_number, lng,
                                    lat, is_default):
        """
        杨露瑶:新增苗叔收货地址
        :param shop_id:
        :param receiver:收货人
        :param contact_number:联系电话
        :param province:
        :param city:
        :param address:
        :param door_number:门牌号
        :param lng:
        :param lat:
        :param is_default:是否默认地址(1.是,0.否)
        :return:"status": "OK"
        """
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id, 'receiver': receiver,
                'contactNumber': contact_number, 'province': province, 'city': city, 'address': address,
                'doorNumber': door_number, 'lng': lng, 'lat': lat, 'isDefault': is_default}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shippingAddress/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shippingAddress_del(self, address_id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'addressId': address_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shippingAddress/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shippingAddress_edit(self, id, shop_id, receiver, contactNumber, province, city, address, doorNumber,
                                     lng, lat, isDefault):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'id': id, 'shopId': shop_id,
                'receiver': receiver, 'contactNumber': contactNumber, 'province': province, 'city': city, 'address': address, 'doorNumber': doorNumber, 'lng': lng, 'lat': lat, 'isDefault': isDefault}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shippingAddress/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shippingAddress_list(self, shop_id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shippingAddress/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shippingAddress_set_default(self, address_id, shop_id):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'addressId': address_id, 'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shippingAddress/set-default', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_find_nearby_shop(self, lng, lat, distance, pn, ps):
        """
        买家搜索店铺
        :param lng:
        :param lat:
        :param distance:
        :param pn:
        :param ps:
        :return:
        """
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'lng': lng, 'lat': lat,
                'distance': distance, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/find-nearby-shop', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_get(self, shop_id):
        """
        杨露瑶:通过当前用户，获取店铺信息
        :param shop_id:
        :return:
        """
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/get', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_get_id(self, id, lng, lat):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'id': id, 'lng': lng, 'lat': lat}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/get/%s' % str(id), data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_refreshPVUV_shopId_deviceId(self,shop_id, deviceId):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id, 'deviceId': deviceId}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/refreshPVUV/%s' % str(shop_id) % str(deviceId), data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_search(self, keyword, lng, lat, pn, ps):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'keyword': keyword, 'lng': lng, 'lat': lat,
                'pn': pn, 'ps': ps}
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

    def _mobile_shop_switch_status(self, status, shop_id, check=True):
        """
        杨露瑶:更新店铺营业状态(10营业中,20休息)
        :param status:
        :param shop_id:
        :param check:
        :return:
        """
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'status': status, 'check': check,
                'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/switch-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_update_mobile(self, mobile, shop_id):
        print(str(self.shop.user_id))
        print(str(mobile))
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'mobile': mobile,
                'verifyCode': self.redis.get('ShopManagerImpl:modify_shop_mobile:%s_%s' %(str(self.shop.user_id), str(mobile))),
                 'shopId': shop_id}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/shop/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_shop_update_shop_info(self, shop_id, seller_id, name, mobile, contact, avatar=None):
        """
        杨露瑶:更新店铺信息
        :param shop_id:
        :param seller_id:
        :param name:
        :param mobile:
        :param contact:
        :param avatar:
        :return:
        """
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id, 'sellerId': seller_id,
                'name': name, 'mobile': mobile, 'contact': contact, 'avatar': avatar}
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
        response = self.request.post_file(url='http://dev.ms.shop.sjnc.com/mobile/shop/upload-avatar',
                                          file_key="avatar", data_dict=data, file_path="./picture/%s" % avatar)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supplier_update_address(self, seller_id, province, city, area, area_name, address, lng, lat):
        """
        杨露瑶:更新供应商店铺地址
        :param seller_id:
        :param province:
        :param city:
        :param area:
        :param area_name:
        :param address:
        :param lng:
        :param lat:
        :return:
        """
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'sellerId': seller_id, 'province': province,
                'city': city, 'area': area, 'areaName': area_name, 'address': address, 'lng': lng, 'lat': lat}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/mobile/supplier/update-address', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_report_shop_seles_report(self, shop_id, begin, end):
        data = {'_tk_': self.shop.token, '_deviceId_': self.shop.device_id, 'shopId': shop_id, 'begin': begin, 'end': end}
        response = self.request.post(url='http://dev.ms.shop.sjnc.com/web/report/shop-seles-report', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")


if __name__ == '__main__':
    import inspect
    # print(shopAction.__dict__)
    # func_list = inspect.getmembers(shopAction, predicate=inspect.isfunction)
    # for a in func_list:
        # print(a[0])
        # print(eval("shopAction.%s.__doc__" % a[0]))
    from backend.User import User
    user = User(18382373185)
    sh = shopAction(user)
    # sh._mobile_shop_update_shop_info('146', '1210', '基地店铺哦', '18382373185', '不知道')
    # sh._mobile_shop_switch_status('10', '148')
    # sh._mobile_supplier_update_address('1210', '41', '4101', '410106', '软件园', '天府五街', '104.07', '30.5546')
    # sh._mobile_shop_upload_avatar('')
    # sh._mobile_shop_get('146')
    # sh._mobile_shippingAddress_add('148', '测试00', '18382373185', '41', '4101', '软件园', '901', '116.397',
    # '39.9165', '0')
    # sh._mobile_address_add('', '148', '116.397', '39.9165', '41', '4101', '高新区', '软件园3-1')
    sh._mobile_address_history('148')
    # sh._mobile_shippingAddress_list('148')
