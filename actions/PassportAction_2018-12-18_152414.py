# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class passportAction(object):

    def __init__(self, passport):
        self.log = Log('passport')
        self.request = Request()
        self.passport = passport

    def _admin_service_account_login(self, appId, deviceType, deviceId, account, password):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'password': password}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/admin/service/account-login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_service_logout(self, token):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'token': token}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/admin/service/logout', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_sso_check_token(self, ip, deviceType, deviceId, token):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'ip': ip, 'deviceType': deviceType, 'deviceId': deviceId, 'token': token}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/api/sso/check-token', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_sso_clear_token(self, userId, appId):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'userId': userId, 'appId': appId}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/api/sso/clear-token', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_sso_ms_freeze(self, userId, appId):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'userId': userId, 'appId': appId}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/api/sso/ms-freeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_automatic_login(self, token, encryptedPwd, deviceId):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'token': token, 'encryptedPwd': encryptedPwd, 'deviceId': deviceId}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/mobile/sso/automatic-login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_logout(self, token):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'token': token}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/mobile/sso/logout', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_sms_login(self, mobile, verifyCode, deviceType, deviceId, accountType, appId):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'mobile': mobile, 'verifyCode': verifyCode, 'deviceType': deviceType, 'deviceId': deviceId, 'accountType': accountType, 'appId': appId}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/mobile/sso/sms-login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_third_bind_weixin(self, mobile, verifyCode, openId, accessToken, nickname, headImg, authType, deviceId, deviceType, appId):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'mobile': mobile, 'verifyCode': verifyCode, 'openId': openId, 'accessToken': accessToken, 'nickname': nickname, 'headImg': headImg, 'authType': authType, 'deviceId': deviceId, 'deviceType': deviceType, 'appId': appId}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/mobile/sso/third-bind-weixin', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_third_login_weixin(self, code, deviceId, deviceType, appId):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'code': code, 'deviceId': deviceId, 'deviceType': deviceType, 'appId': appId}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/mobile/sso/third-login-weixin', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_verify_code_get(self, appId, mobile, bizType):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'appId': appId, 'mobile': mobile, 'bizType': bizType}
        response = self.request.post(url='http://dev.ms.passport.sjnc.com/mobile/sso/verify-code-get', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
