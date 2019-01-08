# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class kbmsAction(object):

    def __init__(self, kbms):
        self.log = Log('kbms')
        self.request = Request()
        self.kbms = kbms

    def _admin_config_add(self, code, key, value, description, isDelete, status):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'code': code, 'key': key, 'value': value, 'description': description, 'isDelete': isDelete, 'status': status}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/config/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_config_detail(self, id):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/config/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_config_edit(self, id, code, key, value, description, status):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id, 'code': code, 'key': key, 'value': value, 'description': description, 'status': status}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/config/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_config_list(self, code, description, pn, ps):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'code': code, 'description': description, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/config/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_config_list_config_by_code(self, code):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'code': code}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/config/list-config-by-code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_plant_disease_detail(self, id):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/plant-disease/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_plant_disease_import(self, file):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'file': file}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/plant-disease/import', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_plant_disease_list_hot(self):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/plant-disease/list-hot', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_plant_disease_name_list(self, search, pn, ps):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'search': search, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/plant-disease/name-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_plant_import(self, file):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'file': file}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/plant/import', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_resource_activity_item_add(self, type, sort, imgUrl, width, height, status, jumpUrl, startTimeStr, endTimeStr, remark):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'type': type, 'sort': sort, 'imgUrl': imgUrl, 'width': width, 'height': height, 'status': status, 'jumpUrl': jumpUrl, 'startTimeStr': startTimeStr, 'endTimeStr': endTimeStr, 'remark': remark}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/resource-activity/item/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_resource_activity_item_del(self, id):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/resource-activity/item/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_resource_activity_item_detail(self, id):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/resource-activity/item/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_resource_activity_item_edit(self, id, type, sort, imgUrl, width, height, status, jumpUrl, startTimeStr, endTimeStr, remark):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id, 'type': type, 'sort': sort, 'imgUrl': imgUrl, 'width': width, 'height': height, 'status': status, 'jumpUrl': jumpUrl, 'startTimeStr': startTimeStr, 'endTimeStr': endTimeStr, 'remark': remark}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/resource-activity/item/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_resource_activity_item_list(self, type, pn, ps):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'type': type, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/resource-activity/item/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_resource_activity_item_update_status(self, id, status):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id, 'status': status}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/resource-activity/item/update-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_upload_log_last(self, type):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'type': type}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/upload-log/last', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _common_upload_activity(self, file):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'file': file}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/common/upload-activity', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_city_list(self, pid):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'pid': pid}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/config/common/get-city-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_service_phone(self):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/config/common/get-service-phone', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_app_version_get(self, appId):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'appId': appId}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/mobile/app/version/get', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_plant_detail(self, id):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/mobile/plant/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_plant_list(self, search, pn, ps):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'search': search, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/mobile/plant/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_resource_activity_item_ms_list(self):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/mobile/resource-activity/item/ms-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_resource_activity_item_supplier_list(self):
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/mobile/resource-activity/item/supplier-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
