#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
__author__ = "yaxin.guan|yong.guo"
__date__ = "20181216"
"""
from actions.PlantAction import plantAction
import unittest
from utils.Log import Log
from utils.Util import DataBaseOperate
import time
from faker import Faker
import random
import xlrd
from os import path
import json


class PlantMain(unittest.TestCase):
    """
    接口地址：http://dev.ms.plant.sjnc.com/swagger-ui.html
    """
    plantTest = plantAction()
    faker_zh = Faker(locale='zh_CN')
    log = Log('PlantMain').logger
    log.info("开始执行家庭类、植物类接口测试")
    invite_mobile = faker_zh.phone_number()
    uuid = faker_zh.random_number(32)

    def test0001(self):
        """
        添加植物.正向流程-关雅馨
        接口路径:POST /mobile/plant/add
        :return:
        """
        self.log.info("开始执行添加植物正向测试，接口路径/mobile/plant/add")
        self.plantTest.set_user("15283855883")
        plant_add = self.plantTest.mobile_plant_add(260, 1727, "虎刺梅2", 1, None,
                                        "http://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data/ms-kbms"
                                        "/plant/img/1544672001176.jpg")

    def test0003(self):
        """
        移动植物.正向流程-关雅馨
        接口路径:POST /mobile/plant/transport
        :return:
        """
        self.log.info("开始执行移动植物正向测试，接口路径/mobile/plant/transport")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_transport(35, 261)

    def test0002(self):
        """
        删除植物.正向流程-关雅馨
        接口路径:POST /mobile/plant/delete
        :return:
        """
        self.log.info("开始执行移动植物正向测试，接口路径/mobile/plant/delete")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_delete(35)

    def test0004(self):
        """
        植物浇水.正向流程-关雅馨
        接口路径:POST /mobile/plant/manage-watering
        :return:
        """
        self.log.info("开始执行植物浇水正向测试，接口路径/mobile/plant/manage-watering")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_manage_watering({42, 40, 41}, None)

    def test0005(self):
        """
        植物施肥.正向流程-关雅馨
        接口路径:POST /mobile/plant/manage-fertilize
        :return:
        """
        self.log.info("开始执行植物施肥正向测试，接口路径/mobile/plant/manage-fertilize")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_manage_fertilize({42, 40, 41}, None)

    def test0006(self):
        """
        植物采摘.正向流程-关雅馨
        接口路径:POST /mobile/plant/manage-pick
        :return:
        """
        self.log.info("开始执行植物采摘正向测试，接口路径/mobile/plant/manage-pick")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_manage_pick({42, 40, 41}, None)

    def test0007(self):
        """
        植物修剪.正向流程-关雅馨
        接口路径:POST /mobile/plant/manage-trim
        :return:
        """
        self.log.info("开始执行植物修剪正向测试，接口路径/mobile/plant/manage-trim")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_manage_trim({42, 40, 41}, None)

    def test0008(self):
        """
        获取植物排列.正向流程-关雅馨
        接口路径:POST /mobile/plant/list-by-room
        :return:
        """
        self.log.info("开始执行获取植物排列正向测试，接口路径/mobile/plant/list-by-room")
        self.plantTest.set_user("15282644233")
        self.plantTest.mobile_plant_list_by_room(486)

    def test0009(self):
        """
       定时调度-浇水到期提醒-关雅馨
        接口路径:POST /callback/plant/watering
        :return:
        """
        self.log.info("开始执行定时调度-浇水到期提醒测试，接口路径/callback/plant/watering")
        self.plantTest.set_user("13592478554")
        self.plantTest.callback_plant_watering("2018-12-20")

    def test0010(self):
        """
        上传植物图片-关雅馨
        接口路径:POST /mobile/plant/album-upload
        :return:
        """
        self.log.info("开始执行上传植物图片测试，接口路径/mobile/plant/album-upload")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_album_upload("1.jpeg")

    def test0011(self):
        """
        上传植物相册-关雅馨
        接口路径:POST /mobile/plant/album-add
        :return:
        """
        self.log.info("开始执行上传植物相册测试，接口路径/mobile/plant/album-add")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_album_add(41, "https://dnkj-family-farm-1.oss-cn-huhehaote.aliyuncs.com/data"
                                                  "/ms-plant/plant/album/1545015438389.jpeg", 510100)

    def test0012(self):
        """
        相册列表-关雅馨
        接口路径:POST /mobile/plant/album-list
        :return:
        """
        self.log.info("开始执行获取相册测试，接口路径/mobile/plant/album-list")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_album_list(41, None, None)

    def test0013(self):
        """
        植物管理-养护记录
        接口路径:POST mobile/plant/man≠age-record-list
        :return:
        """
        self.log.info("开始执行获取植物养护记录，接口路径/mobile/plant/manage-record-list")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_manage_record_list(41, None, None)
    def test0014(self):
        """
       植物管理入口-植物添加记录-关雅馨
       接口路径:POST mobile/plant/record-added
        :return:
        """
        self.log.info("开始执行植物添加记录测试，接口路径mobile/plant/record-added")
        self.plantTest.set_user("15282644233")
        self.plantTest.mobile_plant_record_added()

    def test0015(self):
        """
        植物转移房间列表-关雅馨
        接口路径:POST /mobile/room/change-list
        :return:
        """
        self.log.info("开始执行植物转移房间列表测试，接口路径/mobile/room/change-list")
        self.plantTest.set_user("15282644233")
        self.plantTest.mobile_room_change_list()

    def test0016(self):
        """
        添加植物-关键词模糊查询植物列表-关雅馨
        接口路径:POST /mobile/plant/list
        :return:
        """
        self.log.info("添加植物-关键词模糊查询植物列表测试")
        self.plantTest.set_user("13592478554")
        self.plantTest.mobile_plant_list("虎3")

    def test0017(self):
        """
        植物详情-关雅馨
        接口路径: POST /mobile/plant/detail
        :return:
        """
        self.log.info("获取植物详情")
        self.plantTest.set_user("15282644233")
        self.plantTest.mobile_plant_detail("1818")

    def test0018(self):
        """
        首页-苗叔说话内容-关雅馨
        接口路径: POST /mobile/home/msTalk
        :return:
        """
        self.log.info("首页-苗叔说话内容")
        self.plantTest.set_user("15283855883")
        self.plantTest.mobile_home_msTalk()

    def test0030(self):
        """
        这是一项大工程
        植物管理主流程:登录-进入植物管理主页-获取植物排列-添加植物-获取植物列表-浇水-施肥-修剪-采摘-删除植物-转移房间--关雅馨
        :return:
        """
        # 随机获取adcode
        adcode = [510000, 510100, 510101, 510104, 510105, 510106, 510107, 510108, 510112, 510113, 510114, 510115,
                  510116, 510117, 510121, 510129, 510131, 510132, 510181, 510182, 510183, 510184, 510185, 510300,
                  510301, 510302, 510303, 510304, 510311, 510321, 510322, 510400, 510401, 510402, 510403, 510411,
                  510421, 510422, 510500, 510501, 510502, 510503, 510504, 510521, 510522, 510524, 510525, 510600,
                  510601, 510603, 510623, 510626, 510681, 510682, 510683, 510700, 510701, 510703, 510704, 510705,
                  510722, 510723, 510725, 510726, 510727, 510781, 510800, 510801, 510802, 510811, 510812, 510821,
                  510822, 510823, 510824, 510900, 510901, 510903, 510904, 510921, 510922, 510923, 511000, 511001,
                  511002, 511011, 511024, 511025, 511083, 511100, 511101, 511102, 511111, 511112, 511113, 511123,
                  511124, 511126, 511129, 511132, 511133, 511181, 511300, 511301, 511302, 511303, 511304, 511321,
                  511322, 511323, 511324, 511325, 511381, 511400, 511401, 511402, 511403, 511421, 511423, 511424,
                  511425, 511500, 511501, 511502, 511503, 511521, 511523, 511524, 511525, 511526, 511527, 511528,
                  511529, 511600, 511601, 511602, 511603, 511621, 511622, 511623, 511681, 511700, 511701, 511702,
                  511703, 511722, 511723, 511724, 511725, 511781, 511800, 511801, 511802, 511803, 511822, 511823,
                  511824, 511825, 511826, 511827, 511900, 511901, 511902, 511903, 511921, 511922, 511923, 512000,
                  512001, 512002, 512021, 512022, 513200, 513201, 513221, 513222, 513223, 513224, 513225, 513226,
                  513230, 513231, 513232, 513233, 513300, 513301, 513322, 513323, 513324, 513325, 513326, 513327,
                  513329, 513330, 513331, 513332, 513333, 513334, 513335, 513336, 513337, 513338, 513400, 513401,
                  513423, 513424, 513425, 513426, 513427, 513428, 513429, 513430, 513431, 513432, 513433, 513434,
                  513227, 513228, 513328, 513422, 513435, 513436, 513437]
        adcode_random = random.choice(adcode)
        # 随机获取植物需要浇水的天数
        water_day_random = random.randint(1, 30)
        # 随机获取植物姓名
        plant_name = ["腊梅", "月", "虎刺", "草莓"]
        plant_name_random = random.choice(plant_name)
        # 随机获取植物图片
        plant_pic = ["1.jpg", "1.png", "3.jpeg", "4.jpg", "2.jpeg"]
        plant_pic_random = random.choice(plant_pic)
        self.log.info("登录")
        self.plantTest.set_user("13572720546")
        self.log.info("新增到访记录")
        self.plantTest.mobile_visit_record_add(None)
        self.log.info("苗叔说话内容")
        self.plantTest.mobile_home_msTalk()
        self.log.info("随机获取房间ID")
        room_lists = self.plantTest.mobile_room_homepage_list()
        room_list = room_lists.get("content")
        room_id = []
        for i in range(len(room_list)):
            print(i)
            if "roomId" in room_list[i]:
                room_id.append(room_list[i].get("roomId"))
        room_id_random = random.choice(room_id)
        self.log.info("添加植物前获取房间植物列表")
        self.plantTest.mobile_plant_list_by_room(room_id_random)
        self.log.info("选择图片")
        img_url = self.plantTest.mobile_plant_album_upload(plant_pic_random)
        self.log.info("选择植物名称")
        plant = self.plantTest.mobile_plant_list(plant_name_random)
        self.log.info("确认添加植物")
        self.plantTest.mobile_plant_add(room_id_random, plant["content"]["datas"][0]["id"],
                                        plant["content"]["datas"][0]["name"], str(water_day_random),
                                        adcode_random, img_url["content"])
        time.sleep(5)
        self.log.info("添加植物后获取房间植物列表")
        plant_lists = self.plantTest.mobile_plant_list_by_room(room_id_random)
        # 新增植物后当前用户家庭中的随机房间的所有植物
        plant_list = plant_lists.get("content")
        # plant_wiki_id = []
        # for i in range(len(plant_list)):
        #     print(i)
        #     plant_wiki_id.append(plant_list[i].get("plantWikiId"))
        # plant_wiki_id_random = random.choice(plant_wiki_id)
        plant_id = []
        for i in range(len(plant_list)):
            print(i)
            plant_id.append(plant_list[i].get("id"))
        plant_id_random = random.choice(plant_id)
        self.log.info("随机房间的随机植物浇水")
        self.plantTest.mobile_plant_manage_watering(plant_id_random, adcode_random)
        self.log.info("随机房间的随机植物施肥")
        self.plantTest.mobile_plant_manage_fertilize(plant_id_random, adcode_random)
        self.log.info("随机房间的随机植物采摘")
        self.plantTest.mobile_plant_manage_pick(plant_id_random, adcode_random)
        self.log.info("随机房间的随机植物修剪")
        self.plantTest.mobile_plant_manage_trim(plant_id_random, adcode_random)
        self.log.info("随机房间的随机植物养护记录")
        self.plantTest.mobile_plant_manage_record_list(plant_id_random, None, None)
        self.log.info("随机房间的随机植物相册")
        self.plantTest.mobile_plant_album_list(plant_id_random, None, None)
        self.log.info("转移植物所在房间")
        self.log.info("获取植物转移房间列表")
        room_change_lists = self.plantTest.mobile_room_change_list()
        room_change_list = room_change_lists.get("content")
        room_change_id = []
        for i in range(len(room_change_list)):
            if "roomId" in room_change_list[i]:
                room_change_id.append(room_change_list[i].get("roomId"))
        room_change_id_random = random.choice(room_change_id)
        self.plantTest.mobile_plant_transport(random.choice(plant_id), room_change_id_random)
        self.log.info("删除植物")
        # 冗余注释
        self.plantTest.mobile_plant_delete(random.choice(plant_id))

    def test0031(self, login_user_mobile="13592478554"):
        """
        添加房间.正向流程-郭勇
        接口路径：POST /mobile/room/add
        :return:
        """

        db_get_user_id = self.plantTest.set_user(login_user_mobile).user_id
        # 通过当前登录用户获取，当前用户家庭中的其他用户
        db_get_user_home_users = DataBaseOperate().operate("39.104.28.40", "ms-plant",
                                                           "SELECT user_id FROM t_member WHERE home_id = ("
                                                           "SELECT home_id FROM t_member WHERE user_id = %s)"
                                                           % db_get_user_id)
        get_users = []
        for x in db_get_user_home_users:
            get_users.append(x['user_id'])

        # 随机房间类型 房间类型(10阳台,11客厅,12卧室,13花园,14屋顶,15书房,16厨房,17厕所)
        room_type = random.randint(10, 17)
        # 随机获取房间中的主人
        room_owner = random.choice(get_users)

        self.log.info("开始执行添加房间正向测试，接口路径/mobile/room/add")
        self.log.debug("给用户%d添加%d类型房间" % (room_owner, room_type))
        self.plantTest.mobile_room_add(room_type, room_owner)

    def test0032(self, login_user_mobile="13592478554"):
        """
        隐藏房间.正向流程-郭勇
        接口路径：POST /mobile/room/show-status
        :return:
        """
        db_get_user_id = self.plantTest.set_user(login_user_mobile).user_id
        # 通过当前登录用户获取，当前用户家庭中的所有房间
        db_get_user_homes = DataBaseOperate().operate("39.104.28.40", "ms-plant",
                                                      "SELECT id FROM t_room WHERE home_id = ("
                                                      "SELECT home_id FROM t_member WHERE user_id = %s )"
                                                      " AND is_delete = 0" % db_get_user_id)

        room_ids = []
        for x in db_get_user_homes:
            room_ids.append(x['id'])

        room_id = random.choice(room_ids)
        room_status = random.randint(0, 1)
        self.log.info("开始执行隐藏房间正向测试，接口路径/mobile/room/show-status")
        self.log.debug("将房间%d隐藏状态设置为%d" % (room_id, room_status))
        self.plantTest.mobile_room_show_status(room_id, room_status)

    def test0033(self, login_user_mobile="13592478554"):
        """
        排序房间.正向流程-郭勇
        接口路径：POST /mobile/room/type-order
        :return:
        """
        self.log.info("开始执行排序房间正向测试，接口路径/mobile/room/type-order")
        self.plantTest.set_user("18382373185")
        self.log.info("获取当前用户排序列表：%s" % self.plantTest.mobile_room_group_list())
        # group_lists = self.plantTest.mobile_room_group_list()
        # group_list = group_lists.get("content")
        # room_output_list = {}
        # room_id = []
        # for i in range(len(group_list)):
        #     room_output_lists = group_list[i]
        #     room_output_list = room_output_lists.get("roomOutputList")
        #     room = room_output_list[0]
        #     for j in range(len(room_output_list)):
        #         if room_output_list[j].get("plantNum") == 0:
        #             room_id.append(room_output_list[j].get("id"))
        # room_id_random = random.choice(room_id)
        # 对房间类型进行随机排序
        self.log.info("重新对房间进行排序中....")
        room_sort = []
        for room_number in range(random.randint(1, 8)):
            room_sort.append({"roomType": random.randint(10, 17), "roomTypeOrder": room_number+1})
        self.log.info("准备对房间进行排序顺序为：%s" % room_sort)
        self.plantTest.mobile_room_type_order(str(room_sort))
        self.log.info("获取当前用户排序列表：%s" % self.plantTest.mobile_room_group_list())

    def test0034(self, login_user_mobile="13592478554"):
        """
        单接口测试
        删除房间.正向流程-郭勇
        接口路径：POST /mobile/room/del
        :return:
        """
        db_get_user_id = self.plantTest.set_user(login_user_mobile).user_id
        # # 通过当前登录用户获取，当前用户家庭中的所有房间
        # db_get_user_homes = DataBaseOperate().operate("39.104.28.40", "ms-plant",
        #                                               "SELECT id FROM t_room WHERE home_id = ("
        #                                               "SELECT home_id FROM t_member WHERE user_id = %s "
        #                                               ") AND is_delete = 0" % db_get_user_id)
        # room_ids = []
        # for x in db_get_user_homes:
        #     room_ids.append(x['id'])
        # room_id = random.choice(room_ids)

        self.log.info("开始执行删除房间")
        self.plantTest.set_user("15282644233")
        group_lists = self.plantTest.mobile_room_group_list()
        group_list = group_lists.get("content")
        room_output_list = {}
        room_id = []
        for i in range(len(group_list)):
            room_output_lists = group_list[i]
            room_output_list = room_output_lists.get("roomOutputList")
            room = room_output_list[0]
            for j in range(len(room_output_list)):
                if room_output_list[j].get("plantNum") == 0:
                    room_id.append(room_output_list[j].get("id"))
        room_id_random = random.choice(room_id)
        self.plantTest.mobile_room_del(room_id_random)

    def test0035(self, login_user_mobile="13592478554"):
        """
        单接口测试
        邀请家人.正向流程-郭勇
        接口路径：POST /mobile/member/invite
        :return:
        """

        self.log.info("开始执行邀请家人正向测试，接口路径/mobile/member/invite")
        self.plantTest.set_user(login_user_mobile)
        invite_user_name = self.faker_zh.name_female()
        self.log.info("邀请的电话号码是%s,被邀请对人是：%s" % (self.invite_mobile, invite_user_name))
        self.plantTest.mobile_member_invite(str(self.invite_mobile), str(invite_user_name))

    def test0036(self, login_user_mobile="13592478554"):
        """
        单接口测试
        接受邀请.正向流程-郭勇
        接口路径：POST /mobile/member/accept
        :return:
        """
        db_get_user_id = self.plantTest.set_user(login_user_mobile).user_id
        self.log.info("开始执行家人接受邀请正向测试，接口路径/mobile/member/accept")
        self.log.info("%s接受邀请..." % self.invite_mobile)
        self.plantTest.mobile_member_accept(db_get_user_id, self.invite_mobile, "8888")

    def test0037(self, login_user_mobile="13592478554"):
        """
        单接口测试
        家人备注.正向流程-郭勇
        接口路径：POST /mobile/member-nick/edit
        :return:
        """
        db_get_user_id = self.plantTest.set_user(login_user_mobile).user_id
        self.log.info("开始执行家人备注正向测试，接口路径/mobile/member-nick/edit")
        # 获取当前家庭中所有成员
        db_get_user_home_users = DataBaseOperate().operate("39.104.28.40", "ms-plant",
                                                           "SELECT user_id FROM t_member WHERE home_id = ("
                                                           "SELECT home_id FROM t_member WHERE user_id = %s) "
                                                           "AND user_id != %s" % (db_get_user_id,db_get_user_id))
        get_users = []
        for x in db_get_user_home_users:
            get_users.append(x['user_id'])

        # 随机获给一个家庭成员进行备注
        nick_user = random.choice(get_users)
        nick_name = self.faker_zh.name_female()
        self.plantTest.mobile_member_nick_edit(nick_user, nick_name)

    def test0038(self, login_user_mobile="13592478554"):
        """
        单接口测试
        家人留言.正向流程-郭勇
        接口路径：POST /mobile/message-board/add
        :return:
        """
        message_text = ["心相依，永不悔，有一种相遇叫最美，春花香，蝴蝶飞，有一种思念叫沉醉，夜无眠，饭无味，有一种付出叫珍贵，雨无阻，任风吹，人间真情最为美。写心灵鸡汤美的句子","精神上的道德力量发挥了它的潜能，举起了它的旗帜，于是我们的爱国热情和正义感在现实中均得施展其威力和作用。","如果你对这一片杂草置之不理，则会“野火烧不尽，春风吹又生”。杂草的生命力顽强，稍不留意就会使我们心灵的田野变的一片荒芜。","如果我是亿万富翁，我就要把全世界的玫瑰都买下来送给你。我是富翁吗?不是，所以我只能将心奉上。","如果漂亮的脸蛋是份推荐书的话，那么圣洁的心就是份信用卡。","昙花一现的感情，不能真诚地可靠地长期地相爱，是相当一部分青年人道德方面存在的严重缺陷。","我们教育工作者的任务就在于让每个儿童看到人的心灵美，珍惜爱护这种美，并用自己的行动使这种美达到应有的高度。","道德教育成功的“秘诀”在于，当一个人还在少年时代的时候，就应该在宏伟的社会生活背景上给他展示整个世界个人生活的前景。","只有当自己处于一个最好的姿态，才会有一个最好的人来爱你。你若是想遇到安静温暖的男人，过简单美好的生活，首先，你自己得成为淡定与美丽的女人。","在人生的路途上，我们渐渐地知道，最好的爱情，不是大起大落大喜大悲，而是一杯温水，不随外界变幻而更改，不因岁月迁徙而转移，给你的是永恒的温暖。","审美的感官需要文化修养，借助修养才能了解美，发现美。","道德准则，只有当它们被学生自己去追求获得和亲自体验过的时候，只有当它们变成学生独立的个人信念的时候，才能真正成为学生的精神财富。","平庸将你的心灵烘干到没有一丝水分，然后荣光才会拨动你心灵最深处的弦。","见过磕长头的人吗?他们的脸和手都很脏，可是心灵却很干净。","感动是一种无形的东西，用肉眼望不见，只有用心灵才感受得到。","学会放下，放下，是一种生活的智慧;放下，是一门心灵的学问。人生在世，有些事情是不必在乎的，有些东西是必须清空的。该放下时就放下，你才能够腾出手来，抓住真正属于你的快乐和幸福。","感情有着极大的鼓舞力量，因此，它是一切道德行为的重要前提，谁要是没有强烈的志向，也就不能够热烈地把这个志向体现于事业中。","心灵美比外表美美丽，外表美只不过是外表，心灵美虽然看不见，但可以感受。","即使以为自己的感情已经干涸得无法给予，也总会有一个时刻一样东西能拨动心灵深处的弦;我们毕竟不是生来就享受孤独的。","以天生的感情喜爱纯粹艺术和科学，所感受到的神秘，是我们能够拥有的最美的经验。","集体的习惯，其力量更大于个人的习惯。因此如果有一个有良好道德风气的社会环境，是最有利于培训好的社会公民的。","在任何大自然中都无法认得美的人，这正表示其人心中有缺陷。","人生，总会有不期而遇的温暖，和生生不息的希望。不管前方的路有多苦，只要走的方向正确，不管多么崎岖不平，都比站在原地更接近幸福。","世上最好最美的事物是看不见的，摸不到的。只有心性感情和勇气可以察觉。","良好的心是花园，良好的思想是根茎，良好的说话是花朵，良好的事业就是果子。","有了太阳地球才回转，有了地球月亮才回转，有了月亮星光才如此灿烂，有了你我的世界才如此丰富浪漫。","貌虽美但如果没有纯洁的灵魂，就好比是晶亮的玻璃眼睛，不辨世事。","唯有美德，能使人胸怀开阔，情操优美，内心平衡，灵魂愉悦。","从我们心中夺走对美的爱，也就夺走了。","心灵是一方广袤的天空，它包容着世间的一切;心灵是一片宁静的湖水，偶尔也会泛起阵阵涟漪;心灵是一块皑皑的雪原，它辉映出一个缤纷的世界。","要想除掉旷野里的杂草，不是用手拔，不是用锄锄，也不是用火烧，方法只有一种，那就是让庄稼占据这片旷野。","劳动的崇高道德意义还在于，一个人能在劳动的物质成果中体现他的智慧技艺对事业的无私热爱和把自己的经验传授给同志的志愿。","黑夜里，婴儿的啼哭声和邻居的狗叫声，让人抚慰心灵。","一生的生活是否幸福平安吉祥，则要看他的处世为人是否道德无亏，能否作社会的表率。因此，修身的教育，也成为他的学校工作的主要部分。","要是一个人的全部人格全部生活都奉献给一种道德追求，要是他拥有这样的力量，一切其他的人在这方面和这个人相比起来都显得渺小的时候，那我们在这个人的身上就看到崇高的善。","美是奇异的，它是艺术家从世界的喧嚣和他自身灵魂的磨难中铸造出来的东西。","迷人，则是因为他活得很好。总在做自己喜欢的想做的事情，活得好的人像阳光，总会不自觉地散发着自信的温暖。","受苦图报的念头，对于天生高尚的心灵是一种伤害。美德并不是高尚心灵的一件装饰品：不是的，而是心灵美的一种表现形式。","心灵世界上的那些美好的坦诚的善良的苗，心中的真善美在时时呵护着苗地茁壮成长，有一天会结出来绚丽的果实。而那些丑恶的贪婪的苗我们就不得不把它称之为草。"]
        self.log.info("开始执行家人留言正向测试，接口路径/mobile/message-board/add")
        self.plantTest.set_user(login_user_mobile)
        # 生成留言信息
        message_info = random.choice(message_text)
        message_address = self.faker_zh.address()
        message_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # 生成留言图片信息
        message_picture_tmp = []
        for x in range(random.randint(1, 9)):
            message_picture_tmp.append(self.faker_zh.uri())
        message_picture = ",".join(message_picture_tmp)

        self.log.info("留言内容为：%s, \n上传图片地址是 %s, \n留言地址：%s, \n留言时间： %s" % (message_info, message_picture,
                                                                         message_address, message_time))
        self.plantTest.mobile_message_board_add(message_info, message_picture, message_address, message_time)

    def test0039(self, login_user_mobile="13592478554"):
        """
        单接口测试
        是否邀请过家人.正向流程-郭勇
        接口路径：POST /mobile/member/isInviteBefore
        :return:
        """
        self.log.info("开始是否邀请过家人测试，接口路径/mobile/member/isInviteBefore")
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_member_isInviteBefore()

    def test0040(self, login_user_mobile="13592478554"):
        """
        单接口测试
        留言列表-郭勇
        接口路径：POST /mobile/message-board/listPage
        :return:
        """
        self.log.info("开始留言列表测试，接口路径/mobile/message-board/listPage")
        self.plantTest.set_user(login_user_mobile)
        pn = random.randint(1, 5)
        ps = random.randint(1, 3)
        self.log.info("查看第%d页留言信息(每页%d条数据)" % (pn, ps))
        self.plantTest.mobile_message_board_listPage(ps, pn)

    def test0041(self, login_user_mobile="13592478554"):
        """
        单接口测试
        留言列表-邀请.正向流程-郭勇
        接口路径：POST /mobile/message-board/listPage4Invite
        :return:
        """
        self.log.info("开始留言列表测试，接口路径/mobile/message-board/listPage4Invite")
        self.plantTest.set_user(login_user_mobile)
        pn = random.randint(1, 5)
        ps = random.randint(1, 3)
        self.log.info("H5查看第%d页留言信息(每页%d条数据)" % (pn, ps))
        self.plantTest.mobile_message_board_listPage4Invite(ps, pn)

    def test0042(self, login_user_mobile="13592478554"):
        """
        单接口测试
        新增到访记录.正向流程-郭勇
        接口路径：POST /mobile/visit-record/add
        :return:
        """
        adcode = [510000, 510100, 510101, 510104, 510105, 510106, 510107, 510108, 510112, 510113, 510114, 510115, 510116, 510117, 510121, 510129, 510131, 510132, 510181, 510182, 510183, 510184, 510185, 510300, 510301, 510302, 510303, 510304, 510311, 510321, 510322, 510400, 510401, 510402, 510403, 510411, 510421, 510422, 510500, 510501, 510502, 510503, 510504, 510521, 510522, 510524, 510525, 510600, 510601, 510603, 510623, 510626, 510681, 510682, 510683, 510700, 510701, 510703, 510704, 510705, 510722, 510723, 510725, 510726, 510727, 510781, 510800, 510801, 510802, 510811, 510812, 510821, 510822, 510823, 510824, 510900, 510901, 510903, 510904, 510921, 510922, 510923, 511000, 511001, 511002, 511011, 511024, 511025, 511083, 511100, 511101, 511102, 511111, 511112, 511113, 511123, 511124, 511126, 511129, 511132, 511133, 511181, 511300, 511301, 511302, 511303, 511304, 511321, 511322, 511323, 511324, 511325, 511381, 511400, 511401, 511402, 511403, 511421, 511423, 511424, 511425, 511500, 511501, 511502, 511503, 511521, 511523, 511524, 511525, 511526, 511527, 511528, 511529, 511600, 511601, 511602, 511603, 511621, 511622, 511623, 511681, 511700, 511701, 511702, 511703, 511722, 511723, 511724, 511725, 511781, 511800, 511801, 511802, 511803, 511822, 511823, 511824, 511825, 511826, 511827, 511900, 511901, 511902, 511903, 511921, 511922, 511923, 512000, 512001, 512002, 512021, 512022, 513200, 513201, 513221, 513222, 513223, 513224, 513225, 513226, 513227, 513228, 513230, 513231, 513232, 513233, 513300, 513301, 513322, 513323, 513324, 513325, 513326, 513327, 513328, 513329, 513330, 513331, 513332, 513333, 513334, 513335, 513336, 513337, 513338, 513400, 513401, 513422, 513423, 513424, 513425, 513426, 513427, 513428, 513429, 513430, 513431, 513432, 513433, 513434, 513435, 513436, 513437]
        adcode_random = random.choice(adcode)
        self.log.info("开始执行新增到访记录测试，接口路径/mobile/visit-record/add")
        self.plantTest.set_user(login_user_mobile)
        self.log.info("在adCode为%d地点，添加一个%s的到访记录" % (adcode_random, login_user_mobile))
        self.plantTest.mobile_visit_record_add(str(adcode_random))

    def test0043(self, login_user_mobile="13592478554"):
        """
        单接口测试
        到访记录.正向流程-郭勇
        接口路径：POST /mobile/visit-record/list
        :return:
        """
        self.log.info("开始执行到访记录正向测试，接口路径/mobile/visit-record/list")
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_visit_record_list()

    def test0044(self, login_user_mobile="13592478554"):
        """
        单接口测试
        到访记录-邀请.正向流程-郭勇
        接口路径：POST /mobile/visit-record/list4Invite
        :return:
        """
        self.log.info("开始执行到访记录-邀请测试，接口路径/mobile/visit-record/list4Invite")
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_visit_record_list4Invite("")

    def test0045(self, login_user_mobile="13592478554"):
        """
        单接口测试
        添加通讯录.正向流程-郭勇
        接口路径：POST /mobile/mobile-record/add
        :return:
        """
        # 生成用户电话记录信息
        mobile_record = []
        for x in range(random.randint(50, 300)):
            mobile_record.append({"mobile": self.faker_zh.phone_number(), "remark": self.faker_zh.name_female()})

        self.log.info("开始执行添加电话记录正向测试，接口路径/mobile/mobile-record/add")
        self.plantTest.set_user(login_user_mobile)
        self.log.debug("共上传%d个用户,上传的通讯录内容是:%s" % (len(mobile_record), mobile_record))
        self.plantTest.mobile_mobile_record_add(str(mobile_record))

    def test0046(self, login_user_mobile="13592478554"):
        """
        单接口测试
        通话记录是否存在数据库中.正向流程-郭勇
        接口路径：POST /mobile/mobile-record/exist
        :return:
        """
        self.log.info("开始通话记录是否存在数据库中正向测试，接口路径/mobile/mobile-record/exist")
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_mobile_record_exist()

    def test0047(self, login_user_mobile="13592478554"):
        """
        单接口测试
        查询当前用户的家庭成员.正向流程-郭勇
        接口路径：POST /mobile/member/member-info-list
        :return:
        """
        self.log.info("开始执行查询当前用户的家庭成员正向测试，接口路径/mobile/member/member-info-list")
        self.plantTest.set_user()
        self.plantTest.mobile_member_member_info_list()

    def test0048(self, login_user_mobile="13592478554"):
        """
        单接口测试
        查询当前用户的家庭成员(当前用户排第一位).正向流程-郭勇
        接口路径：POST /mobile/member/member-info-order-list
        :return:
        """
        self.log.info("开始执行查询当前用户的家庭成员正向测试，接口路径/mobile/member/member-info-list")
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_member_member_info_order_list()

    def test0049(self, login_user_mobile="13592478554"):
        """
        单接口测试
        用户所在地天气.正向流程-郭勇
        接口路径：POST /mobile/member/member-weather
        :return:
        """
        adcode = [510000, 510100, 510101, 510104, 510105, 510106, 510107, 510108, 510112, 510113, 510114, 510115, 510116, 510117, 510121, 510129, 510131, 510132, 510181, 510182, 510183, 510184, 510185, 510300, 510301, 510302, 510303, 510304, 510311, 510321, 510322, 510400, 510401, 510402, 510403, 510411, 510421, 510422, 510500, 510501, 510502, 510503, 510504, 510521, 510522, 510524, 510525, 510600, 510601, 510603, 510623, 510626, 510681, 510682, 510683, 510700, 510701, 510703, 510704, 510705, 510722, 510723, 510725, 510726, 510727, 510781, 510800, 510801, 510802, 510811, 510812, 510821, 510822, 510823, 510824, 510900, 510901, 510903, 510904, 510921, 510922, 510923, 511000, 511001, 511002, 511011, 511024, 511025, 511083, 511100, 511101, 511102, 511111, 511112, 511113, 511123, 511124, 511126, 511129, 511132, 511133, 511181, 511300, 511301, 511302, 511303, 511304, 511321, 511322, 511323, 511324, 511325, 511381, 511400, 511401, 511402, 511403, 511421, 511423, 511424, 511425, 511500, 511501, 511502, 511503, 511521, 511523, 511524, 511525, 511526, 511527, 511528, 511529, 511600, 511601, 511602, 511603, 511621, 511622, 511623, 511681, 511700, 511701, 511702, 511703, 511722, 511723, 511724, 511725, 511781, 511800, 511801, 511802, 511803, 511822, 511823, 511824, 511825, 511826, 511827, 511900, 511901, 511902, 511903, 511921, 511922, 511923, 512000, 512001, 512002, 512021, 512022, 513200, 513201, 513221, 513222, 513223, 513224, 513225, 513226, 513227, 513228, 513230, 513231, 513232, 513233, 513300, 513301, 513322, 513323, 513324, 513325, 513326, 513327, 513328, 513329, 513330, 513331, 513332, 513333, 513334, 513335, 513336, 513337, 513338, 513400, 513401, 513422, 513423, 513424, 513425, 513426, 513427, 513428, 513429, 513430, 513431, 513432, 513433, 513434, 513435, 513436, 513437]
        adcode_random = random.choice(adcode)
        self.log.info("开始执行用户所在地天气正向测试，接口路径/mobile/member/member-weather")
        self.log.info("查询的adCode是%d" % adcode_random)
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_member_member_weather(adcode_random)

    def test0050(self, login_user_mobile="13592478554"):
        """
        单接口测试
        首页房间列表.正向流程-郭勇
        接口路径：POST /mobile/room/homepage-list
        :return:
        """
        self.log.info("开始执行首页房间类表正向测试，接口路径/mobile/room/homepage-list")
        self.plantTest.set_user("15282644233")
        self.plantTest.mobile_room_homepage_list()

    def test0051(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        单接口测试
        web端-生成病例.正向流程-郭勇
        接口路径：POST /admin/plant-case/create
        :return:
        """
        excel_info = xlrd.open_workbook(path.abspath(".")+"/utils/Docs/PestDatabase.xlsx").sheet_by_index(0)
        # 生成植物病例信息
        pest_row = random.randint(1, 337)
        plant_case_topic = excel_info.cell_value(pest_row, 0) + \
                           excel_info.cell_value(pest_row, 2) + \
                           "有" + \
                           excel_info.cell_value(pest_row, 1)
        plant_case_symptom = excel_info.cell_value(pest_row, 3)
        plant_case_treatment_method = excel_info.cell_value(pest_row, 6) \
            if \
            len(excel_info.cell_value(pest_row, 6)) > len(excel_info.cell_value(pest_row, 7)) \
            else \
            excel_info.cell_value(pest_row, 7)
        self.plantTest.set_user(login_user_mobile, passwd, True)
        db_get_users = DataBaseOperate().operate("39.104.28.40", "ms-user",
                                                 "SELECT id FROM t_base_user "
                                                 "WHERE account_type = 1 "
                                                 "AND is_delete = 0 "
                                                 "AND account_status = 1 "
                                                 "LIMIT 10")
        db_get_user_id = random.choice(db_get_users)["id"]
        # 开始执行测试
        self.log.info("开始执行web端-生成病例接口正向测试，接口路径/admin/plant-case/create")
        self.log.info("给用户%d生成了病例。\n病例主题：%s\n症状描述：%s\n诊断处方：%s\n" % (db_get_user_id, plant_case_topic, plant_case_symptom,         plant_case_treatment_method))
        self.plantTest.admin_plant_case_create(plant_case_topic, plant_case_symptom, plant_case_treatment_method, db_get_user_id)

    # def test0052(self, login_user_mobile="13828898130", passwd="8dw1bC"):
    #     """
    #     单接口测试
    #     web端-房间类型分组-列表.正向流程-郭勇
    #     接口路径：POST /mobile/room/group-list
    #     :return:
    #     """
    #     self.log.info("开始执行首页房间类表正向测试，接口路径/mobile/room/group-list")
    #     self.plantTest.set_user(login_user_mobile)
    #     self.plantTest.mobile_room_group_list()

    def test0053(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        单接口测试
        web端-查询病例.正向流程-郭勇
        接口路径：POST /admin/plant-case/list
        :return:
        """
        self.plantTest.set_user(login_user_mobile, passwd, True)
        self.log.info("开始执行查询病例接口正向测试，接口路径/admin/plant-case/list")
        self.plantTest.admin_plant_case_list(None, None, None, None, None, None, None, None, None, None, None, None, None, None)

    def test0054(self, login_user_mobile="13828898130", passwd="8dw1bC"):
        """
        单接口测试
        web端-病例详情.正向流程-郭勇
        接口路径：POST /admin/plant-case/detail
        :return:
        """
        plant_case_ids = DataBaseOperate().operate("39.104.28.40", "ms-plant",
                                                   "SELECT id FROM t_plant_case LIMIT 50")
        plant_case_id = random.choice(plant_case_ids)["id"]
        self.log.info("查看病例ID %s详情" % plant_case_id)
        self.log.info("开始执行病例详情接口正向测试，接口路径/admin/plant-case/detail")
        self.plantTest.set_user(login_user_mobile, passwd, True)
        self.plantTest.admin_plant_case_detail(plant_case_id)

    def test0055(self, login_user_mobile="13592478554"):
        """
        单接口测试
        app端-病例详情.正向流程-郭勇
        接口路径：POST /mobile/plantCase/detail
        :return:
        """
        plant_case_ids = DataBaseOperate().operate("39.104.28.40", "ms-plant",
                                                   "SELECT id FROM t_plant_case LIMIT 50")
        plant_case_id = random.choice(plant_case_ids)["id"]
        self.log.info("查看病例ID %s详情" % plant_case_id)
        self.log.info("开始执行病例详情接口正向测试，接口路径/mobile/plantCase/detail")
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_plantCase_detail(plant_case_id)

    def test0056(self, login_user_mobile="13592478554"):
        """
        单接口测试
        邀请页面-植物列表.正向流程-郭勇
        接口路径：POST /mobile/plant/list-for-invite
        :return:
        """
        get_user_id = self.plantTest.set_user(login_user_mobile).user_id
        self.log.info("开始执行邀请页面-植物列表接口正向测试，接口路径/mobile/plant/list-for-invite")
        self.plantTest.mobile_plant_list_for_invite(get_user_id)

    def test0057(self, login_user_mobile="13592478554"):
        """
        单接口测试
        微信获取access_token.正向流程-郭勇
        接口路径：POST /mobile/wx/getAccessToken
        :return:
        """
        self.log.info("开始执行微信获取access_token接口正向测试，接口路径/mobile/wx/getAccessToken")
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_wx_getAccessToken()

    def test0058(self, login_user_mobile="13592478554"):
        """
        单接口测试
        微信刷新access_token.正向流程-郭勇
        接口路径：POST /mobile/wx/refreshAccessToken
        :return:
        """
        self.log.info("开始执行微信刷新access_token接口正向测试，接口路径/mobile/wx/refreshAccessToken")
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_wx_refreshAccessToken()

    def test0059(self, login_user_mobile="13592478554"):
        """
        单接口测试
        微信签名.正向流程-郭勇
        接口路径：POST /mobile/wx/signature
        :return:
        """
        self.log.info("开始执行微信签名接口正向测试，接口路径/mobile/wx/signature")
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_wx_signature(self.faker_zh.uri())

    def test0099(self):
        """
        大爆炸集合测试-家庭类核心流程
        大爆炸集合测试.正向流程-郭勇
        :return:
        """
        self.log.info("----------开始核心流程测试----------")
        self.test0031()
        self.test0032()
        self.test0033()
        self.test0034()
        self.test0035()
        self.test0036()
        self.test0037()
        self.test0038()
        self.test0039()
        self.test0040()
        self.test0041()
        self.test0042()
        self.test0043()
        self.test0044()
        self.test0045()
        self.test0046()
        self.test0047()
        self.test0048()
        self.test0049()

    def test0066(self, login_user_mobile="18382373185"):
        self.plantTest.set_user(login_user_mobile)
        db_get_user_id = self.plantTest.set_user(login_user_mobile).user_id
        room_type = random.randint(10, 17)
        self.log.debug("添加房间")
        self.plantTest.mobile_room_add(room_type, db_get_user_id)

        self.log.debug("房间排序")
        room_sort = []
        for room_number in range(random.randint(1, 8)):
            room_sort.append({"roomType": random.randint(10, 17), "roomTypeOrder": room_number+1})
        self.plantTest.mobile_room_type_order(str(room_sort))

        self.log.debug("随机隐藏房间")
        db_get_user_homes = DataBaseOperate().operate("39.104.28.40", "ms-plant",
                                                      "SELECT id FROM t_room WHERE home_id = ("
                                                      "SELECT home_id FROM t_member WHERE user_id = %s )"
                                                      " AND is_delete = 0" % db_get_user_id)

        room_ids = []
        for x in db_get_user_homes:
            room_ids.append(x['id'])

        room_id = random.choice(room_ids)
        room_status = random.randint(0, 1)
        self.plantTest.mobile_room_show_status(room_id, room_status)

        self.log.debug("删除房间")
        group_lists = self.plantTest.mobile_room_group_list()
        group_list = group_lists.get("content")
        room_output_list = {}
        room_id = []
        for i in range(len(group_list)):
            room_output_lists = group_list[i]
            room_output_list = room_output_lists.get("roomOutputList")
            for j in range(len(room_output_list)):
                if room_output_list[j].get("plantNum") == 0:
                    room_id.append(room_output_list[j].get("id"))
        room_id_random = random.choice(room_id)
        self.plantTest.mobile_room_del(room_id_random)

        self.log.debug("手机号邀请家人")
        invite_user_name = self.faker_zh.name_female()
        self.plantTest.mobile_member_invite(str(self.invite_mobile), str(invite_user_name))

        self.log.debug("家人接受邀请")
        self.plantTest.mobile_member_accept(db_get_user_id, self.invite_mobile, "8888")

        self.log.debug("随机添加备注")
        db_get_user_home_users = DataBaseOperate().operate("39.104.28.40", "ms-plant",
                                                           "SELECT user_id FROM t_member WHERE home_id = ("
                                                           "SELECT home_id FROM t_member WHERE user_id = %s) "
                                                           "AND user_id != %s" % (db_get_user_id,db_get_user_id))
        get_users = []
        for x in db_get_user_home_users:
            get_users.append(x['user_id'])

        nick_user = random.choice(get_users)
        nick_name = self.faker_zh.name_female()
        self.plantTest.mobile_member_nick_edit(nick_user, nick_name)

        self.log.debug("发表留言")
        message_text = ["心相依，永不悔，有一种相遇叫最美，春花香，蝴蝶飞，有一种思念叫沉醉."]
        # 生成留言信息
        message_info = random.choice(message_text)
        message_address = self.faker_zh.address()
        message_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # 生成留言图片信息
        message_picture_tmp = []
        for x in range(random.randint(1, 9)):
            message_picture_tmp.append(self.faker_zh.uri())
        message_picture = ",".join(message_picture_tmp)
        self.log.info("留言内容为：%s, \n上传图片地址是 %s, \n留言地址：%s, \n留言时间： %s" % (message_info, message_picture,
                                                                         message_address, message_time))
        self.plantTest.mobile_message_board_add(message_info, message_picture, message_address, message_time, self.uuid)

        self.log.debug("被邀请的家人进行登录")
        self.plantTest.set_user(self.invite_mobile)

        self.log.debug("运营登录生成病例")
        self.plantTest.set_user('13828898130', '8dw1bC', True)
        excel_info = xlrd.open_workbook(path.abspath(".")+"/utils/Docs/PestDatabase.xlsx").sheet_by_index(0)
        pest_row = random.randint(1, 337)
        plant_case_topic = excel_info.cell_value(pest_row, 0) + \
                           excel_info.cell_value(pest_row, 2) + \
                           "有" + \
                           excel_info.cell_value(pest_row, 1)
        plant_case_symptom = excel_info.cell_value(pest_row, 3)
        plant_case_treatment_method = excel_info.cell_value(pest_row, 6) \
            if \
            len(excel_info.cell_value(pest_row, 6)) > len(excel_info.cell_value(pest_row, 7)) \
            else \
            excel_info.cell_value(pest_row, 7)
        self.log.info("给用户%d生成了病例。\n病例主题：%s\n症状描述：%s\n诊断处方：%s\n" % (db_get_user_id, plant_case_topic,
                                                                    plant_case_symptom, plant_case_treatment_method))
        self.plantTest.admin_plant_case_create(plant_case_topic, plant_case_symptom, plant_case_treatment_method,
                                               db_get_user_id)

        self.log.debug("查询病例列表")
        self.plantTest.admin_plant_case_list(None, None, None, None, None, None, None, None, None, None, None, None,
                                             None, None)
        self.log.debug("查看病例详情")
        plant_case_ids = DataBaseOperate().operate("39.104.28.40", "ms-plant",
                                                   "SELECT id FROM t_plant_case LIMIT 50")
        plant_case_id = random.choice(plant_case_ids)["id"]
        self.plantTest.set_user(login_user_mobile)
        self.plantTest.mobile_plantCase_detail(plant_case_id)
