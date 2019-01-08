# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
from backend.User import User

import json
 
class userAction(object):

    def __init__(self):
        self.log = Log('user')
        self.request = Request()

    def set_user(self, user):
        self.user = User(user)
        return self.user

    def _admin_audit_detail(self, id, user_id):
        """
        杨露瑶:审核详情
        :param id:
        :param user_id:
        :return:
        """
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_list(self, pn, ps, status, mobile, apply_role, nickname=None):
        """
        杨露瑶:用户待审核列表,返回用户id进行下一步审核
        :param pn:
        :param ps:
        :param status:
        :param mobile:
        :param apply_role:
        :param nickname:
        :return:
        """
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'status': status,
                'mobile': mobile, 'nickname': nickname, 'applyRole': apply_role}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_pass(self, id, user_id, positive, negative, name, gender, birthday, id_num, province, city,
                          district, address):
        """
        杨露瑶:用户审核通过
        """
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'userId': user_id,
                'positive': positive, 'negative': negative, 'name': name, 'gender': gender, 'birthday': birthday,
                'idNum': id_num, 'province': province, 'city': city, 'district': district, 'address': address}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/pass', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_refuse(self, id, user_id, reason):
        """
        杨露瑶:用户审核不通过
        :param id:
        :param user_id:
        :param reason:
        :return:
        """
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'userId': user_id,
                'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/refuse', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_save(self, id, positive, negative, name, gender, birthday, id_num, province, city, district,
                          address):
        """
        审核保存
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
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'positive': positive,
                'negative': negative, 'name': name, 'gender': gender, 'birthday': birthday, 'idNum': id_num,
                'province': province, 'city': city, 'district': district, 'address': address}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/save', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_audit_upload(self):
        """
        杨露瑶:身份证图片上传,返回图片https地址
        :return:
        """
        # data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'identityFile': identity_file}
        response = self.request.post_file(url='http://dev.ms.user.sjnc.com/admin/audit/upload',
                                          file_path='./../picture/1.png', file_key='identityFile', data_dict=None)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_add(self, mobile, real_name, role, email):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'realName': real_name,
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
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_edit(self, user_id, mobile, real_name, role, email):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id, 'mobile': mobile,
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
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id, 'reason': reason}
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

    def _admin_backstage_list(self, pn, ps, status, role, real_name, email, mobile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'status': status,
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
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/reset-password', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_backstage_unfreeze(self, user_id, reason):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id, 'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/unfreeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_log_auth_log(self, pn, ps, operate_role, user_id):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps,
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
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'userId': user_id}
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

    def _admin_service_update_service_status(self, service_id, service_status):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'serviceId': service_id,
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
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_default_head_img(self, head_img, head_img_type):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImg': head_img,
                'headImgType': head_img_type}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/default-head-img', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_detail(self, user_id):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_freeze(self, user_id, role_type, reason):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id, 'roleType': role_type,
                'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/freeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_list(self, pn, ps, status, nickname, role, mobile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'status': status,
                'nickname': nickname, 'role': role, 'mobile': mobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_unfreeze(self, user_id, role_type, reason):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id, 'roleType': role_type,
                'reason': reason}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/unfreeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_update_mobile(self, old_mobile, new_mobile):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'oldMobile': old_mobile,
                'newMobile': new_mobile}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/user/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_address_detail(self, address_id):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'addressId': address_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/address/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_address_get_default(self, user_id, lat, lng):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id, 'lat': lat, 'lng': lng}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/address/get-default', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_address_list(self, user_id, lat, lng):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id, 'lat': lat, 'lng': lng}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/address/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_third_login_or_register(self, mobile, app_type, openid, nickname, access_token):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'appType': app_type,
                'openid': openid, 'nickname': nickname, 'accessToken': access_token}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user-third/login-or-register', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_back_detail(self, user_id):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user/back-detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_detail(self, user_id):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id}
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

    def _api_user_list_ids(self, user_ids):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userIds': user_ids}
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

    def _api_user_register(self, mobile, verify_code):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'verifyCode': verify_code}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user/register', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_user_validate_account(self, account, account_type, password):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'account': account,
                'accountType': account_type, 'password': password}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/api/user/validate-account', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_add(self, user_id, receiver, contact_number, province, city, address, door_number, lng, lat,
                            is_default):
        """
        买家添加收货地址
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
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id, 'receiver': receiver,
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

    def _mobile_address_del(self, address_id):
        """
        买家删除收货地址
        :param address_id:
        :return:
        """
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'addressId': address_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/address/del', data=data)
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
        买家编辑地址
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
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'userId': user_id, 'receiver':
                receiver, 'contactNumber': contact_number, 'province': province, 'city': city, 'address': address,
                'doorNumber': door_number, 'lng': lng, 'lat': lat, 'isDefault': is_default}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/address/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_list(self, user_id):
        """
        买家获取地址列表
        :param user_id:
        :return:
        """
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/address/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_address_set_default(self, address_id, user_id):
        """
        买家设置默认地址
        :param address_id:
        :param user_id:
        :return:
        """
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'addressId': address_id, 'userId': user_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/address/set-default', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_apply_channel(self):
        """
        杨露瑶:苗叔申请
        """
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
        """
        杨露瑶:获取苗叔申请状态
        """
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
        """
        杨露瑶:基地申请
        """
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
        """
        杨露瑶:获取基地审核状态
        :return:
        """
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/apply/supplier-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_message_del(self, msg_id):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'msgId': msg_id}
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

    def _mobile_message_read(self, msg_id):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'msgId': msg_id}
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

    def _mobile_service_get_seller_accid(self, seller_id):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'sellerId': seller_id}
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

    def _mobile_user_change_verify_code(self, mobile, biz_type):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'bizType': biz_type}
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

    def _mobile_user_modify(self, user_id, head_img, nickname):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id, 'headImg': head_img,
                'nickname': nickname}
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

    def _mobile_user_update_mobile(self, mobile, verify_code):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'verifyCode': verify_code}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_update_nickname(self, user_id, nickname):
        """
        杨露瑶:修改用户昵称
        :param user_id:
        :param nickname:
        :return:
        """
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': user_id, 'nickname': nickname}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/update-nickname', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_upload_headImg(self, head_img_file):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImgFile': head_img_file}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/upload-headImg', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_user_validate_mobile(self, verify_code):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'verifyCode': verify_code}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/mobile/user/validate-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_situation_info(self, startTime, endTime):
        '''
        baiying:平台概况
        :param startTime:
        :param endTime:
        :return:
        '''
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/admin/situation/info', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _admin_situation_service_order_quantity(self, startTime, endTime):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/admin/situation/service-order-quantity', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _admin_situation_service_tansactions(self, startTime, endTime):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/admin/situation/service-tansactions', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_account_sales_amount(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/mobile/account/sales-amount', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _mobile_account_sales_bill(self, pageSize, pageNum):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pageSize': pageSize, 'pageNum': pageNum}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/mobile/account/sales-bill', data=data)
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
    user = User('18382373185')
    us = userAction(user)
    # us._admin_situation_info("2018-12-18", "2018-12-19")
    # us._admin_situation_service_order_quantity("2018-12-18", "2018-12-19")
    # us._admin_situation_service_tansactions("2018-12-18", "2018-12-19")
    # us._mobile_account_sales_amount()
    # us._mobile_account_sales_bill(1, 2)

    # us._mobile_apply_channel()
    # us._mobile_apply_supplier()
    # us._mobile_apply_channel_status()
    # us._mobile_apply_supplier_status()
    # us._admin_audit_list('1', '20', '4', '18382373185', '2')
    # us._admin_audit_upload()
    # us._admin_audit_pass('127', '1210', 'https://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-user/applyMa'
    #                      'terials/1544852604402.png?Expires=1544852897&OSSAccessKeyId=LTAIln07EgYJRc0Z&S''ignature=jTDa'
    #                      '0Bk1zJljncu04ijZ7kE73rA%3D', 'https://dnkj-family-farm-1.oss-''cn-huhehaote.aliyuncs.com/'
    #                      'data/ms-user/applyMaterials/1544852604402.png?Expires=1544852897&OSSAccessKeyId=LTAIln07EgYJ'
    #                      'Rc0Z&Signature=jTDa0Bk1zJljncu04ijZ7kE73rA%3D', '付国超', '1', '1994-01-14',
    #                      '513822199409147688', '11', '11101', '1101104', '大农科技')
    # us._admin_audit_refuse('119', '1210', '信息不完整')
    # us._admin_audit_detail('127', '1210')
    # us._mobile_user_update_nickname('1210', '一群精灵')
    # us._mobile_address_add('1210', '大农科技', '18382373185', '41', '4101', '软件园', '901', '116.397', '39.9165', '0')
    # us._mobile_address_list(1210)
    # us._mobile_address_edit(149, 1210, '高新区某某某', '18382373185', '41', '4101', '软件园', '901', '116.397', '39.9165', '0')