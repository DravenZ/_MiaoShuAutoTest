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

    def _admin_config_add(self, code, key, value, description, is_delete, status):
        """
        杨露瑶: 新增配置
        :param code:
        :param key:
        :param value:
        :param description:
        :param isDelete:
        :param status:
        :return:
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'code': code, 'key': key, 'value': value,
                'description': description, 'isDelete': is_delete, 'status': status}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/config/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_config_detail(self, id):
        """
        杨露瑶: 获取配置详情
        :param id:
        :return:
        """
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
        """
        杨露瑶: 修改配置
        :param id:
        :param code:
        :param key:
        :param value:
        :param description:
        :param status:
        :return:
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id, 'code': code, 'key': key,
                'value': value, 'description': description, 'status': status}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/config/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_config_list(self, pn, ps, code=None, description=None):
        """
        杨露瑶: 获取配置列表
        :param code:
        :param description:
        :param pn:
        :param ps:
        :return:
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'code': code, 'description': description,
                'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/config/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_config_list_config_by_code(self, code):
        """
        杨露瑶: 查询字典值
        :param code:
        :return:
        """
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
        """
        杨露瑶: 选中病症名查看详情
        :param id:
        :return:
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/plant-disease/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_plant_disease_import(self):
        """
        杨露瑶: 从Excel导入植物病虫害知识库
        :return:
        """
        response = self.request.post_file(url='http://dev.ms.kbms.sjnc.com/admin/plant-disease/import?'
                                              '_tk_=%s&_deviceId_=%s' % (self.kbms.token, self.kbms.deviceId),
                                          file_key="file",
                                          file_path="./../picture/plantdisease.xls")
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_plant_disease_list_hot(self):
        """
        杨露瑶: 热门病症
        :return:
        """
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
        """
        杨露瑶: 关键词模糊联想病症名称列表
        :param search:
        :param pn:
        :param ps:
        :return: 返回病症id
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'search': search, 'pn': pn, 'ps': ps}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/plant-disease/name-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_plant_import(self):
        """
        杨露瑶: 从Excel导入植物特性知识库
        :param file:
        :return:
        """
        # data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id}
        # response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/plant/import', data=data)
        response = self.request.post_file(url='http://dev.ms.kbms.sjnc.com/admin/plant/import?'
                                              '_tk_=%s&_deviceId_=%s' % (self.kbms.token, self.kbms.deviceId),
                                          file_key="file",
                                          file_path="./../picture/植物特性表.xls")
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_resource_activity_item_add(self, type, sort, img_url, width, height, status, jump_url, start_time_str,
                                          end_time_str, remark):
        """
        杨露瑶: 新增活动
        :param type: 类型(10:我的苗叔 20:我的基地)
        :param sort:
        :param img_url:
        :param width:
        :param height:
        :param status: 状态（10生效20关闭）
        :param jump_url: 跳转路径
        :param start_time_str: 开始时间 yyyy-MM-dd HH:mm:ss
        :param end_time_str: 开始时间 yyyy-MM-dd HH:mm:ss
        :param remark:
        :return:
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'type': type, 'sort': sort,
                'imgUrl': img_url, 'width': width, 'height': height, 'status': status, 'jumpUrl': jump_url,
                'startTimeStr': start_time_str, 'endTimeStr': end_time_str, 'remark': remark}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/resource-activity/item/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_resource_activity_item_del(self, id):
        """
        杨露瑶: 删除活动
        :param id:
        :return:
        """
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
        """
        杨露瑶: 活动详情
        :param id:
        :return:
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/resource-activity/item/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_resource_activity_item_edit(self, id, type, sort, img_url, width, height, status, jump_url,
                                           start_time_str, end_time_str, remark):
        """
        杨露瑶: 编辑活动
        :param id:
        :param type:
        :param sort:
        :param img_url:
        :param width:
        :param height:
        :param status:
        :param jump_url:
        :param start_time_str:
        :param end_time_str:
        :param remark:
        :return:
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'id': id, 'type': type, 'sort': sort,
                'imgUrl': img_url, 'width': width, 'height': height, 'status': status, 'jumpUrl': jump_url,
                'startTimeStr': start_time_str, 'endTimeStr': end_time_str, 'remark': remark}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/resource-activity/item/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_resource_activity_item_list(self, type, pn, ps):
        """
        杨露瑶: 活动列表
        :param type:
        :param pn:
        :param ps:
        :return: 返回活动id
        """
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
        """
        杨露瑶: 开始/结束活动
        :param id:
        :param status: 状态（10生效20关闭)
        :return:
        """
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
        """
        杨露瑶: 文件最后上传记录
        :param type: 上传文件类型（1：植物库；2：病虫害库)
        :return:
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'type': type}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/admin/upload-log/last', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _common_upload_activity(self):
        """
        杨露瑶: 上传活动图片,并返回宽和高
        :return:
        """
        # data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'file': file}
        # response = self.request.post(url='http://dev.ms.kbms.sjnc.com/common/upload-activity', data=data)
        response = self.request.post_file(url='http://dev.ms.kbms.sjnc.com/common/upload-activity',
                                          file_path='./../picture/1.png', file_key='file', data_dict=None)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_city_list(self, pid):
        """
        杨露瑶: 城市列表（pid为空查询所有省份，否则查询对应区域下的数据)
        :param pid:
        :return:
        """
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
        """
        杨露瑶: 客服电话
        :return:
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/config/common/get-service-phone', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_app_version_get(self, app_id):
        """
        杨露瑶: 获取版本更新信息
        :param app_id:
        :return:
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id, 'appId': app_id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/mobile/app/version/get', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_plant_detail(self, id):
        """
        杨露瑶: 植物详情
        :param id:
        :return:
        """
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
        """
        杨露瑶: 关键词模糊查询植物列表
        :param search:
        :param pn:
        :param ps:
        :return:
        """
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
        """
        杨露瑶: 苗叔页面banner
        :return: 苗叔banner url
        """
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
        """
        杨露瑶: 基地页面banner
        :return: 基地banner url
        """
        data = {'_tk_': self.kbms.token, '_deviceId_': self.kbms.device_id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/mobile/resource-activity/item/supplier-list',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")


if __name__ == '__main__':
    from backend.Session import EmployeeSession
    emp = EmployeeSession('18382373185', 'o8h85G')
    kb = kbmsAction(emp)
# if __name__ == '__main__':
#     from backend.Session import EmployeeSession
#     emp = EmployeeSession('18382373185', 'o8h85G')
    # kb = kbmsAction(emp)
    # kb._config_common_get_city_list('41')
    # kb._config_common_get_service_phone(
    # kb._mobile_app_version_get('01'). _admin_resource_activity_item_add
    # kb. _admin_resource_activity_item_add('10', '10', 'kbms/activity/img/1544146751218.jpg', '500', '375', '10',
    #                                       'http://qa.ms.admin.sjnc.com/login?from=%2Fmanage', '2018-12-18 15:11:11',
    #                                       '2018-12-18 18:12:16', '测试')
    # kb. _admin_resource_activity_item_edit('25', '10', '8', 'http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/'
    #                                        'data/ms-kbms/activity/img/1544146751218.jpg', '500', '375', '10', 'http://'
    #                                        'qa.ms.admin.sjnc.com/login?from=%2Fmanage', '2018-12-17 15:11:11',
    #                                        '2018-12-18 18:12:16', '测试')
    # kb._admin_resource_activity_item_list(10, 1, 20)
    # kb._admin_resource_activity_item_detail(25)
    # kb._admin_resource_activity_item_update_status(25, 10)
    # kb._admin_resource_activity_item_del(25)
    # kb._mobile_resource_activity_item_supplier_list()
    # kb._mobile_resource_activity_item_ms_list()
    # kb._common_upload_activity()
    # kb. _mobile_plant_list('海棠', 1, 20)
    # kb. _mobile_plant_detail(1816)
    # kb._admin_plant_disease_name_list('枯萎', 1, 20)
    # kb._admin_plant_disease_list_hot()
    # kb._admin_plant_disease_detail(45)
    # kb._admin_config_list(1, 20)
    # kb._admin_config_detail(1)
    # kb._admin_config_list_config_by_code('PHONE_CODE')
    # kb._admin_config_edit(2, 'CONFIG_UPDATE_USER', 'SERVICE', '02800000', '杨露瑶测试', '1')
    # kb._admin_config_add('PHONE', 'SERVICE', '02800000', '测试电话', '0', '1')
    # kb._admin_upload_log_last(2)
    kb._admin_plant_disease_import()
    # kb._admin_plant_import()
