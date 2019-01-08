#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'yangluyao'
__date__ = '2018/11/14'
"""


from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
from utils.Config import Config


class OperatorAction(object):
    hosts = Config('config').data['hosts'][Config('config').data['run']]

    def __init__(self, operator):
        self.log = Log('OperatorAction')
        self.tool = Tool()
        self.operator = operator
        self.request = Request()
        self.tool = Tool()
        self.ps = 10

    def admin_supplier_unaudited_list(self, status, mobile=None):
        # 苗叔供应商 - 待审核列表(已通)
        bind_data = {"status": status,
                     "mobile": mobile,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/supplier/unaudited-list',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_user_info = self.tool.ms_query_supplier_status(status)
            if query_user_info is not None:
                query_user_info = query_user_info
            for n in range(len(query_user_info)):
                assert query_user_info[n]['mobile'] == json_response['content']['datas'][n]['account']
                # assert query_user_info[n]['create_time'] == json_response['content']['datas'][n]['createTime']
                assert query_user_info[n]['id'] == json_response['content']['datas'][n]['id']
                # assert query_user_info[n]['nickname'] == json_response['content']['datas'][n]['nickname']
                assert query_user_info[n]['user_id'] == json_response['content']['datas'][n]['userId']
                assert query_user_info[n]['status'] == json_response['content']['datas'][n]['status']
                assert query_user_info[n]['statusDesc'] == json_response['content']['datas'][n]['statusDesc']
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_supplier_unaudited_detail(self, user_id):
        # 苗叔供应商-待审核详情(已通)
        bind_data = {"userId": user_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/supplier/unaudited-detail',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_user_info = self.tool.ms_query_supplier_unaudited_detail(user_id)
            if query_user_info is not None:
                query_user_info = query_user_info[0]
            assert query_user_info['mobile'] == json_response['content']['account']
            # assert query_user_info['create_time'] == json_response['content']['createTime']
            assert query_user_info['id'] == json_response['content']['id']
            # assert query_user_info['last_time'] == json_response['content']['lastTime']
            assert query_user_info['nickname'] == json_response['content']['nickname']
            assert query_user_info['positive'] == json_response['content']['positive']
            assert query_user_info['negative'] == json_response['content']['negative']
            assert query_user_info['user_id'] == json_response['content']['userId']
            assert query_user_info['status'] == json_response['content']['status']
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_supplier_audit(self, supplier_id, user_id, name, gender, birthday, id_num, status, province, city,
                             district, address, remark):
        # 苗叔供应商-审核(已通)
        bind_data = {"id": supplier_id,
                     "userId": user_id,
                     "name": name,
                     "gender": gender,
                     "birthday": birthday,
                     "idNum": id_num,
                     "status": status,
                     "province": province,
                     "city": city,
                     "district": district,
                     "address": address,
                     "remark": remark,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/supplier/audit',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_user_info = self.tool.ms_query_supplier_audit(user_id)
            if query_user_info is not None:
                query_user_info = query_user_info[0]
            assert str(query_user_info['id']) == bind_data['id']
            assert str(query_user_info['gender']) == bind_data['gender']
            assert query_user_info['birthday'] == bind_data['birthday']
            assert query_user_info['remark'] == bind_data['remark']
            assert str(query_user_info['user_id']) == bind_data['userId']
            assert query_user_info['province'] == bind_data['province']
            assert query_user_info['city'] == bind_data['city']
            assert query_user_info['address'] == bind_data['address']
            assert str(query_user_info['status']) == bind_data['status']
            assert query_user_info['statusDesc'] == bind_data['statusDesc']
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_supplier_detail(self, user_id):
        # 供应商账号详情(已通)
        bind_data = {"userId": user_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/supplier/detail',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            query_user_info = self.tool.ms_query_supplier_detail(user_id)
            if query_user_info is not None:
                query_user_info = query_user_info[0]
            assert query_user_info['address'] == json_response['content']['address']
            # assert query_user_info['birthday'] == str(json_response['content']['birthday'])
            assert query_user_info['city'] == json_response['content']['city']
            assert query_user_info['gender'] == json_response['content']['gender']
            # assert query_user_info['idNum'] == json_response['content']['idNum']
            assert query_user_info['name'] == json_response['content']['name']
            assert query_user_info['contact'] == json_response['content']['shopContact']
            assert query_user_info['positive'] == json_response['content']['positive']
            assert query_user_info['negative'] == json_response['content']['negative']
            # assert query_user_info['account_status'] == json_response['content']['status']
            assert query_user_info['status'] == json_response['content']['shopStatus']
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_supplier_list(self, status, mobile):
        # 查询供应商账号列表(已通)
        bind_data = {"status": status,
                     "mobile": mobile,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/supplier/list',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_supplier_freeze(self, user_id, reason):
        # 冻结供应商角色(已通)
        bind_data = {"userId": user_id,
                     "reason": reason,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/supplier/freeze',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_supplier_unfreeze(self, user_id, reason):
        # 解冻供应商角色(已通)
        bind_data = {"userId": user_id,
                     "reason": reason,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/supplier/unfreeze',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_channel_unaudited_list(self, status, mobile=None):
        # 苗叔渠道商-待审核列表(已通)
        bind_data = {"status": status,
                     "mobile": mobile,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/channel/unaudited-list', data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def admin_channel_unaudited_detail(self, user_id):
        # 苗叔渠道商-待审核详情(已通)
        bind_data = {"userId": user_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/channel/unaudited-detail', data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def admin_channel_audit(self, supplier_id, user_id, name, gender, birthday, id_num, status, province, city,
                            district, address, remark):
        # 苗叔渠道商-审核(已通)
        bind_data = {"id": supplier_id,
                     "userId": user_id,
                     "name": name,
                     "gender": gender,
                     "birthday": birthday,
                     "idNum": id_num,
                     "status": status,
                     "province": province,
                     "city": city,
                     "district": district,
                     "address": address,
                     "remark": remark,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/channel/audit',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_channel_detail(self, user_id):
        # 供应商账号详情(已通)
        bind_data = {"userId": user_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/channel/detail',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_channel_list(self, status, mobile):
        # 查询渠道商账号列表(已通)
        bind_data = {"status": status,
                     "mobile": mobile,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/channel/list',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_channel_freeze(self, user_id, reason):
        # 冻结渠道商角色()
        bind_data = {"userId": user_id,
                     "reason": reason,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/channel/freeze',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_channel_unfreeze(self, user_id, reason):
        # 解冻渠道商角色()
        bind_data = {"userId": user_id,
                     "reason": reason,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/channel/unfreeze',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_buyer_list(self, status, mobile=None):
        # 查询买家账号列表(已通)
        bind_data = {"status": status,
                     "mobile": mobile,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/buyer/list',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_buyer_detail(self, user_id):
        # 查询买家账号详情(已通)
        bind_data = {"userId": user_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/buyer/detail',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_buyer_freeze(self, user_id, reason):
        # 冻结买家角色()
        bind_data = {"userId": user_id,
                     "reason": reason,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/buyer/freeze',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_buyer_unfreeze(self, user_id, reason):
        # 解冻买家角色()
        bind_data = {"userId": user_id,
                     "reason": reason,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/buyer/unfreeze',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_backstage_list(self, status, mobile=None, real_name=None, email=None):
        # 查询运营后台账号列表(已通)
        bind_data = {"status": status,
                     "mobile": mobile,
                     "realName": real_name,
                     "email": email,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/backstage/list',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_backstage_add(self, mobile, real_name, email):
        # 新建后台账号(已通)
        bind_data = {"mobile": mobile,
                     "realName": real_name,
                     "email": email,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/backstage/add',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_backstage_edit(self, user_id, mobile, real_name, email):
        # 编辑后台账号(已通)
        bind_data = {"userId": user_id,
                     "mobile": mobile,
                     "realName": real_name,
                     "email": email,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/backstage/edit',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_backstage_reset_password(self, user_id):
        # 重置后台帐号密码(已通)
        bind_data = {"userId": user_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/backstage/reset-password',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_backstage_del(self, user_id):
        # 删除后台账号(已通)
        bind_data = {"userId": user_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/backstage/del',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_backstage_freeze(self, user_id, reason):
        # 冻结后台运维账号(已通)
        bind_data = {"userId": user_id,
                     "reason": reason,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/backstage/freeze',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_backstage_unfreeze(self, user_id, reason):
        # 解冻后台运维账号(已通)
        bind_data = {"userId": user_id,
                     "reason": reason,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/backstage/unfreeze',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_category_add(self, category_type, name, category_status, orders=None, parent_id=None,
                           tags=None, category_img=None):
        # 新增分类()
        bind_data = {"type": category_type,
                     "name": name,
                     "categoryStatus": category_status,
                     "orders": orders,
                     "parentId": parent_id,
                     "tags": tags,
                     "imgs": category_img,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/category/add',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_category_list(self, category_type, first_category_id=None, second_category_status=None, name=None):
        # 分类列表(已通)
        bind_data = {"type": category_type,
                     "firstCategoryId": first_category_id,
                     "secondCategoryStatus": second_category_status,
                     "name": name,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/category/list',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_category_edit(self, category_type, category_id, name, category_status, orders, parent_id, tags,
                            category_img):
        # 编辑分类()
        bind_data = {"type": category_type,
                     "category_id": category_id,
                     "name": name,
                     "categoryStatus": category_status,
                     "orders": orders,
                     "parentId": parent_id,
                     "tags": tags,
                     "imgs": category_img,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/category/edit',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_category_detail(self, category_type, category_id):
        # 分类详情(已通)
        bind_data = {"type": category_type,
                     "id": category_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/category/detail',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_category_update_status(self, category_type, category_id, category_status):
        # 分类上下架(已通)
        bind_data = {"type": category_type,
                     "id": category_id,
                     "categoryStatus": category_status,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/category/update-status',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_category_del(self, category_type, category_id):
        # 删除分类(已通)
        bind_data = {"type": category_type,
                     "id": category_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/category/del',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_store_unit_add(self, name):
        # 新增商品单位(已通)
        bind_data = {"name": name,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/store-unit/add',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_store_unit_list(self):
        # 分页获取商品单位(已通)
        bind_data = {"_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/store-unit/list',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_store_unit_edit(self, store_id, name):
        # 编辑商品单位(已通)
        bind_data = {"id": store_id,
                     "name": name,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/store-unit/edit',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_store_unit_detail(self, store_id):
        # 商品单位详情(已通)
        bind_data = {"id": store_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/store-unit/detail',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_store_unit_del(self, store_id):
        # 删除商品单位(已通)
        bind_data = {"id": store_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_PRODUCT'] + '/admin/store-unit/del',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_resource_activity_item_add(self, sort, img_url, width, height, status, jump_url, start_time_str,
                                         end_time_str, remark):
        # 新增活动()
        bind_data = {"sort": sort,
                     "imgUrl": img_url,
                     "width": width,
                     "height": height,
                     "status": status,
                     "jumpUrl": jump_url,
                     "startTimeStr": start_time_str,
                     "endTimeStr": end_time_str,
                     "remark": remark,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_KBMS'] + '/admin/resource-activity/item/add',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_resource_activity_item_list(self):
        # 活动列表()已通
        bind_data = {"_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_KBMS'] + '/admin/resource-activity/item/list',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_resource_activity_item_detail(self, item_id):
        # 活动详情()已通
        bind_data = {"id": item_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_KBMS'] + '/admin/resource-activity/item/detail',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_resource_activity_item_edit(self, item_id, sort, img_url, width, height, status, jump_url, start_time_str,
                                          end_time_str, remark):
        # 编辑活动()已通
        bind_data = {"id": item_id,
                     "sort": sort,
                     "imgUrl": img_url,
                     "width": width,
                     "height": height,
                     "status": status,
                     "jumpUrl": jump_url,
                     "startTimeStr": start_time_str,
                     "endTimeStr": end_time_str,
                     "remark": remark,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_KBMS'] + '/admin/resource-activity/item/edit',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_resource_activity_item_update_status(self, item_id, status):
        # 开始/结束活动()
        bind_data = {"id": item_id,
                     "status": status,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_KBMS'] + '/admin/resource-activity/item/update-status',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_resource_activity_item_del(self, item_id):
        # 删除活动()
        bind_data = {"id": item_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_KBMS'] + '/admin/resource-activity/item/del',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_log_auth_log(self, auth_type, pn, ps, user_id):
        # 获取用户审核日志()已通
        bind_data = {"type": auth_type,
                     "pn": pn,
                     "ps": ps,
                     "userId": user_id,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/log/auth-log',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_log_buyer_log(self, user_id, pn, ps):
        # 获取消费者角色操作日志()已通
        bind_data = {"userId": user_id,
                     "pn": pn,
                     "ps": ps,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/log/buyer-log',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_log_channel_log(self, user_id, pn, ps):
        # 获取渠道商角色操作日志()已通
        bind_data = {"userId": user_id,
                     "pn": pn,
                     "ps": ps,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/log/channel-log',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_log_backstage_log(self, user_id, pn, ps):
        # 获取运维后台操作日志()已通
        bind_data = {"userId": user_id,
                     "pn": pn,
                     "ps": ps,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/log/servicer-log',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_log_supplier_log(self, user_id, pn, ps):
        # 获取供应商操作日志()已通
        bind_data = {"userId": user_id,
                     "pn": pn,
                     "ps": ps,
                     "_tk_": self.operator.token,
                     "_deviceId_": self.operator.deviceId}
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/log/supplier-log',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def channel_detail(self, user_id):
        """
        账号详情(已通)
        :param user_id: 用户ID
        :return:
        """
        data = {
            '_tk_': self.operator.token,
            '_deviceId_': self.operator.deviceId,
            'userId': user_id
        }
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/channel/detail',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def supplier_detail(self, user_id):
        """
        账号详情(已通)
        :param user_id: 用户ID
        :return:
        """
        data = {
            '_tk_': self.operator.token,
            '_deviceId_': self.operator.deviceId,
            'userId': user_id
        }
        response = self.request.post(url=self.hosts['MS_USER'] + '/admin/supplier/detail',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def admin_upload_activity(self, file):
        """
        :param  file: 上传文件路径
        :return: None
        """
        response = self.request.post_file(url='http://192.168.62.253:31020/common/upload-activity',
                                          file_path=file,
                                          data_dict={},
                                          file_key="file")
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            assert json_response["content"]["url"].startswith("http://")
            assert isinstance(json_response["content"]["height"], int)
            assert isinstance(json_response["content"]["width"], int)
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_get_basic_info(self):
        """
        后台系统-后台运营账号管理---获取当前登录后台用户基础信息----已通
        :return:
        """
        bind_data = {}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/backstage/get-basic-info',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _admin_audit_pass(self, id, user_id, positive, negative, name, gender, birthday, id_num, province, city,
                          district, address):
        """
        用户审核通过-杨
        """
        data = {'_tk_': self.operator.token, '_deviceId_': self.operator.deviceId, 'id': id, 'userId': user_id,
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

    def _admin_audit_list(self, pn, ps, status, mobile, apply_role, nickname=None):
        data = {'_tk_': self.operator.token, '_deviceId_': self.operator.deviceId, 'pn': pn, 'ps': ps, 'status': status,
                'mobile': mobile, 'nickname': nickname, 'applyRole': apply_role}
        response = self.request.post(url='http://dev.ms.user.sjnc.com/admin/audit/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def _admin_report_order_pie_sta(self, startDate, endDate):
        data = {'_tk_': self.operator.token, '_deviceId_': self.operator.deviceId, 'startDate': startDate, 'endDate': endDate}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/admin/report/order/pie-sta', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_order_summary_sta(self, startDate, endDate):
        data = {'_tk_': self.operator.token, '_deviceId_': self.operator.deviceId, 'startDate': startDate, 'endDate': endDate}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/admin/report/order/summary-sta', data=data)
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
        data = {'_tk_': self.operator.token, '_deviceId_': self.operator.deviceId, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/admin/report/service-order/service-data-card', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_service_order_service_data_trend(self, startTime, endTime):
        data = {'_tk_': self.operator.token, '_deviceId_': self.operator.deviceId, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.hosts['MS_ORDER'] + '/admin/report/service-order/service-data-trend', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_report_service_order_service_type_distribution(self, startTime, endTime):
        data = {'_tk_': self.operator.token, '_deviceId_': self.operator.deviceId, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.hosts['MS_ORDER'] +
                                         '/admin/report/service-order/service-type-distribution', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")


# if __name__ == '__main__':
#     from backend.Employee import Employee
#     opera = Employee("18919028888", "123456", 1)
#     da = OperatorAction(opera)
    # da.admin_upload_activity("C:/bd_logo1.png")
    # da.admin_supplier_unaudited_list('2')
    # da.admin_supplier_unaudited_detail('1015')
    # da.admin_supplier_audit('10', '80', '测试测试', '2', '1995-11-15', '518387473873832', '4', '四川省', '成都市',
                            # '仁寿县', '高新区', '不知道不知道')
    # da.admin_supplier_detail('1050')
    # da.admin_supplier_audit('11', '1050', '测试关雅馨', '2', '1995-11-15', '518387473873832', '4', '四川省', '成都市',
    # '仁寿县', '高新区', '不知道')
    # da.admin_supplier_detail('1050')
    # da.admin_supplier_list('1', '181113193661')
    # da.admin_supplier_freeze('1050', '不知道')
    # da.admin_supplier_unfreeze('1050', '不知道')
    # da.admin_channel_unaudited_list('2')
    # da.admin_channel_unaudited_detail('1020')
    # da.admin_channel_audit('5', '1052', '陈秀娟测试', '2', '1995-11-15', '518387473873832', '4', '四川省', '成都市',
    # '双流县', '天府新区', '不知道')
    # da.admin_channel_detail('1052')
    # da.admin_channel_list('1','19982917912')
    # da.admin_channel_freeze('1052', '不知道')
    # da.admin_buyer_list('1')
    # da.admin_channel_unfreeze('1052', '不知道不知道')
    # da.admin_buyer_detail('1027')
    # da.admin_backstage_list('1')
    # da.admin_backstage_add('18382373185', '杨露瑶', '1124525691@qq.com')
    # da.admin_backstage_edit('1032', '18382373100', '测试', '42343242@qq.com')
    # da.admin_backstage_reset_password('1034')
    # da.admin_backstage_del('1032')
    # da.admin_backstage_freeze('1034')
    # da.admin_backstage_unfreeze('1032')
    # da.admin_store_unit_add('把')
    # da.admin_store_unit_list()
    # da.admin_store_unit_edit('11', '个')
    # da.admin_store_unit_detail('11')
    # da.admin_store_unit_del('9')
    # da.admin_category_list('2')
    # da.admin_category_detail('1', '20')
    # da.admin_category_update_status('1', '25', '20')
    # da.admin_category_del('2', '25')
    # da.admin_resource_activity_item_add(20,
    #                                     "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/ms-shop/1542273836206.jpg",
    #                                     10, 20, 10, "www.baidu.com", '2018-11-05 15:28:00', '2018-11-15 19:28:00', '哈哈哈')
    # da.admin_resource_activity_item_list()
    # da.admin_resource_activity_item_detail(10)
    # da.admin_resource_activity_item_edit(10,22,
    #                                     "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/ms-shop/1542273836206.jpg",
    #                                     10, 20, 10, "www.baidu.com", '2018-11-05 15:28:00', '2018-11-15 19:28:00', '哈哈哈')
    # da.admin_resource_activity_item_update_status(10, 20)
    # da.admin_resource_activity_item_del(10)
    # da.admin_log_auth_log(8, 1, 20, 76)
    # da.admin_log_buyer_log('9', 1, 20)
    # da.admin_log_channel_log('1059', 1, 20)
    # da.admin_log_backstage_log('76', 1, 20)
    # da.admin_log_supplier_log('1025', 1, 20)
    # da.channel_detail('1059')
    # da.supplier_detail('1025')
    # da.admin_category_del('2', '25')
    # da.admin_log_auth_log('1', '20', '1027')
    # da.admin_log_buyer_log('1027', '1', '20')
    # da.admin_log_channel_log('1020', '1', '20')
    # da.admin_log_supplier_log('1015', '1', '20')
    # da.admin_log_backstage_log('1032', '1', '20')
    # da.admin_get_basic_info()获取当前登录后台用户基础信息
