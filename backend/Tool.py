#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Pengfei'
__date__ = '2018/11/5'
"""


import json
import random
import string
import urllib.parse
from utils.Log import Log
from utils.Util import DataBaseOperate
from utils.Util import Request
from utils.Config import Config
import os
from utils.Util import Redis, RedisNew
from bs4 import BeautifulSoup
import re
# from utils.Util import AndroidTool

host_ip = Config('config').data['detabase'][Config('config').data['run']]['host_ip']


class Tool(object):
    L = Log("Tool")

    def get_images(self, key='farm'):
        redis = Redis()
        # redis.set('get_index', 0)
        get_index = int(redis.get('get_index'))
        response = Request().get(
            'https://www.pexels.com/search/%s/?page=%s&format=html' % (key, str((get_index / 15) + 1)))
        soup = BeautifulSoup(response)
        images = soup.findAll('a', attrs={'href': re.compile("(^https.*)\?")})
        # list_start = get_index
        # list_end = list_start + 15
        i = 0
        for link in images:
            image_url = '%s&auto=compress\n' % link.get('href')
            self.L.logger.debug(image_url)
            image = Request().get(image_url)
            i += 1
            with open('./Images/banner%s.jpg' % str(i), 'wb') as picture:
                picture.write(image)
        # redis.set('get_index', str(list_end))

    def upload_image(self):
        redis = Redis()
        get_index = int(redis.get('get_index')) - 15
        for i in range(1, 16):
            if round((os.path.getsize("./Images/banner"+str(i)+".jpg"))/1000.0/1000.0, 1) < 5:
                Request().post_file(url="http://39.104.28.40:9600/common/farm/upload-img",
                                    file_path="./Images/banner%s.jpg" % str(i), file_key='file')
                # zyp_url = json.loads(response)["content"]
                # redis.set("image%s" % str(get_index + i), zyp_url)
                self.L.logger.debug("image%s uploaded !" % str(get_index + i))
            else:
                self.L.logger.debug("image%s exceed size !" % str(get_index + i))

    @staticmethod
    def miaoshu_query_user_info_by_mobile(mobile, user_type):
        sql = 'SELECT * FROM `ms-user`.t_base_user tu ' \
              'WHERE tu.mobile = %s AND tu.is_delete = 0 AND tu.account_type = %s;' % (str(mobile), str(user_type))
        user_info = DataBaseOperate().operate(host_ip, "ms-user", sql)
        return user_info

    def miaoshu_query_user_info_by_email(email, user_type):
        sql = 'SELECT * FROM t_user WHERE email = %s AND is_delete = 0 AND account_type = %s;' \
              % (str(email), str(user_type))
        user_info = DataBaseOperate().operate(host_ip, "ms-user", sql)
        return user_info

    def ms_delete_user_by_mobile(self, mobile):
        user_info = Tool.miaoshu_query_user_info_by_mobile(mobile, 1)
        if user_info:
            redis = RedisNew()
            user_index = int(redis.get('user_index'))
            DataBaseOperate().operate(host_ip, "ms-user",
                                      'UPDATE t_user SET mobile = "%s" WHERE mobile = "%s";'
                                      % (str(user_index), str(mobile)))
            self.L.logger.debug('原手机号 %s 修改为 %s' % (str(mobile), str(user_index)))
            redis.set('user_index', user_index + 1)
        else:
            raise Exception('手机号输入错误: %s' % str(mobile))

    @staticmethod
    def ms_query_user_address_by_user_id(user_id):
        sql = 'SELECT * FROM t_address WHERE user_id = %s AND is_delete = 0 order by is_default DESC,edit_time DESC;'\
              % (str(user_id))
        address_list_info = DataBaseOperate().operate(host_ip, "ms-user", sql)
        return address_list_info

    @staticmethod
    def ms_query_user_address_by_address_id(address_id):
        sql = 'SELECT * FROM t_address WHERE id = %s;' % (str(address_id))
        address_info = DataBaseOperate().operate(host_ip, "ms-user", sql)
        return address_info

    @staticmethod
    def ms_query_channel_bill_id_by_trade_no(trade_no):
        sql = "SELECT * FROM t_channel_bill WHERE biz_num = %s AND is_delete = 0 order by edit_time;" % ("'" + str(trade_no) + "'")
        pay_list_info = DataBaseOperate().operate(host_ip, "ms-pay", sql)
        return pay_list_info

    @staticmethod
    def ms_query_supplier_supp_update_by_user_id(user_id):
        sql = 'SELECT user_id, positive, negative FROM t_identity_supplier WHERE user_id = %s;' % user_id
        user_info = DataBaseOperate().operate(host_ip, "ms-user", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_shop_get_by_user_id(user_id):
        sql = 'SELECT * FROM t_shop WHERE seller_id = %s;' % user_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_update_shop_info_by_user_id(user_id):
        sql = 'SELECT name, mobile, contact, avatar FROM t_shop WHERE seller_id = %s;' % user_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_update_address_by_shop_id(shop_id):
        sql = 'SELECT province,city,area,address FROM t_shop_ext_supplier WHERE shop_id = %s;' % shop_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_switch_status_by_shop_id(shop_id):
        sql = 'SELECT status FROM t_shop WHERE id = %s;' % shop_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_category_list_all_by_status(status):
        sql = 'SELECT count(*) FROM t_category WHERE `status` = %s;' % status
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_category_list_by_category_id(category_id):
        sql = 'SELECT count(*) FROM t_category WHERE `status` = 10 AND parent= %s;' % category_id
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_store_unit_list_by_is_delete(is_delete):
        sql = 'SELECT count(*) FROM t_store_unit WHERE is_delete= %s;' % is_delete
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_freight_template_all_by_shop_id(shop_id):
        sql = 'SELECT count(*) FROM t_freight_template WHERE shop_id= %s AND is_delete=0;' % shop_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_freight_template_add_by_freight_id(freight_id):
        sql = 'SELECT id, shop_id, title, freigh_per_km, free_price, free_distance, free_price_status, ' \
              'free_distance_status  FROM t_freight_template WHERE id= %s;' % freight_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_freight_template_delete_by_freight_id(freight_id):
        sql = 'SELECT id, shop_id, is_delete FROM t_freight_template WHERE id= %s;' % freight_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_freight_template_edit_by_freight_id(freight_id):
        sql = 'SELECT id, title, freigh_per_km, free_price, free_distance, free_price_status,' \
              'free_distance_status FROM t_freight_template WHERE id= %s;' % freight_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_freight_template_get_by_freight_id(freight_id):
        sql = 'SELECT id, title, freigh_per_km, free_price, free_distance, free_price_status,' \
              'free_distance_status FROM t_freight_template WHERE id= %s;' % freight_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_status(status):
        sql = '''SELECT tus.mobile, tis.create_time,tis.id, tus.nickname, tis.`status`,tis.user_id,
                 CASE tis.`status`WHEN 2 THEN	'审核中'WHEN 3 THEN	'未通过'END AS statusDesc
                 FROM	`ms-user`.t_user tus
                 LEFT JOIN `ms-user`.t_identity_supplier tis ON tis.user_id = tus.id
                 WHERE	tis.`status` = %s order by tis.create_time DESC ''' % str(status)
        user_info = DataBaseOperate().operate(host_ip, "ms-user", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_unaudited_detail(user_id):
        sql = '''SELECT tus.mobile,tis.create_time,tis.id,	tis.last_time, tus.nickname, tis.positive, tis.negative, 
                 tis.`status`,tis.user_id,
                 CASE tis.`status`WHEN 2 THEN	'审核中'WHEN 3 THEN	'未通过'END AS statusDesc
                 FROM	`ms-user`.t_user tus
                 LEFT JOIN `ms-user`.t_identity_supplier tis ON tis.user_id = tus.id
                 WHERE	tis.`user_id` = %s''' % str(user_id)
        user_info = DataBaseOperate().operate(host_ip, "ms-user", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_audit(user_id):
        sql = '''SELECT tis.id, tis.user_id, tis.`name`, tis.gender, tis.birthday, tis.province, tis.city,tis.address, 
                 tis.`status`, top.remark,
                 CASE tis.`status`WHEN 2 THEN	'审核中'WHEN 3 THEN	'未通过'WHEN 4 THEN	'审核通过'END AS statusDesc
                 FROM	`ms-user`.t_user tus
                 LEFT JOIN `ms-user`.t_identity_supplier tis ON tis.user_id = tus.id
                 LEFT JOIN `ms-user`.t_user_operate_log top ON top.user_id = tus.id
                 WHERE	tis.user_id = %s''' % str(user_id)
        user_info = DataBaseOperate().operate(host_ip, "ms-user", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_detail(user_id):
        sql = '''SELECT tis.address, tis.birthday, tis.city, tis.create_time, tis.district, tis.gender,
                 tis.id_num, tis.last_time, tus.mobile, tis.`name`, tis.negative, tus.nickname, tis.auth_time, 
                 tis.positive, tis.province, tsh.contact, tsh.id, tsh.mobile, tsh.`name`, tsh.`status`, tus.account_status,
                 CASE tus.account_status WHEN 1 THEN	'正常'WHEN 2 THEN	'冻结'END AS statusDesc,
                 CASE tsh.`status`WHEN 10 THEN	'接单'WHEN 20 THEN	'休息'END AS statusDesc
                 FROM	`ms-user`.t_user tus
                 LEFT JOIN `ms-user`.t_identity_supplier tis ON tis.user_id = tus.id
                 LEFT JOIN `ms-shop`.t_shop tsh ON tsh.seller_id = tus.id
                 WHERE	tis.user_id = %s''' % str(user_id)
        user_info = DataBaseOperate().operate(host_ip, "ms-user", sql)
        return user_info

    @staticmethod
    def ms_query_channel_zz_by_user_id(user_id):
        sql = 'SELECT * FROM t_identity_channel WHERE user_id = %s;' % user_id
        user_info = DataBaseOperate().operate(host_ip, "ms-user", sql)
        return user_info

    @staticmethod
    def ms_query_shop_info_by_seller_id(seller_id, current=True):
        if current:
            sql = 'SELECT ta.address, ta.area, ta.city, ta.lat, ta.lng, ta.province, ta.shop_id, ' \
              'ts.avatar, ts.contact, ts.mobile, ts.`name`, IFNULL(tpv.pv,0) pv, ts.seller_id, ts.`status`, ts.type  ' \
              'FROM `ms-shop`.t_shop ts ' \
              'LEFT JOIN `ms-shop`.t_address ta ON ta.shop_id = ts.id ' \
              'LEFT JOIN t_page_view AS tpv ON tpv.shop_id = ts.id  ' \
              'WHERE ta.`status`=10 and ts.seller_id = %s;' % seller_id
        else:
            sql = 'SELECT ta.address, ta.area, ta.city, ta.lat, ta.lng, ta.province, ta.shop_id, ' \
              'ts.avatar, ts.contact, ts.mobile, ts.`name`, IFNULL(tpv.pv,0) pv, ts.seller_id, ts.`status`, ts.type  ' \
                  'FROM `ms-shop`.t_shop ts ' \
                  'LEFT JOIN `ms-shop`.t_address ta ON ta.shop_id = ts.id ' \
                  'LEFT JOIN t_page_view AS tpv ON tpv.shop_id = ts.id  ' \
                  'WHERE ts.seller_id = %s;' % seller_id
        get_shop_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return get_shop_info

    @staticmethod
    def ms_query_update_shop_info_by_seller_id(seller_id):
        sql = 'SELECT  mobile,contact,status,name FROM t_shop WHERE seller_id=%s;' % seller_id
        get_shop_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return get_shop_info

    @staticmethod
    def ms_query_latest_address_info_by_shop_id(shop_id):
        sql = 'SELECT id,shop_id, lng,lat,province,city,area,address FROM t_address WHERE shop_id=%s AND' \
              '`status` = 10 ;' % shop_id
        get_address_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return get_address_info

    @staticmethod
    def ms_query_all_address_info_by_shop_id(shop_id):
        sql = 'SELECT id,shop_id, lng,lat,province,city,area,address,`status` FROM t_address WHERE shop_id=%s ' \
              'ORDER BY id DESC' % shop_id
        get_address_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return get_address_info

    @staticmethod
    def ms_query_channel_product_info_by_shop_id(shop_id):
        sql = 'SELECT 	tp.`name`, tp.shop_id,tp.price, tp.store_unit_id, tp.store,' \
              ' tp.`status`, tp.service_type, tp.create_time, tpi.content ' \
              'FROM 	`ms-product`.t_product tp ' \
              'LEFT JOIN `ms-product`.t_product_info tpi ' \
              'ON tpi.product_id=tp.id WHERE tp.shop_id = %s ' \
              'ORDER BY tp.create_time desc' % shop_id
        add_product_info = DataBaseOperate().operate("39.104.28.40", "ms-product", sql)
        return add_product_info

    @staticmethod
    def ms_query_seller_order_info_by_order_no(order_no):
        sql = "SELECT o.content, o.door_address, unix_timestamp(o.door_time)*1000 door_time, oi.pay_status, " \
              "oi.price_real, o.earnest_money_price, o.tail_money_price,"\
              "oi.trade_no, oi.order_type,o.order_status, CASE o.order_status WHEN 10 THEN '待下单' WHEN 20 THEN '待上门'"\
              " WHEN 30 THEN '待结款' WHEN 40 THEN '已完成' WHEN 50 THEN '已取消' END AS orderStatusDesc, u.mobile, " \
              "o.service_type, CASE WHEN (oi.order_type = 10 AND oi.pay_status = 10) THEN 10 WHEN (oi.order_type = 10"\
              " AND oi.pay_status = 20 ) THEN 20 END AS earnestMoneyPayStatus, CASE WHEN ( oi.order_type = 20 AND " \
              "oi.pay_status = 10 ) THEN 10 WHEN ( oi.order_type = 20 AND oi.pay_status = 20) THEN 20 END AS " \
              "tailMoneyPayStatus FROM `ms-order`.t_service_order o LEFT JOIN `ms-order`.t_service_order_item oi " \
              "ON o.id = oi.order_id LEFT JOIN `ms-user`.t_base_user u ON u.id = o.buyer_id WHERE o.order_no = '%s' " \
              "order by oi.create_time;" % order_no
        order_info = DataBaseOperate().operate(host_ip, "ms-order", sql)
        return order_info

    @staticmethod
    def ms_query_buyer_order_info_by_order_no(order_no):
        sql = "SELECT o.content, o.door_address, unix_timestamp(o.door_time)*1000 door_time, oi.pay_status, " \
              "oi.price_real, o.earnest_money_price, o.tail_money_price,"\
              "oi.trade_no, oi.order_type,o.order_status, CASE o.order_status WHEN 10 THEN '待下单' WHEN 20 THEN '待上门'"\
              " WHEN 30 THEN '待结款' WHEN 40 THEN '已完成' WHEN 50 THEN '已取消' END AS orderStatusDesc, u.mobile, " \
              "o.service_type, CASE WHEN (oi.order_type = 10 AND oi.pay_status = 10) THEN 10 WHEN (oi.order_type = 10"\
              " AND oi.pay_status = 20 ) THEN 20 END AS earnestMoneyPayStatus, CASE WHEN ( oi.order_type = 20 AND " \
              "oi.pay_status = 10 ) THEN 10 WHEN ( oi.order_type = 20 AND oi.pay_status = 20) THEN 20 END AS " \
              "tailMoneyPayStatus FROM `ms-order`.t_service_order o LEFT JOIN `ms-order`.t_service_order_item oi " \
              "ON o.id = oi.order_id LEFT JOIN `ms-user`.t_base_user u ON u.id = o.seller_id WHERE o.order_no = '%s' " \
              "order by oi.create_time;" % order_no
        order_info = DataBaseOperate().operate(host_ip, "ms-order", sql)
        return order_info

    @staticmethod
    def ms_query_seller_id_order_list_by_user_id(user_id, order_status, ps, pn):
        sql = "SELECT 	o.order_no orderNo, 	o.order_status orderStatus, CASE 	o.order_status 	WHEN 10 THEN '待下单'" \
              "	WHEN 20 THEN 	'待上门' 	WHEN 30 THEN 	'待结款' 	WHEN 40 THEN 	'已完成' 	WHEN 50 THEN '已取消'" \
              "	END AS orderStatusDesc, CASE 	WHEN ( oi.order_type = 10 AND oi.pay_status = 10 ) THEN 	'未支付定金' 	" \
              "WHEN ( oi.order_type = 10 AND oi.pay_status = 20 ) THEN 	'已支付定金' 	WHEN ( oi.order_type = 20 AND " \
              "oi.pay_status = 20 ) THEN 	'未支付尾款' 	WHEN ( oi.order_type = 20 AND oi.pay_status = 20 ) " \
              "THEN 	'已支付尾款' 	END AS payStatusDesc, 	o.earnest_money_price, 	o.tail_money_price, 	" \
              "bu.mobile buyerMobile, CASE 		o.service_type 		WHEN 10 THEN 		'苗叔上门种植服务' 		" \
              "WHEN 20 THEN 		'苗叔上门养护服务' 	END AS serviceTypeDesc, 	o.shop_name shopName FROM 	" \
              "`ms-order`.t_service_order o 	LEFT JOIN `ms-order`.t_service_order_item oi ON o.id = oi.order_id " \
              "	LEFT JOIN `ms-user`.t_base_user u ON u.id = o.seller_id 	LEFT JOIN `ms-user`.t_base_user bu ON " \
              "bu.id = o.buyer_id WHERE 	u.id = %s 	AND o.order_status = %s GROUP BY oi.order_id " \
              "ORDER BY o.create_time DESC LIMIT %s, %s" % (user_id, order_status, (pn-1)*ps, ps)
        order_list = DataBaseOperate().operate(host_ip, "ms-order", sql)
        return order_list

    @staticmethod
    def ms_query_buyer_shop_order_detail_by_order_no(order_no):
        """
        张鹏飞:买家查看商品订单详情
        :param order_no: 订单编号
        :return:
        """
        sql = "SELECT o.apply_status applyStatus, CASE o.apply_status WHEN 10 THEN '申诉' WHEN 20 THEN '已取消' " \
              "WHEN 30 THEN '卖家拒绝取消订单' end as applyStatusDesc, o.order_no, tu.id buyerId, tu.head_img buyerHeadImg," \
              " o.buyer_name, u.id 卖家ID, o.seller_name, unix_timestamp(o.create_time)* 1000 createTime, " \
              "CASE o.order_status WHEN 10 THEN '待付款' WHEN 20 THEN '待收货' WHEN 30 THEN '待收货' WHEN 40 THEN '交易成功' " \
              "WHEN 50 THEN '已取消' WHEN 70 THEN '已取消' END AS orderStatusDesc, o.order_status orderStatus, " \
              "unix_timestamp(o.pay_time)* 1000 payTime, o.price_real priceReal, " \
              "unix_timestamp(o.receive_time)* 1000 receiveTime, tsp.`name` shopName, tod.send_mobile sendMobile," \
              "o.price_total priceTotal, o.freight, tos.product_id 商品ID, tps.price 商品单价, tos.sku_num 商品数量, " \
              "tod.receive_address receiveAddress, tod.receive_lng receiveLng, tod.receive_lat receiveLat, " \
              "tod.receive_mobile receiveMobile, tod.receive_name receiveName, tod.send_name sendName, " \
              "tsp.contact shopContact, tsp.mobile shopContactMobile, unix_timestamp(o.valid_date)* 1000 validDate, " \
              "o.trade_no tradeNo FROM `ms-order`.`t_order` o LEFT JOIN `ms-user`.`t_base_user` tu ON " \
              "tu.id = o.buyer_id LEFT JOIN `ms-user`.`t_base_user` u ON u.id = o.seller_id " \
              "LEFT JOIN `ms-order`.`t_order_item` tos ON tos.order_id = o.id " \
              "LEFT JOIN `ms-product`.`t_product_snapshot` tps ON tos.snapshot_id = tps.id " \
              "LEFT JOIN `ms-order`.`t_order_delivery` tod ON tod.order_id = o.id " \
              "LEFT JOIN `ms-shop`.`t_shop` tsp ON tsp.id = o.shop_id WHERE o.order_no = '%s';" % order_no
        order_detail = DataBaseOperate().operate(host_ip, "ms-order", sql)
        return order_detail

    @staticmethod
    def ms_query_seller_shop_order_detail_by_order_no(order_no):
        """
        张鹏飞:卖家查看商品订单详情
        :param order_no: 订单编号
        :return:
        """
        sql = "SELECT o.apply_status applyStatus, CASE o.apply_status WHEN 10 THEN '买家申请取消订单' WHEN 20 THEN '已取消' " \
              "WHEN 30 THEN '已拒绝' end as applyStatusDesc, o.order_no, tu.id buyerId, tu.head_img buyerHeadImg, " \
              "o.buyer_name, u.id 卖家ID, o.seller_name, unix_timestamp(o.create_time)* 1000 createTime, " \
              "CASE o.order_status WHEN 10 THEN '等待买家待付款' WHEN 20 THEN '待处理' WHEN 30 THEN '等待买家确认收货' " \
              "WHEN 40 THEN '已完成' WHEN 50 THEN '已取消' WHEN 70 THEN '已取消' END AS orderStatusDesc, " \
              "o.order_status orderStatus, o.price_total priceTotal, unix_timestamp(o.pay_time)* 1000 payTime, " \
              "o.price_real, o.freight, tos.product_id 商品ID, tps.price 商品单价, tos.sku_num 商品数量, " \
              "tod.receive_address receiveAddress, tod.receive_lng receiveLng, tod.receive_lat receiveLat, " \
              "tod.receive_mobile receiveMobile, tod.receive_name receiveName, unix_timestamp(o.receive_time)* 1000 " \
              "receiveTime, tod.send_name sendName, tod.send_mobile sendMobile, tsp.contact shopContact, " \
              "tsp.mobile shopContactMobile, tsp.`name` shopName, unix_timestamp(o.valid_date)* 1000 validDate, " \
              "o.trade_no tradeNo FROM `ms-order`.`t_order` o " \
              "LEFT JOIN `ms-user`.`t_base_user` tu ON tu.id = o.buyer_id " \
              "LEFT JOIN `ms-user`.`t_base_user` u ON u.id = o.seller_id " \
              "LEFT JOIN `ms-order`.`t_order_item` tos ON tos.order_id = o.id " \
              "LEFT JOIN `ms-product`.`t_product_snapshot` tps ON tos.snapshot_id = tps.id " \
              "LEFT JOIN `ms-order`.`t_order_delivery` tod ON tod.order_id = o.id " \
              "LEFT JOIN `ms-shop`.`t_shop` tsp ON tsp.id = o.shop_id WHERE o.order_no = '%s'" % order_no
        order_detail = DataBaseOperate().operate(host_ip, "ms-order", sql)
        return order_detail

    @staticmethod
    def ms_query_channel_product_category_info_by_id_delete(is_delete):
        sql = 'SELECT id,`name`,parent FROM t_category WHERE is_delete=%s ORDER BY id DESC' % is_delete
        product_category_info = DataBaseOperate().operate("39.104.28.40", "ms-product", sql)
        return product_category_info

    @staticmethod
    def ms_query_channel_search_product_by_product_code(pcode):
        sql = 'SELECT tp.pcode,tp.category_id,tp.full_name,tp.pcode,tp.price,tp.sales,tp.shop_id,tp.`status`,' \
              'tp.store,tp.store_unit_id,tc.parent,tc.name,tpi.content,tpi.freight_id,tpm.url ' \
              'FROM `ms-product`.t_product tp ' \
              'LEFT JOIN `ms-product`.t_category tc ON tp.category_id=tc.id ' \
              'LEFT JOIN `ms-product`.t_product_info tpi ON tp.id=tpi.product_id ' \
              'LEFT JOIN `ms-product`.t_product_img tpm ON tp.id=tpm.product_id ' \
              'LEFT JOIN `ms-product`.t_store_unit tsu ON tp.store_unit_id=tsu.id ' \
              'WHERE tp.pcode=%s;' % pcode
        product_info = DataBaseOperate().operate("39.104.28.40", "ms-product", sql)
        return product_info
        sql = 'SELECT id,shop_id, lng,lat,province,city,area,address,`status` FROM t_address WHERE shop_id=%s ' \
              'ORDER BY id DESC' % shop_id
        get_address_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return get_address_info

    @staticmethod
    def ms_query_supplier_shop_get_by_user_id(user_id):
        sql = 'SELECT * FROM t_shop WHERE seller_id = %s;' % user_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_update_shop_info_by_user_id(user_id):
        sql = 'SELECT name, mobile, contact, avatar FROM t_shop WHERE seller_id = %s;' % user_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_update_address_by_shop_id(shop_id):
        sql = 'SELECT province,city,area,address FROM t_shop_ext_supplier WHERE shop_id = %s;' % shop_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_switch_status_by_shop_id(shop_id):
        sql = 'SELECT status FROM t_shop WHERE id = %s;' % shop_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_category_list_all_by_status(status):
        sql = 'SELECT count(*) FROM t_category WHERE `status` = %s;' % status
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_category_list_by_category_id(category_id):
        sql = 'SELECT count(*) FROM t_category WHERE `status` = 10 AND parent= %s;' % category_id
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_store_unit_list_by_is_delete(is_delete):
        sql = 'SELECT count(*) FROM t_store_unit WHERE is_delete= %s;' % is_delete
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_freight_template_all_by_shop_id(shop_id):
        sql = 'SELECT count(*) FROM t_freight_template WHERE shop_id= %s AND is_delete=0;' % shop_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_freight_template_add_by_freight_id(freight_id):
        sql = 'SELECT id, shop_id, title, freigh_per_km, free_price, free_distance, free_price_status, ' \
              'free_distance_status  FROM t_freight_template WHERE id= %s;' % freight_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_freight_template_delete_by_freight_id(freight_id):
        sql = 'SELECT id, shop_id, is_delete FROM t_freight_template WHERE id= %s;' % freight_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_freight_template_edit_by_freight_id(freight_id):
        sql = 'SELECT id, title, freigh_per_km, free_price, free_distance, free_price_status,' \
              'free_distance_status FROM t_freight_template WHERE id= %s;' % freight_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_freight_template_get_by_freight_id(freight_id):
        sql = 'SELECT id, title, freigh_per_km, free_price, free_distance, free_price_status,' \
              'free_distance_status FROM t_freight_template WHERE id= %s;' % freight_id
        user_info = DataBaseOperate().operate(host_ip, "ms-shop", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_product_save_by_shop_id(shop_id):
        sql = 'SELECT t_product.id, t_product.category_id, t_product.name, t_product.store_unit_id, ' \
              't_product_info.content, t_product.price, t_product.store, t_product_info.freight_id, ' \
              't_product.STATUS, t_product.service_type, t_product_img.url FROM t_product, t_product_info,' \
              ' t_product_img WHERE t_product_info.product_id = t_product.id and ' \
              't_product_img.product_id = t_product.id and t_product.id=(select MAX(id) from t_product)' \
              'and t_product.shop_id=%s;' % shop_id
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_product_list_by_shop_id(shop_id):
        sql = 'SELECT count(*) FROM t_product WHERE shop_id= %s;' % shop_id
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_status_update_by_product_pcode(product_pcode):
        sql = 'SELECT pcode, status, is_delete  FROM t_product WHERE pcode= %s;' % product_pcode
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_product_update_by_pcode(pcode):
        sql = 'SELECT t_product.id, t_category.parent,t_product.category_id,t_product.name,t_product.store_unit_id, ' \
              't_product_info.content, t_product.price, t_product.store, t_product_info.freight_id, ' \
              't_product.STATUS, t_product.service_type, t_product_img.url FROM t_product, t_product_info,t_category,' \
              ' t_product_img WHERE t_product_info.product_id = t_product.id AND ' \
              't_product_img.product_id = t_product.id AND t_category.id = t_product.category_id AND' \
              ' t_product.pcode =%s;' % pcode
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_store_list_by_shop_id(shop_id):
        sql = 'SELECT count(*) FROM t_product WHERE shop_id= %s;' % shop_id
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_supplier_store_update_by_pcode(pcode_list):
        sql = 'SELECT pcode, store FROM t_product WHERE pcode in %s;' % pcode_list
        user_info = DataBaseOperate().operate(host_ip, "ms-product", sql)
        return user_info

    @staticmethod
    def ms_query_city_list_by_parent_id(parent_id=0):
        sql = 'SELECT `id`,`name` FROM `ms-kbms`.t_region te WHERE te.parent_id= %s' % str(parent_id)
        city_list = DataBaseOperate().operate("39.104.28.40", "ms-kbms", sql)
        return city_list

    @staticmethod
    def ms_shop_t_address_list_by_shop_id(shop_id):
        sql = 'SELECT * FROM `ms-shop`.t_address WHERE shop_id = %s and status=10' % str(shop_id)
        shop_list = DataBaseOperate().operate("39.104.28.40", "ms-shop", sql)
        return shop_list

    @staticmethod
    def ms_mobile_plant_add_by_room_id(room_id):
        sql = 'SELECT t_room.home_id,t_plant.room_id,t_plant.plant_wiki_id,t_plant.plant_name,t_plant.water_cycle_time,' \
              't_plant.img_url FROM `ms-plant`.t_room,`ms-plant`.t_plant WHERE t_plant.room_id=t_room.id AND ' \
              't_plant.room_id = %s ORDER BY t_plant.id DESC' % room_id
        plant_list = DataBaseOperate().operate("39.104.28.40", "ms-plant", sql)
        return plant_list[0]


    @staticmethod
    def test():
        redis = Redis()
        for i in range(160):
            j = redis.get("image%s" % str(i))
            if j is None:
                print("image%s" % str(i))
            else:
                pass

    @staticmethod
    def get_short_massage_code(mobile):
        data_sso = Config('Sso').data
        data = data_sso['http://192.168.62.253:31007']['/mobile/sso/verify-code-get']
        data["mobile"] = mobile
        code = Request().post(url="http://192.168.62.253:31007/mobile/sso/verify-code-get", data=data)
        Tool.L.logger.debug("手机号 %s 发送验证码成功" % str(mobile))
        return Redis().get('VerifyCodeMobile: SmsVerifyCode:9_REGISTER_%s' % str(mobile))

    @staticmethod
    def order_info_change(order_info):
        if order_info['status'] == 'OK':
            order = {
                "shopId": order_info['content'].get('shop').get('shopId'),
                "sellerId": order_info['content'].get('shop').get('sellerId'),
                "addressId": order_info['content'].get('shippingAddressDto').get('id'),
                "freight": order_info['content'].get('deliveryPrice'),
                "productPrice": order_info['content'].get('totalPrice'),
                "isCheck": 0
            }
            products = []
            for i in order_info["content"].get("products"):
                product = {}
                if i.get("cartId") is not None:
                    product['cartId'] = i.get("cartId")
                if i.get("pcode") is not None:
                    product["pCode"] = str(i.get("pcode"))
                    product["num"] = str(i.get("amount"))
                if i.get("imgs") != [] and i.get("imgs") is not None:
                    product['image'] = i.get("imgs")[0]
                if product != {}:
                    products.append(product)

            products = urllib.parse.quote(str(products), safe=string.printable)
            order["product"] = products
            return order
        else:
            return False

    @staticmethod
    def get_cart_ids_by_cart_list(cart_list, shop_id):
        if cart_list['status'] == 'OK':
            shop_list = cart_list['content']['shopItem']
            for j in shop_list:
                if j['shopId'] == shop_id:
                    cart_id_list = []
                    for i in j['products']:
                        cart_id_list.append(i['cartId'])
                    return cart_id_list
        else:
            return False

    @staticmethod
    def get_pro_code_by_pro_list(pro_list):
        for i in pro_list:
            if i['productList'] != '[]':
                for j in i['productList']:
                    if j['store'] != 0:
                        return j['pcode']
        return "未找到有库存的商品"
