# encoding: utf-8

"""
__author__ = "Zhang Pengfei"
__date__ = 2018/11/21
"""


from utils.Log import Log
from faker import Faker
from actions.DistributorAction import DistributorAction
import random


class Shop(object):
    L = Log('Shop')
    fake = Faker('zh_CN')

    def __init__(self, user, shop_name='', shop_mobile='', shop_contact=''):
        """
        初始化一个店铺对象
        :param user: 传一个用户对象
        :param shop_name: 店铺名称
        :param shop_mobile: 店铺手机号
        :param shop_contact: 店铺联系人
        """
        da = DistributorAction(user)
        if shop_name == '':
            self.name = str(user.mobile[1:])
        else:
            self.name = shop_name
        self.L.logger.debug("店铺名称为: %s" % str(self.name))

        if shop_mobile == '':
            pre_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151",
                        "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
            self.mobile = random.choice(pre_list)+"".join(random.choice("0123456789") for i in range(8))
        else:
            self.mobile = shop_mobile
        self.L.logger.debug("店铺手机号为: %s" % str(self.mobile))

        if shop_contact == '':
            shop_contact_name = self.fake.name()
            self.contact = shop_contact_name
        else:
            self.contact = shop_contact
        self.L.logger.debug("店铺联系人为: %s" % str(self.contact))

        self.avatar = da.upload_avatar()
        self.L.logger.debug("头像链接为: %s" % str(self.avatar))

        self.lat = round(random.uniform(30.5, 30.7), 4)
        self.L.logger.debug("纬度为: %s" % str(self.lat))
        self.lng = round(random.uniform(103.9, 104.2), 3)
        self.L.logger.debug("经度为: %s" % str(self.lng))
        self.province = 41
        self.city = 4101
        self.area = '高新区'
        self.address = self.fake.address()
        self.L.logger.debug("地址为: %s" % str(self.address))

        self.shopId = user.channel_shop_id
        self.supplier_shop_id = user.supplier_shop_id


# if __name__ == '__main__':
#     from backend.User import User
#
#     seller = User("18380581415")
#     seller.change_identity(2)
#
#     s = Shop(seller)
