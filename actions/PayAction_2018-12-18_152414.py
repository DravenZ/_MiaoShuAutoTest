# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class payAction(object):

    def __init__(self, pay):
        self.log = Log('pay')
        self.request = Request()
        self.pay = pay

    def _admin_situation_info(self, startTime, endTime):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/admin/situation/info', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_situation_service_order_quantity(self, startTime, endTime):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/admin/situation/service-order-quantity', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_situation_service_tansactions(self, startTime, endTime):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/admin/situation/service-tansactions', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_account_fund_bind_third(self, accountId, pfCode, openId, appType):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'accountId': accountId, 'pfCode': pfCode, 'openId': openId, 'appType': appType}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/account-fund/bind-third', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_account_fund_create(self, accountId, pfCode, openId, appType):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'accountId': accountId, 'pfCode': pfCode, 'openId': openId, 'appType': appType}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/account-fund/create', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_account_fund_freeze(self, accountId, pfCode):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'accountId': accountId, 'pfCode': pfCode}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/account-fund/freeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_account_fund_query_balance(self, accountId, pfCode):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'accountId': accountId, 'pfCode': pfCode}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/account-fund/query-balance', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_account_fund_unfreeze(self, accountId, pfCode):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'accountId': accountId, 'pfCode': pfCode}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/account-fund/unfreeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_callback_query_pay(self, channelId, channelSubmitId):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'channelId': channelId, 'channelSubmitId': channelSubmitId}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/callback/query-pay', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_callback_query_refund(self, channelId, channelSubmitId):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'channelId': channelId, 'channelSubmitId': channelSubmitId}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/callback/query-refund', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_callback_query_withdraw(self, channelId, channelSubmitId):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'channelId': channelId, 'channelSubmitId': channelSubmitId}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/callback/query-withdraw', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_callback_withdraw(self, pfCode, name, srcAccountId, srcAccountName, desAccountNo, desAccountName, amount, outTradeNo, notifyUrl, channelId):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'pfCode': pfCode, 'name': name, 'srcAccountId': srcAccountId, 'srcAccountName': srcAccountName, 'desAccountNo': desAccountNo, 'desAccountName': desAccountName, 'amount': amount, 'outTradeNo': outTradeNo, 'notifyUrl': notifyUrl, 'channelId': channelId}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/callback/withdraw', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_channel_bill_query_mspay_bill(self, tradeDateStart, tradeDateEnd, channelId, pageSize, currentPage):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'tradeDateStart': tradeDateStart, 'tradeDateEnd': tradeDateEnd, 'channelId': channelId, 'pageSize': pageSize, 'currentPage': currentPage}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/channel-bill/query-mspay-bill', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_channel_bill_query_thrid_party_bill(self, tradeDateStart, tradeDateEnd, channelId):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'tradeDateStart': tradeDateStart, 'tradeDateEnd': tradeDateEnd, 'channelId': channelId}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/channel-bill/query-thrid-party-bill', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_trade_close(self, tradeNo, outTradeNo):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'tradeNo': tradeNo, 'outTradeNo': outTradeNo}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/trade/close', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_trade_confirm(self, tradeNos, accountId, remark):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'tradeNos': tradeNos, 'accountId': accountId, 'remark': remark}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/trade/confirm', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_trade_create(self, pfCode, name, srcAccountId, srcAccountName, desAccountNo, desAccountName, amount, outTradeNo, notifyUrl):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'pfCode': pfCode, 'name': name, 'srcAccountId': srcAccountId, 'srcAccountName': srcAccountName, 'desAccountNo': desAccountNo, 'desAccountName': desAccountName, 'amount': amount, 'outTradeNo': outTradeNo, 'notifyUrl': notifyUrl}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/trade/create', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_trade_query(self, pageSize, pageNum, tradeNo, outTradeNo):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'pageSize': pageSize, 'pageNum': pageNum, 'tradeNo': tradeNo, 'outTradeNo': outTradeNo}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/trade/query', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_trade_refund(self, tradeNo, amount, remark, accountId):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'tradeNo': tradeNo, 'amount': amount, 'remark': remark, 'accountId': accountId}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/api/trade/refund', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_account_sales_amount(self):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/mobile/account/sales-amount', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_account_sales_bill(self, pageSize, pageNum):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'pageSize': pageSize, 'pageNum': pageNum}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/mobile/account/sales-bill', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_cashier_index(self, tradeNos):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'tradeNos': tradeNos}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/mobile/cashier/index', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_weipay_pay(self, tradeNos, channelId, channelAmount):
        data = {'_tk_': self.pay.token, '_deviceId_': self.pay.device_id, 'tradeNos': tradeNos, 'channelId': channelId, 'channelAmount': channelAmount}
        response = self.request.post(url='https://dev.ms.pay.sjnc.com/mobile/weipay/pay', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
