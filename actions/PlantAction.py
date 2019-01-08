# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
from backend.User import User
from backend.Employee import Employee


class plantAction(object):
    def __init__(self):
        self.log = Log('plant').logger
        self.request = Request()
        self.tool = Tool()
        # self.plant = object

    def set_user(self, user, passwd="8888", employee=False):
        if employee is False:
            self.plant = User(user)
            return self.plant
        else:
            self.plant = Employee(user, passwd)
            return self.plant

    def admin_plant_case_create(self, caseTopic, symptom, treatmentMethod, creatorId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'caseTopic': caseTopic, 'symptom': symptom, 'treatmentMethod': treatmentMethod, 'creatorId': creatorId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/admin/plant-case/create', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_plantCase_detail(self, plantCaseId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantCaseId': plantCaseId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/admin/plantCase/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_plantCase_list(self, caseNo, caseKeyword, doctorUserId, mobile, pageSize, pageNum, id, createTime, editTime, isDelete, orderFieldType, startIndex, orderField, queryData):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'caseNo': caseNo, 'caseKeyword': caseKeyword, 'doctorUserId': doctorUserId, 'mobile': mobile, 'pageSize': pageSize, 'pageNum': pageNum, 'id': id, 'createTime': createTime, 'editTime': editTime, 'isDelete': isDelete, 'orderFieldType': orderFieldType, 'startIndex': startIndex, 'orderField': orderField, 'queryData': queryData}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/admin/plantCase/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def callback_plant_watering(self, expireDate):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'expireDate': expireDate}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/callback/plant/watering', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_home_msTalk(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/home/msTalk', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_member_nick_edit(self, nickUserId, nick):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'nickUserId': nickUserId, 'nick': nick}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/member-nick/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_member_accept(self, invitorId, acceptorMobile, verifyCode):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'invitorId': invitorId, 'acceptorMobile': acceptorMobile, 'verifyCode': verifyCode}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/member/accept', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_member_invite(self, acceptorMobile, acceptorNick):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'acceptorMobile': acceptorMobile, 'acceptorNick': acceptorNick}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/member/invite', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_member_isInviteBefore(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/member/isInviteBefore', data=data)
        json_response = json.loads(response)
        self.log.debug("开始是否邀请过家人,接口返回:%s" % json_response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_member_member_info_list(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/member/member-info-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_member_member_info_order_list(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/member/member-info-order-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_member_member_weather(self, adCode):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'adCode': adCode}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/member/member-weather', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_message_board_add(self, content, messageBoardImgs, adCode, createTime):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'content': content, 'messageBoardImgs': messageBoardImgs, 'adCode': adCode, 'createTime': createTime}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/message-board/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_message_board_listPage(self, pageSize, pageNum):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'pageSize': pageSize, 'pageNum': pageNum}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/message-board/listPage', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_message_board_listPage4Invite(self, pageSize, pageNum):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'pageSize': pageSize, 'pageNum': pageNum}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/message-board/listPage4Invite', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_mobile_record_add(self, mobileJson):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'mobileJson': mobileJson}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/mobile-record/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_mobile_record_exist(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/mobile-record/exist', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_add(self, roomId, plantWikiId, plantName, waterCycleTime, adCode, imgUrl):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'roomId': roomId, 'plantWikiId': plantWikiId, 'plantName': plantName, 'waterCycleTime': waterCycleTime, 'adCode': adCode, 'imgUrl': imgUrl}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            raise Exception("status返回ERROR")
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_album_add(self, plantId, imgUrl, adCode):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantId': plantId, 'imgUrl': imgUrl, 'adCode': adCode}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/album-add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_album_list(self, plantId, pageSize, pageNum):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantId': plantId, 'pageSize': pageSize, 'pageNum': pageNum}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/album-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_album_upload(self, file):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'file': file}
        response = self.request.post_file(url='http://dev.ms.plant.sjnc.com/mobile/plant/album-upload',
                                          file_key="file", data_dict=data, file_path="./picture/%s" % file)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def mobile_plant_delete(self, plantId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantId': plantId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/delete', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_list_by_room(self, roomId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'roomId': roomId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/list-by-room', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def mobile_plant_list_for_invite(self, userId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'userId': userId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/list-for-invite', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_manage_fertilize(self, plantIds, adCode):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantIds': plantIds, 'adCode': adCode}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/manage-fertilize', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_manage_pick(self, plantIds, adCode):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantIds': plantIds, 'adCode': adCode}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/manage-pick', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_manage_record_list(self, plantId, pageSize, pageNum):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantId': plantId, 'pageSize': pageSize, 'pageNum': pageNum}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/manage-record-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_manage_trim(self, plantIds, adCode):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantIds': plantIds, 'adCode': adCode}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/manage-trim', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_manage_watering(self, plantIds, adCode):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantIds': plantIds, 'adCode': adCode}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/manage-watering', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_record_added(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/record-added', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_transport(self, plantId, toRoomId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantId': plantId, 'toRoomId': toRoomId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plant/transport', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plantCase_detail(self, plantCaseId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantCaseId': plantCaseId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/plantCase/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_room_add(self, roomType, roomUserId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'roomType': roomType, 'roomUserId': roomUserId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/room/add', data=data)
        json_response = json.loads(response)
        self.log.debug("添加房间，响应结果:%s" % json_response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_room_change_list(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/room/change-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def mobile_room_del(self, roomId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'roomId': roomId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/room/del', data=data)
        json_response = json.loads(response)
        self.log.debug("删除房间，响应结果:%s" % json_response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_room_group_list(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/room/group-list', data=data)
        json_response = json.loads(response)
        self.log.debug("房间当前排序，响应结果:%s" % json_response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def mobile_room_homepage_list(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/room/homepage-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def mobile_room_show_status(self, roomId, showStatus):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'roomId': roomId, 'showStatus': showStatus}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/room/show-status', data=data)
        json_response = json.loads(response)
        self.log.debug("隐藏显示房间，响应结果:%s" % json_response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_room_type_order(self, roomTypeOrderJson):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'roomTypeOrderJson': roomTypeOrderJson}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/room/type-order', data=data)
        json_response = json.loads(response)
        self.log.debug("排序房间房间，响应结果:%s" % json_response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_visit_record_add(self, adCode):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'adCode': adCode}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/visit-record/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_visit_record_list(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/visit-record/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_visit_record_list4Invite(self, userId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'userId': userId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/visit-record/list4Invite', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_plant_list(self, search):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'search': search}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/mobile/plant/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
        return json_response

    def mobile_plant_detail(self, id):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'id': id}
        response = self.request.post(url='http://dev.ms.kbms.sjnc.com/mobile/plant/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_plant_case_list(self, caseNo, caseKeyword, doctorUserId, mobile, pageSize, pageNum, id, createTime, editTime, isDelete, orderFieldType, startIndex, orderField, queryData):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'caseNo': caseNo, 'caseKeyword': caseKeyword, 'doctorUserId': doctorUserId, 'mobile': mobile, 'pageSize': pageSize, 'pageNum': pageNum, 'id': id, 'createTime': createTime, 'editTime': editTime, 'isDelete': isDelete, 'orderFieldType': orderFieldType, 'startIndex': startIndex, 'orderField': orderField, 'queryData': queryData}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/admin/plant-case/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_plant_case_detail(self, plantCaseId):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'plantCaseId': plantCaseId}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/admin/plant-case/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_wx_getAccessToken(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/wx/getAccessToken', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_wx_refreshAccessToken(self):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/wx/refreshAccessToken', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_wx_signature(self, url):
        data = {'_tk_': self.plant.token, '_deviceId_': self.plant.device_id, 'url': url}
        response = self.request.post(url='http://dev.ms.plant.sjnc.com/mobile/wx/signature', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

