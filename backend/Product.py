# encoding: utf-8

"""
__author__ = "Zhang Pengfei"
__date__ = 2018/11/20
"""

from utils.Log import Log
from faker import Faker
from actions.DistributorAction import DistributorAction
import random


class Product(object):
    L = Log('Product')
    fake = Faker('zh_CN')

    def __init__(self, user, parent_category_name='', category_name='', product_name='自动化默认商品名',
                 price=1, store_unit_name='', store=100, freight_id=None,
                 product_status=10, product_service_type=20):
        """
        初始化一个商品对象的信息
        :param user: 用户对象
        :param parent_category_name: 一级分类名称
        :param category_name: 二级分类名称
        :param product_name: 商品名称
        :param price: 价格(分)
        :param store_unit_name: 单位随机
        :param store: 库存数量
        :param freight_id: 运费模板ID,-1表示免运费
        :param product_status:商品上下架状态,10:上架,20:下架
        :param product_service_type: 商品所在平台,20:渠道商
        """
        da = DistributorAction(user)
        category_list = da.list_all_category()['content']
        category_list_parent_id = []
        for i in category_list:
            category_list_parent_id.append(i['parent'])
        parent_category_dict = {}
        erji_category_list = {}
        for category in category_list:
            if category['parent'] == 0 and category['id'] in category_list_parent_id:
                parent_category_dict[category['name']] = category['id']
            else:
                if erji_category_list.get(str(category['parent'])) is None:
                    erji_category_list[str(category['parent'])] = []
                erji_category_list[str(category['parent'])].append(category)
        if parent_category_name == '':
            self.parent_category_id = parent_category_dict.get(random.choice(list(parent_category_dict.keys())))
            self.L.logger.debug("一级分类ID为: %s" % self.parent_category_id)
        elif parent_category_dict.get(parent_category_name) is not None:
            self.parent_category_id = parent_category_dict.get(parent_category_name)
            self.L.logger.debug("一级分类ID为: %s" % self.parent_category_id)
        else:
            raise Exception("未找到该一级分类")
        flag = 0

        if category_name == '':
            flag = 1
            self.category_id = random.choice(erji_category_list[str(self.parent_category_id)])['id']
        else:
            for i in erji_category_list[str(self.parent_category_id)]:
                if i['name'] == category_name:
                    flag = 1
                    self.category_id = i['id']

        if flag == 0:
            raise Exception("未找到该二级分类")
        else:
            self.L.logger.debug("二级分类ID为: %s" % self.category_id)

        self.channel_shop_id = user.channel_shop_id
        self.supplier_shop_id = user.supplier_shop_id
        self.L.logger.debug("店铺ID为: %s" % self.channel_shop_id)
        self.name = product_name
        self.L.logger.debug("商品名称为: %s" % self.name)
        self.price = price
        self.L.logger.debug("商品价格为: %s" % self.price)

        unit_list = da.list_store_unit()['content']
        flag = 0
        if store_unit_name == '':
            self.unit_id = random.choice(unit_list)['id']
            flag = 1
        else:
            for i in unit_list:
                if i['name'] == store_unit_name:
                    flag = 1
                    self.unit_id = i['id']
        if flag == 0:
            raise Exception("未找到该单位")
        else:
            self.L.logger.debug("单位ID为: %s" % str(self.unit_id))

        self.store = store
        self.L.logger.debug("商品库存为: %s" % str(self.store))
        self.status = product_status
        self.L.logger.debug("商品状态为: %s" % str(self.status))
        self.product_serviceType = product_service_type
        self.L.logger.debug("商品平台为: %s" % str(self.product_serviceType))
        self.image = da.upload_img_product()
        self.L.logger.debug("商品图片链接为: %s" % str(self.image))
        self.content = str(self.fake.text().replace("\n", " "))[:20]
        self.L.logger.debug("商品描述为: %s" % str(self.content))

        if freight_id is not None:
            self.freight_id = freight_id
        else:
            freight_list = da.all_freight()['content']
            self.freight_id = freight_list[self.fake.random_int(0, len(freight_list)-1)]['id']
            self.L.logger.debug("商品运费模板ID为: %s" % str(self.freight_id))


# if __name__ == '__main__':
#     from backend.User import User
#
#     seller = User("14500000000")
#     seller.change_identity(2)
#
#     p = Product(seller)
