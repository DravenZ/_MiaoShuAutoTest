# encoding: utf-8

"""
__author__ = "Zhang Pengfei"
__date__ = 2018/11/17
"""
from backend.User import User
from actions.PurchaserAction import PurchaserAction
from actions.DistributorAction import DistributorAction
from actions.OperatorAction import OperatorAction
from actions.SupplierAction import SupplierAction
from backend.Employee import Employee
import unittest
from utils.Log import Log
from backend.Product import Product
from backend.Shop import Shop
from backend.Tool import Tool
from utils.Config import Config
from utils.Util import AndroidTool
from utils.Util import Mail
import time
import random


class Main(unittest.TestCase):
    op_account = Config('config').data['User'][Config('config').data['run']]['op']
    product_name = Config('productname').data['product_name']
    L = Log('Main')
    toot = Tool()
    # 登录
    buyer = User('18380581406')
    # 切换角色
    pa = PurchaserAction(buyer)
    at = AndroidTool()
    distributor = User('18380581416')
    di = DistributorAction(distributor)

    supplier = User('18380581426')
    su = SupplierAction(supplier)

    operator = Employee(op_account['account'], op_account['password'], 1)
    op = OperatorAction(operator)

    def tearDown(self):
        pass

    def setUp(self):
        url = 'http://203.6.234.220:9660/download/attachments/1016059/user-avatar'
        resp = self.di._mobile_apply_channel_status()
        if resp.get('content') in (1, 2, 3):
            if resp.get('content') in (1, 3):
                self.di._mobile_apply_channel()
            resp = self.op._admin_audit_list(1, 10, 2, self.distributor.mobile, 2).get('content').get('datas')[0]
            self.op._admin_audit_pass(id=resp.get('id'), user_id=resp.get('userId'), positive=url, negative=url,
                                      name='Draven', gender=1, birthday='2018-11-11', id_num='513902199309091011',
                                      province=41, city=4140, district=1101104, address='领馆科技')
        resp = self.di._mobile_apply_channel_status()
        if resp.get('content') == 4:
            self.di._mobile_shop_server_server(10, 10)
            self.di._mobile_shop_server_server(20, 10)

        shop_info = self.di.get_shop_id_by_type(self.distributor.user_id)
        shop_id = shop_info.get('content').get('shopId')
        self.distributor.channel_shop_id = shop_id

        self.L.logger.debug('客户端查询地址列表')
        address_list = self.pa._mobile_address_list()
        if len(address_list['content']) == 0:
            self.L.logger.debug('用户添加收货地址')
            self.pa._mobile_address_add('xiu', self.buyer.mobile, '41', '4101', '天府五街', 'E3-9', 104.069, 30.539, 1)

    def test0033(self):
        try:
            apk_path = '/Users/hengxin/Downloads/苗叔-20181130\(v1.0.24\).apk'
            self.at.launch_app_by_apk(apk_path)
            self.at.login_miaoshu("18602832572", "888888")
            self.at.enter_shop("自动化刷单勿删")
            self.at.pay_product()
            self.at.tear_down_miaoshu()
            Mail().send_html_email()
            self.L.logger.info("测试完成, 邮件发送成功")
        except Exception as e:
            self.at.get_screen_shot()
            self.L.logger.debug("错误信息: %s" % e)
            self.at.tear_down_miaoshu()

    def test0034(self):
        """
        服务订单的完整流程
        :return:
        """
        shopinfo = self.di.get_shop_id_by_type(self.distributor.user_id)
        shop_id = shopinfo.get('content').get('shopId')
        self.distributor.channel_shop_id = shop_id
        shop = Shop(self.distributor)
        self.L.logger.debug('渠道商新增商品')
        for i in range(3):
            p = Product(user=self.distributor, product_name=str(i))
            self.di.product_save(p)
        self.L.logger.debug('添加接单点')
        self.di.add_address(shop)
        self.L.logger.debug('开始接单')
        self.di.switch_status(shop_id=shop_id)

        order_no = self.di._mobile_channel_service_order_submit(buyerId=self.buyer.user_id, shopId=shop_id,
                                                                serviceType=20, doorTime='2019-12-16 08:00',
                                                                content='养猪', earnestMoneyPrice=1, doorAddress='ce',
                                                                lng=103, lat=40)
        self.di._mobile_channel_service_order_detail(order_no['content'])
        order_info = self.pa._mobile_customer_service_order_detail(order_no['content'])
        caindex = self.pa.cashier_index(order_info['content']['earnestMoneyTradeNo'])
        self.pa.weipay_pay(order_info['content']['earnestMoneyTradeNo'], caindex['content']['channelList'][0]['id'],
                           order_info['content']['earnestMoneyPrice'])
        self.pa.pay_callback(order_info['content']['earnestMoneyTradeNo'], order_info['content']['earnestMoneyPrice'])
        time.sleep(15)
        self.pa._mobile_customer_service_order_detail(order_no['content'])
        self.di._mobile_channel_service_order_detail(order_no['content'])
        self.di._mobile_channel_service_order_finish_door(order_no['content'], 10)

        order_info = self.pa._mobile_customer_service_order_detail(order_no['content'])
        caindex = self.pa.cashier_index(order_info['content']['tailMoneyTradeNo'])
        self.pa.weipay_pay(order_info['content']['tailMoneyTradeNo'], caindex['content']['channelList'][0]['id'],
                           order_info['content']['tailMoneyPrice'])
        self.pa.pay_callback(order_info['content']['tailMoneyTradeNo'], order_info['content']['tailMoneyPrice'])

        time.sleep(15)
        self.pa._mobile_customer_service_order_detail(order_no['content'])
        self.di._mobile_channel_service_order_detail(order_no['content'])

    def test0035(self):
        """
        服务订单的取消流程
        :return:
        """
        shopinfo = self.di.get_shop_id_by_type(self.distributor.user_id)
        shop_id = shopinfo.get('content').get('shopId')
        self.distributor.channel_shop_id = shop_id

        shop = Shop(self.distributor)
        self.L.logger.debug('渠道商新增商品')
        for i in range(3):
            p = Product(user=self.distributor, product_name=str(i))
            self.di.product_save(p)
        self.L.logger.debug('添加接单点')
        self.di.add_address(shop)
        self.L.logger.debug('开始接单')
        self.di.switch_status(shop_id=shop_id)

        order_no = self.di._mobile_channel_service_order_submit(buyerId=self.buyer.user_id, shopId=shop_id,
                                                                serviceType=10, doorTime='2019-12-16 08:00',
                                                                content='养猪', earnestMoneyPrice=1,
                                                                doorAddress='ce', lng=103, lat=40)
        self.di._mobile_channel_service_order_detail(order_no['content'])
        self.pa._mobile_customer_service_order_detail(order_no['content'])
        self.pa._mobile_customer_service_order_cancel(order_no['content'])
        self.pa._mobile_customer_service_order_detail(order_no['content'])
        self.di._mobile_channel_service_order_detail(order_no['content'])

    def test0036(self):
        """
        张鹏飞:服务订单列表  订单状态,10:待下单, 20:待上门, 30:已结款, 40:已完成, 50: 已取消
        :return:
        """
        self.L.logger.debug("卖家服务订单列表")
        self.di._mobile_channel_service_order_list(10)
        self.di._mobile_channel_service_order_list(20)
        self.di._mobile_channel_service_order_list(30)
        self.di._mobile_channel_service_order_list(40)
        self.di._mobile_channel_service_order_list(50)
        self.L.logger.debug("买家服务订单列表")
        self.pa._mobile_customer_service_order_list(10)
        self.pa._mobile_customer_service_order_list(20)
        self.pa._mobile_customer_service_order_list(30)
        self.pa._mobile_customer_service_order_list(40)
        self.pa._mobile_customer_service_order_list(50)

    def test0037(self):
        """
        张鹏飞:商品订单正向流程
        :return:
        """
        shop_info = self.di.get_shop_id_by_type(self.distributor.user_id)
        shop_id = shop_info.get('content').get('shopId')
        self.distributor.channel_shop_id = shop_id

        self.L.logger.debug('苗叔查询运费模板列表')
        freight_list = self.di.all_freight()
        if len(freight_list['content']) <= 1:
            self.L.logger.debug('苗叔添加运费模板')
            self.di.freight_save_or_update(shop_id, '测试模板66', 500, 10000, 2000)

        self.L.logger.debug('更新店铺信息')
        shop = Shop(self.distributor)
        self.di.update_shop_info(shop)
        self.L.logger.debug('渠道商新增商品')
        for i in range(3):
            p = Product(user=self.distributor, product_name=random.choice(self.product_name))
            self.di.product_save(p)
            if i == 0:
                self.L.logger.debug('苗叔筛选查看库存商品列表')
                store_list = self.di.store_list_product(p)
                pro_code = store_list.get('content').get('datas')[0]['pcode']
                self.L.logger.debug('苗叔更新商品库存')
                self.di.store_update_product(pro_code)

                self.L.logger.debug('苗叔筛选查看商品列表')
                pro_list = self.di.list_product(p)
                pro_code = pro_list.get('content').get('datas')[0]['pcode']
                self.L.logger.debug('苗叔上架商品')
                self.di.status_update_product(pro_code)
                self.L.logger.debug('苗叔下架商品')
                self.di.status_update_product(pro_code, 20)
                self.L.logger.debug('苗叔删除商品')
                self.di.status_update_product(pro_code, 30)

        self.L.logger.debug('添加接单点')
        self.di.add_address(shop)
        self.L.logger.debug('开始接单')
        self.di.switch_status(shop_id=shop_id)

        self.L.logger.debug('客户端查询地址列表')
        address_list = self.pa._mobile_address_list()
        address = address_list['content'][0]
        add_id = address['id']

        self.L.logger.debug('客户端查询店铺信息')
        self.pa.get_shop_info_by_id(shop_id)
        self.L.logger.debug('店铺内商品列表')
        product_list = self.pa.get_shop_products_by_shop_id(shop_id)
        p_code = self.pa.tool.get_pro_code_by_pro_list(product_list['content'])

        self.L.logger.debug('添加购物车')
        self.pa.cart_add(p_code)
        self.L.logger.debug('购物车列表')
        cart_list = self.pa.get_cart_list()
        self.L.logger.debug('购物车结算')
        sure_order = self.pa.cart_balance(self.pa.tool.get_cart_ids_by_cart_list(cart_list, shop_id), add_id)
        self.L.logger.debug('确认提交订单')
        order = self.pa.submit_order(self.pa.tool.order_info_change(sure_order))
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('收银台')
        order_pay_info = self.pa.cashier_index(order['content']['tradeNo'])
        self.L.logger.debug('支付')
        self.pa.weipay_pay(order['content']['tradeNo'], order_pay_info['content']['channelList'][0]['id'],
                           order_pay_info['content']['amount'])
        self.L.logger.debug('付款')
        self.pa.pay_callback(order['content']['tradeNo'], order_pay_info['content']['amount'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('买家未完成配送前取消订单')
        self.pa._mobile_customer_order_apply_refund(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('苗叔拒绝取消订单')
        self.di._mobile_channel_order_refuse(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('渠道商完成配送')
        self.di.finish_send_order(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('买家完成配送后取消订单')
        self.pa._mobile_customer_order_apply_refund(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('苗叔拒绝取消订单')
        self.di._mobile_channel_order_refuse(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('用户确认收货')
        self.pa.confirm_receive(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])

    def test0038(self):
        """
        张鹏飞:待付款订单取消
        :return:
        """
        shop_info = self.di.get_shop_id_by_type(self.distributor.user_id)
        shop_id = shop_info.get('content').get('shopId')
        self.distributor.channel_shop_id = shop_id

        self.L.logger.debug('更新店铺信息')
        shop = Shop(self.distributor)
        self.di.update_shop_info(shop)
        self.L.logger.debug('渠道商新增商品')
        for i in range(3):
            p = Product(user=self.distributor, product_name=str(i))
            self.di.product_save(p)
        self.L.logger.debug('添加接单点')
        self.di.add_address(shop)
        self.L.logger.debug('开始接单')
        self.di.switch_status(shop_id=shop_id)

        self.L.logger.debug('客户端查询地址列表')
        address_list = self.pa._mobile_address_list()
        address = address_list['content'][0]
        add_id = address['id']

        self.L.logger.debug('客户端查询店铺信息')
        self.pa.get_shop_info_by_id(shop_id)
        self.L.logger.debug('店铺内商品列表')
        product_list = self.pa.get_shop_products_by_shop_id(shop_id)
        p_code = self.pa.tool.get_pro_code_by_pro_list(product_list['content'])

        self.L.logger.debug('添加购物车')
        self.pa.cart_add(p_code)
        self.L.logger.debug('购物车列表')
        cart_list = self.pa.get_cart_list()
        self.L.logger.debug('购物车结算')
        sure_order = self.pa.cart_balance(self.pa.tool.get_cart_ids_by_cart_list(cart_list, shop_id), add_id)
        self.L.logger.debug('确认提交订单')
        order = self.pa.submit_order(self.pa.tool.order_info_change(sure_order))
        self.L.logger.debug('关闭订单')
        self.pa.order_close(order['content']['orderNo'])

    def test0039(self):
        """
        张鹏飞:待配送订单取消成功
        :return:
        """
        shop_info = self.di.get_shop_id_by_type(self.distributor.user_id)
        shop_id = shop_info.get('content').get('shopId')
        self.distributor.channel_shop_id = shop_id

        self.L.logger.debug('更新店铺信息')
        shop = Shop(self.distributor)
        self.di.update_shop_info(shop)
        self.L.logger.debug('渠道商新增商品')
        for i in range(3):
            p = Product(user=self.distributor, product_name=str(i))
            self.di.product_save(p)
        self.L.logger.debug('添加接单点')
        self.di.add_address(shop)
        self.L.logger.debug('开始接单')
        self.di.switch_status(shop_id=shop_id)

        # self.L.logger.debug('用户添加收货地址')
        # self.pa._mobile_address_add('xiu', 19982917912, '41', '4101', '天府五街', 'E3-9', 104.069, 30.539, 1)
        self.L.logger.debug('客户端查询地址列表')
        address_list = self.pa._mobile_address_list()
        address = address_list['content'][0]
        add_id = address['id']

        self.L.logger.debug('客户端查询店铺信息')
        self.pa.get_shop_info_by_id(shop_id)
        self.L.logger.debug('店铺内商品列表')
        product_list = self.pa.get_shop_products_by_shop_id(shop_id)
        p_code = self.pa.tool.get_pro_code_by_pro_list(product_list['content'])

        self.L.logger.debug('添加购物车')
        self.pa.cart_add(p_code)
        self.L.logger.debug('购物车列表')
        cart_list = self.pa.get_cart_list()
        self.L.logger.debug('购物车结算')
        sure_order = self.pa.cart_balance(self.pa.tool.get_cart_ids_by_cart_list(cart_list, shop_id), add_id)
        self.L.logger.debug('确认提交订单')
        order = self.pa.submit_order(self.pa.tool.order_info_change(sure_order))
        self.L.logger.debug('订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('收银台')
        order_pay_info = self.pa.cashier_index(order['content']['tradeNo'])
        self.L.logger.debug('支付')
        self.pa.weipay_pay(order['content']['tradeNo'], order_pay_info['content']['channelList'][0]['id'],
                           order_pay_info['content']['amount'])
        self.L.logger.debug('付款')
        self.pa.pay_callback(order['content']['tradeNo'], order_pay_info['content']['amount'])

        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('买家未完成配送前取消订单')
        self.pa._mobile_customer_order_apply_refund(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('苗叔拒绝取消订单')
        self.di._mobile_channel_order_refuse(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('买家未完成配送前取消订单')
        self.pa._mobile_customer_order_apply_refund(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('苗叔同意取消订单')
        self.di._mobile_channel_order_agree(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])

    def test0040(self):
        """
        张鹏飞:已配送完成的订单,买家取消订单,卖家同意
        :return:
        """
        shop_info = self.di.get_shop_id_by_type(self.distributor.user_id)
        shop_id = shop_info.get('content').get('shopId')
        self.distributor.channel_shop_id = shop_id

        self.L.logger.debug('更新店铺信息')
        shop = Shop(self.distributor)
        self.di.update_shop_info(shop)
        self.L.logger.debug('渠道商新增商品')
        for i in range(3):
            p = Product(user=self.distributor, product_name=str(i))
            self.di.product_save(p)
        self.L.logger.debug('添加接单点')
        self.di.add_address(shop)
        self.L.logger.debug('开始接单')
        self.di.switch_status(shop_id=shop_id)

        # self.L.logger.debug('用户添加收货地址')
        # self.pa._mobile_address_add('xiu', 19982917912, '41', '4101', '天府五街', 'E3-9', 104.069, 30.539, 1)
        self.L.logger.debug('客户端查询地址列表')
        address_list = self.pa._mobile_address_list()
        address = address_list['content'][0]
        add_id = address['id']

        self.L.logger.debug('客户端查询店铺信息')
        self.pa.get_shop_info_by_id(shop_id)
        self.L.logger.debug('店铺内商品列表')
        product_list = self.pa.get_shop_products_by_shop_id(shop_id)
        p_code = self.pa.tool.get_pro_code_by_pro_list(product_list['content'])

        self.L.logger.debug('添加购物车')
        self.pa.cart_add(p_code)
        self.L.logger.debug('购物车列表')
        cart_list = self.pa.get_cart_list()
        self.L.logger.debug('购物车结算')
        sure_order = self.pa.cart_balance(self.pa.tool.get_cart_ids_by_cart_list(cart_list, shop_id), add_id)
        self.L.logger.debug('确认提交订单')
        order = self.pa.submit_order(self.pa.tool.order_info_change(sure_order))
        self.L.logger.debug('订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('收银台')
        order_pay_info = self.pa.cashier_index(order['content']['tradeNo'])
        self.L.logger.debug('支付')
        self.pa.weipay_pay(order['content']['tradeNo'], order_pay_info['content']['channelList'][0]['id'],
                           order_pay_info['content']['amount'])
        self.L.logger.debug('付款')
        self.pa.pay_callback(order['content']['tradeNo'], order_pay_info['content']['amount'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('买家未完成配送前取消订单')
        self.pa._mobile_customer_order_apply_refund(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('苗叔拒绝取消订单')
        self.di._mobile_channel_order_refuse(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('渠道商完成配送')
        self.di.finish_send_order(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('买家完成配送后取消订单')
        self.pa._mobile_customer_order_apply_refund(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])
        self.L.logger.debug('苗叔同意取消订单')
        self.di._mobile_channel_order_agree(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('买家订单详情')
        self.pa.order_detail(order['content']['orderNo'])
        self.L.logger.debug('卖家订单详情')
        self.di.shopping_order_detail(order['content']['orderNo'])

    def test0041(self):
        """
        张鹏飞:商品订单列表  订单状态,10:待下单, 20:待上门, 30:已结款, 40:已完成, 50: 已取消
        :return:
        """
        self.L.logger.debug("卖家商品订单待处理列表")
        self.di.list_order(20)
        self.L.logger.debug("卖家商品订单待买家收货列表")
        self.di.list_order(30)
        self.L.logger.debug("卖家商品订单已完成列表")
        self.di.list_order(40)
        self.L.logger.debug("卖家商品订单已退款已取消列表")
        self.di.list_order(70)
        self.L.logger.debug("买家商品订单列表")
        self.pa.order_list(10)
        self.pa.order_list(20)
        self.pa.order_list(30)
        self.pa.order_list(40)
        self.pa.order_list((50, 70))

    def test0042(self):
        """
        baiying:苗叔向基地购买商品正向流程
        :return:
        """
        shop_info = self.su.get_shop_id_by_type(self.supplier.user_id)
        shop_id = shop_info.get('content').get('shopId')
        self.supplier.supplier_shop_id = shop_id
        self.L.logger.debug('更新店铺信息')
        shop = Shop(self.supplier)
        self.su.update_shop_info(shop)
        self.L.logger.debug('基地新增商品')
        for i in range(3):
            p = Product(user=self.supplier, product_name=str(i))
            self.su.product_save(p)
        self.L.logger.debug('基地地址')
        address_list = self.su.history_address(shop_id)
        if len(address_list['content']) == 0:
            self.L.logger.debug('基地添加店铺地址')
            self.su._mobile_address_add('xiu', self.buyer.mobile, '41', '4101', '天府五街', 'E3-9', 104.069, 30.539, 1)
        self.L.logger.debug('开始接单')
        self.su.switch_status(shop_id=shop_id)
        self.L.logger.debug('客户端查询地址列表')
        address_list = self.di._mobile_address_list()
        address = address_list['content'][0]
        add_id = address['id']
        self.L.logger.debug('客户端查询店铺信息')
        self.di.get_shop_info_by_id(shop_id)
        self.L.logger.debug('店铺内商品列表')
        product_list = self.pa.get_shop_products_by_shop_id(shop_id)
        p_code = self.pa.tool.get_pro_code_by_pro_list(product_list['content'])
        self.L.logger.debug('添加购物车')
        self.di.cart_add(p_code)
        self.L.logger.debug('购物车列表')
        cart_list = self.di.get_cart_list()
        self.L.logger.debug('购物车结算')
        sure_order = self.di.cart_balance(self.pa.tool.get_cart_ids_by_cart_list(cart_list, shop_id), add_id)
        self.L.logger.debug('确认提交订单')
        order = self.di.submit_order(self.pa.tool.order_info_change(sure_order))
        self.L.logger.debug('苗叔订单详情')
        self.di._mobile_supply_customer_order_detail(order['content']['orderNo'])
        self.L.logger.debug('收银台')
        order_pay_info = self.di.cashier_index(order['content']['tradeNo'])
        self.L.logger.debug('支付')
        self.di.weipay_pay(order['content']['tradeNo'], order_pay_info['content']['channelList'][0]['id'],
                           order_pay_info['content']['amount'])
        self.L.logger.debug('付款')
        self.di.pay_callback(order['content']['tradeNo'], order_pay_info['content']['amount'])
        time.sleep(10)
        self.L.logger.debug('苗叔订单详情')
        self.di._mobile_supply_customer_order_detail(order['content']['orderNo'])
        self.L.logger.debug('基地订单详情')
        self.su._mobile_supply_channel_order_detail(order['content']['orderNo'])
        self.L.logger.debug('苗叔未完成配送前取消订单')
        self.di._mobile_supply_customer_order_apply_refund(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('苗叔订单详情')
        self.di._mobile_supply_customer_order_detail(order['content']['orderNo'])
        self.L.logger.debug('基地订单详情')
        self.su._mobile_supply_channel_order_detail(order['content']['orderNo'])
        self.L.logger.debug('苗叔未完成配送前取消订单')
        self.L.logger.debug('基地拒绝取消订单')
        self.su._mobile_supply_channel_order_refuse(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('苗叔订单详情')
        self.di._mobile_supply_customer_order_detail(order['content']['orderNo'])
        self.L.logger.debug('基地订单详情')
        self.su._mobile_supply_channel_order_detail(order['content']['orderNo'])
        self.L.logger.debug('基地完成配送')
        self.su._mobile_supply_channel_order_finish_send(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('苗叔订单详情')
        self.di._mobile_supply_customer_order_detail(order['content']['orderNo'])
        self.L.logger.debug('基地订单详情')
        self.su._mobile_supply_channel_order_detail(order['content']['orderNo'])
        self.L.logger.debug('苗叔完成配送后取消订单')
        self.di._mobile_supply_customer_order_apply_refund(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('苗叔订单详情')
        self.di._mobile_supply_customer_order_detail(order['content']['orderNo'])
        self.L.logger.debug('基地订单详情')
        self.su._mobile_supply_channel_order_detail(order['content']['orderNo'])
        self.L.logger.debug('基地拒绝取消订单')
        self.su._mobile_supply_channel_order_refuse(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('苗叔订单详情')
        self.di._mobile_supply_customer_order_detail(order['content']['orderNo'])
        self.L.logger.debug('基地订单详情')
        self.su._mobile_supply_channel_order_detail(order['content']['orderNo'])
        self.L.logger.debug('苗叔确认收货')
        self.di._mobile_supply_customer_order_confirm_receive(order['content']['orderNo'])
        time.sleep(10)
        self.L.logger.debug('苗叔订单详情')
        self.di._mobile_supply_customer_order_detail(order['content']['orderNo'])
        self.L.logger.debug('基地订单详情')
        self.su._mobile_supply_channel_order_detail(order['content']['orderNo'])

    def test0043(self):
        """
        张鹏飞:运营后台订单数据
        :return:
        """
        self.op._admin_report_order_pie_sta('2018-12-1', '2018-12-20')
        self.op._admin_report_order_summary_sta('2018-12-1', '2018-12-20')
        self.op._admin_report_service_order_service_data_card('2018-12-1', '2018-12-20')
        self.op._admin_report_service_order_service_data_trend('2018-12-1', '2018-12-20')
        self.op._admin_report_service_order_service_type_distribution('2018-12-1', '2018-12-20')


if __name__ == '__main__':
    Main()
