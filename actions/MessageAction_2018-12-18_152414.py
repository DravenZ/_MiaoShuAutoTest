# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class messageAction(object):

    def __init__(self, message):
        self.log = Log('message')
        self.request = Request()
        self.message = message

    def _admin_im_auth_service_get_accid(self, serveType, userId):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'serveType': serveType, 'userId': userId}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/admin/im-auth/service-get/accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_im_get_im_account(self, appId, uid, accType, serveType, roleType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'appId': appId, 'uid': uid, 'accType': accType, 'serveType': serveType, 'roleType': roleType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/api/im/get/im-account', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_im_get_service_accid(self, appId, fromUid, fromUserType, toUid, toUserType, serveType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'appId': appId, 'fromUid': fromUid, 'fromUserType': fromUserType, 'toUid': toUid, 'toUserType': toUserType, 'serveType': serveType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/api/im/get/service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_message_center_del(self, userId, msgId, serveType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'userId': userId, 'msgId': msgId, 'serveType': serveType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/api/message-center/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_message_center_list(self, userId, serveType, pn, ps):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'userId': userId, 'serveType': serveType, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/api/message-center/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_message_center_pageList(self, userId, serveType, pn, ps):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'userId': userId, 'serveType': serveType, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/api/message-center/pageList', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_message_center_read(self, userId, msgId, serveType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'userId': userId, 'msgId': msgId, 'serveType': serveType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/api/message-center/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_message_center_unread(self, userId, msgId, serveType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'userId': userId, 'msgId': msgId, 'serveType': serveType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/api/message-center/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_push_message_get_push_alias(self, userId, userType, serveType, roleId, deviceId):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'userId': userId, 'userType': userType, 'serveType': serveType, 'roleId': roleId, 'deviceId': deviceId}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/api/push-message/get-push-alias', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shortMessage_send_message_count(self, mobileRegion, mobile, businessType, serveType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'mobileRegion': mobileRegion, 'mobile': mobile, 'businessType': businessType, 'serveType': serveType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/api/shortMessage/send-message-count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shortMessage_validate_verify_code(self, mobileRegion, mobile, verifyCode, businessType, serveType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'mobileRegion': mobileRegion, 'mobile': mobile, 'verifyCode': verifyCode, 'businessType': businessType, 'serveType': serveType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/api/shortMessage/validate-verify-code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_message_center_list(self, category, userId, serveType, pn, ps):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'category': category, 'userId': userId, 'serveType': serveType, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/buyer/message-center/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_message_center_read(self, category):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'category': category}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/buyer/message-center/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_message_center_unread(self, category):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'category': category}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/buyer/message-center/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_sub_message_read(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/buyer/sub-message/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_sub_message_unread(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/buyer/sub-message/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_im_auth_promoter_get_seller_agency_accid(self, userId, serveType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'userId': userId, 'serveType': serveType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/im-auth/promoter/get/seller-agency-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_message_center_read(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/message-center/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_message_center_unread(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/message-center/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_push_message_count_unread(self, category):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'category': category}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/promoter/push-message/count-unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_push_message_list(self, category, pn, ps, userId):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'category': category, 'pn': pn, 'ps': ps, 'userId': userId}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/promoter/push-message/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_push_message_read(self, msgId):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'msgId': msgId}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/promoter/push-message/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_push_auth_get_alias_buyer(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/push-auth/get/alias/buyer', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_push_auth_get_alias_buyer_and_seller(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/push-auth/get/alias/buyer-and-seller', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_push_auth_get_alias_promoter(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/push-auth/get/alias/promoter', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_push_auth_get_alias_seller_agency(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/push-auth/get/alias/seller-agency', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_push_message_count_unread(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/seller-agency/push-message/count-unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_push_message_detail(self, id):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/seller-agency/push-message/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_push_message_list(self, pn, ps, userId):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'pn': pn, 'ps': ps, 'userId': userId}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/seller-agency/push-message/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_push_message_read(self, msgId):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'msgId': msgId}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/mobile/seller-agency/push-message/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _tx_get_user_info(self, accid):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'accid': accid}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/tx/get/user-info', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_message_center_list(self, category, userId, serveType, pn, ps):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'category': category, 'userId': userId, 'serveType': serveType, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/web/buyer/message-center/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_message_center_read(self, category):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'category': category}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/web/buyer/message-center/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_message_center_unread(self, category):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'category': category}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/web/buyer/message-center/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_im_auth_buyer_and_seller_allot_exclusive_service_accid(self, serveType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'serveType': serveType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/web/im-auth/buyer-and-seller/allot/exclusive-service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_im_auth_buyer_and_seller_get_exclusive_service_accid(self, serveType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'serveType': serveType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/web/im-auth/buyer-and-seller/get/exclusive-service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_im_auth_buyer_and_seller_get_service_accid(self, userId, serveType):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id, 'userId': userId, 'serveType': serveType}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/web/im-auth/buyer-and-seller/get/service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_message_center_read(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/web/message-center/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_message_center_unread(self):
        data = {'_tk_': self.message.token, '_deviceId_': self.message.device_id}
        response = self.request.post(url='http://dev.ms.message.sjnc.com/web/message-center/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
