# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
 
class orderAction(object):

    def __init__(self, order):
        self.log = Log('order')
        self.request = Request()
        self.order = order

    def _admin_report_order_pie_sta(self, startDate, endDate):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'startDate': startDate, 'endDate': endDate}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/admin/report/order/pie-sta', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_order_summary_sta(self, startDate, endDate):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'startDate': startDate, 'endDate': endDate}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/admin/report/order/summary-sta', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_service_order_service_data_card(self, startTime, endTime):
        '''
        baiying:服务数据卡片
        :param startTime:开始时间
        :param endTime:结束时间
        :return:
        '''
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/admin/report/service-order/service-data-card', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_service_order_service_data_trend(self, startTime, endTime):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/admin/report/service-order/service-data-trend', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_service_order_service_type_distribution(self, startTime, endTime):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/admin/report/service-order/service-type-distribution', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_order_shop_pending_count(self, orderType, shopId):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderType': orderType, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/api/order/shop-pending-count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_order_sta_shop_income(self, orderType, shopId):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderType': orderType, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/api/order/sta-shop-income', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_order_trade_callback(self, tradeNo, outTradeNo, amount, status, statusInTime, pfCode):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'tradeNo': tradeNo, 'outTradeNo': outTradeNo, 'amount': amount, 'status': status, 'statusInTime': statusInTime, 'pfCode': pfCode}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/api/order/trade/callback', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_serviceOrder_complete_num(self, shopId):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/api/serviceOrder/complete-num', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_trigger_call_close_over_time_order(self):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/api/trigger/call/close-over-time-order', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_trigger_call_service_order_daily_sta(self):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/api/trigger/call/service-order-daily-sta', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_trigger_call_sync_order_pay_status(self):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/api/trigger/call/sync-order-pay-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_order_agree(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/channel/order/agree', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_order_detail(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/channel/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_order_finish_send(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/channel/order/finish-send', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_order_list(self, orderStatus, shopId, pn, ps):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderStatus': orderStatus, 'shopId': shopId, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/channel/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_order_pending_count(self, shopId):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/channel/order/pending-count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_order_refuse(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/channel/order/refuse', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_service_order_detail(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/channel/service/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_service_order_finish_door(self, orderNo, tailMoneyPrice):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo, 'tailMoneyPrice': tailMoneyPrice}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/channel/service/order/finish-door', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_service_order_list(self, orderStatus, pn, ps):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderStatus': orderStatus, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/channel/service/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_channel_service_order_submit(self, buyerId, shopId, serviceType, doorTime, doorAddress, lng, lat, content, earnestMoneyPrice):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'buyerId': buyerId, 'shopId': shopId, 'serviceType': serviceType, 'doorTime': doorTime, 'doorAddress': doorAddress, 'lng': lng, 'lat': lat, 'content': content, 'earnestMoneyPrice': earnestMoneyPrice}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/channel/service/order/submit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_customer_order_apply_refund(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/customer/order/apply-refund', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_customer_order_close(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/customer/order/close', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_customer_order_confirm_receive(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/customer/order/confirm-receive', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_customer_order_detail(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/customer/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_customer_order_list(self, orderStatus, pn, ps):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderStatus': orderStatus, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/customer/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_customer_order_submit_order(self, shopId, sellerId, buyerMemo, product, addressId, freight, productPrice, isCheck):
        """
        买家端确认下单
        :param shopId:
        :param sellerId:
        :param buyerMemo:
        :param product:
        :param addressId:
        :param freight:
        :param productPrice:
        :param isCheck:
        :return:
        """
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'shopId': shopId, 'sellerId': sellerId, 'buyerMemo': buyerMemo, 'product': product, 'addressId': addressId, 'freight': freight, 'productPrice': productPrice, 'isCheck': isCheck}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/customer/order/submit-order', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_customer_service_order_cancel(self, orderNo):
        '''
        baiying：买家服务单取消订单
        :param orderNo:订单编号
        :return:
        '''
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/customer/service/order/cancel', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_customer_service_order_detail(self, orderNo):
        '''
        baiying:买家服务单订单详情
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/customer/service/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_customer_service_order_list(self, orderStatus, pn, ps):
        '''
        baiying:买家服务单订单列表
        :param orderStatus:
        :param pn:
        :param ps:
        :return:
        '''
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderStatus': orderStatus, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/customer/service/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_customer_service_order_unpaid_tail_money(self):
        '''
        baiying:获取用户未支付尾款的订单编号
        :return:
        '''
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/customer/service/order/unpaid-tail-money', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_channel_order_agree(self, orderNo):
        '''
        baiying:
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/agree', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_channel_order_detail(self, orderNo):
        '''
        baiying:
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_channel_order_finish_send(self, orderNo):
        '''
        baiying:
        :param orderNo:
        :return:
        '''
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/finish-send', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_channel_order_list(self, orderStatus, shopId, pn, ps):
        '''
        baiying:
        :param orderStatus:
        :param shopId:
        :param pn:
        :param ps:
        :return:
        '''
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderStatus': orderStatus, 'shopId': shopId, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_channel_order_pending_count(self, shopId):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'shopId': shopId}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/pending-count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_channel_order_refuse(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/channel/order/refuse', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_customer_order_apply_refund(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/apply-refund', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_customer_order_close(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/close', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_customer_order_confirm_receive(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/confirm-receive', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_customer_order_detail(self, orderNo):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderNo': orderNo}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_customer_order_list(self, orderStatus, pn, ps):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'orderStatus': orderStatus, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_supply_customer_order_submit_order(self, shopId, sellerId, buyerMemo, product, addressId, productPrice, isCheck):
        data = {'_tk_': self.order.token, '_deviceId_': self.order.device_id, 'shopId': shopId, 'sellerId': sellerId, 'buyerMemo': buyerMemo, 'product': product, 'addressId': addressId, 'productPrice': productPrice, 'isCheck': isCheck}
        response = self.request.post(url='http://dev.ms.order.sjnc.com/mobile/supply/customer/order/submit-order', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

if __name__ == '__main__':
    User = User