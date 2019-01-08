# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class userAction(object):

    def __init__(self, user):
        self.log = Log('user')
        self.request = Request()
        self.user = user

    def _admin_audit_detail(self, id, userId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'userId': userId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_list(self, pn, ps, status, mobile, nickname, applyRole):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'status': status, 'mobile': mobile, 'nickname': nickname, 'applyRole': applyRole}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_pass(self, id, userId, positive, negative, name, gender, birthday, idNum, province, city, district, address):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'userId': userId, 'positive': positive, 'negative': negative, 'name': name, 'gender': gender, 'birthday': birthday, 'idNum': idNum, 'province': province, 'city': city, 'district': district, 'address': address}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/pass', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_refuse(self, id, userId, reason):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'userId': userId, 'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/refuse', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_save(self, id, positive, negative, name, gender, birthday, idNum, province, city, district, address):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'positive': positive, 'negative': negative, 'name': name, 'gender': gender, 'birthday': birthday, 'idNum': idNum, 'province': province, 'city': city, 'district': district, 'address': address}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/save', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_upload(self, identityFile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'identityFile': identityFile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/upload', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_add(self, mobile, realName, role, email):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'realName': realName, 'role': role, 'email': email}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_del(self, userId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_edit(self, userId, mobile, realName, role, email):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId, 'mobile': mobile, 'realName': realName, 'role': role, 'email': email}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_freeze(self, userId, reason):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId, 'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/freeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_get_basic_info(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/get-basic-info', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_list(self, pn, ps, status, role, realName, email, mobile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'status': status, 'role': role, 'realName': realName, 'email': email, 'mobile': mobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_reset_password(self, userId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/reset-password', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_unfreeze(self, userId, reason):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId, 'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/unfreeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_log_auth_log(self, pn, ps, operateRole, userId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'operateRole': operateRole, 'userId': userId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/log/auth-log', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_log_user_log(self, pn, ps, userId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'userId': userId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/log/user-log', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_service_get_accid(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/service/get-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_service_update_service_status(self, serviceId, serviceStatus):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'serviceId': serviceId, 'serviceStatus': serviceStatus}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/service/update-service-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_count(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_default_head_img(self, headImg, headImgType):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImg': headImg, 'headImgType': headImgType}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/default-head-img', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_detail(self, userId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_freeze(self, userId, roleType, reason):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId, 'roleType': roleType, 'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/freeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_list(self, pn, ps, status, nickname, role, mobile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'status': status, 'nickname': nickname, 'role': role, 'mobile': mobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_unfreeze(self, userId, roleType, reason):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId, 'roleType': roleType, 'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/unfreeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_update_mobile(self, oldMobile, newMobile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'oldMobile': oldMobile, 'newMobile': newMobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_address_detail(self, addressId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'addressId': addressId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/address/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_address_get_default(self, userId, lat, lng):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId, 'lat': lat, 'lng': lng}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/address/get-default', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_address_list(self, userId, lat, lng):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId, 'lat': lat, 'lng': lng}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/address/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_third_login_or_register(self, mobile, appType, openid, nickname, headImg, accessToken):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'appType': appType, 'openid': openid, 'nickname': nickname, 'headImg': headImg, 'accessToken': accessToken}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user-third/login-or-register', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_back_detail(self, userId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user/back-detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_detail(self, userId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_get_by_mobile(self, mobile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user/get-by-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_list_ids(self, userIds):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userIds': userIds}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user/list-ids', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_login_or_register(self, mobile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user/login-or-register', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_register(self, mobile, verifyCode):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'verifyCode': verifyCode}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user/register', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_validate_account(self, account, accountType, password):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'account': account, 'accountType': accountType, 'password': password}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user/validate-account', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_add(self, receiver, contactNumber, province, city, address, doorNumber, lng, lat, isDefault):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'receiver': receiver, 'contactNumber': contactNumber, 'province': province, 'city': city, 'address': address, 'doorNumber': doorNumber, 'lng': lng, 'lat': lat, 'isDefault': isDefault}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/address/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_del(self, addressId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'addressId': addressId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/address/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_edit(self, id, receiver, contactNumber, province, city, address, doorNumber, lng, lat, isDefault):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'receiver': receiver, 'contactNumber': contactNumber, 'province': province, 'city': city, 'address': address, 'doorNumber': doorNumber, 'lng': lng, 'lat': lat, 'isDefault': isDefault}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/address/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_list(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/address/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_set_default(self, addressId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'addressId': addressId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/address/set-default', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_apply_channel(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/apply/channel', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_apply_channel_status(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/apply/channel-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_apply_supplier(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/apply/supplier', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_apply_supplier_status(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/apply/supplier-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_message_del(self, msgId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'msgId': msgId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/message/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_message_list(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/message/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_message_read(self, msgId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'msgId': msgId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/message/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_message_unread(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/message/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_service_get_accid(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/service/get-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_service_get_seller_accid(self, sellerId):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'sellerId': sellerId}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/service/get-seller-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_service_get_service_accid(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/service/get-service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_third_change_payaccount(self, code):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user-third/change-payaccount', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_change_verify_code(self, mobile, bizType):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'bizType': bizType}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/change-verify-code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_get_basic_info(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/get-basic-info', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_get_push_alias(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/get-push-alias', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_modify(self, headImg, nickname):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImg': headImg, 'nickname': nickname}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/modify', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_register_verify_code(self, mobile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/register-verify-code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_update_mobile(self, mobile, verifyCode):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'verifyCode': verifyCode}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_update_nickname(self, nickname):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'nickname': nickname}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/update-nickname', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_upload_headImg(self, headImgFile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImgFile': headImgFile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/upload-headImg', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_validate_mobile(self, verifyCode):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'verifyCode': verifyCode}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/validate-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
