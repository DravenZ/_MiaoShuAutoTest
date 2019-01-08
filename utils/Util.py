#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/3/28'
"""


import requests
import pymysql
import redis
import json
import datetime
import decimal
import os
import platform
import re
import mimetypes
from utils.Log import Log
from time import sleep
import urllib.parse
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from multiprocessing import Process
import subprocess

header = {"Content-Type": "application/x-www-form-urlencoded",
               "Accept": "application/json",
               "User-Agent": "IFFamilyFarm/1.0.0 (iPhone; iOS 12.1; Scale/3.00)"
               }


class Request(object):

    L = Log("Request")

    @staticmethod
    def url_encode(string):
        cn = ''
        for ch in string.decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                cn += urllib.parse.quote(ch.encode('utf-8'))
            else:
                cn += ch.encode('utf-8')
        return cn

    def post(self, url, data, headers=header):
        client = requests.session()
        response = client.post(url=url, data=data, headers=headers, cookies=None).content
        self.L.logger.debug("\n request: %s\ndata: %s" %
                            (url, data))
        try:
            response_json = json.loads(response)
            self.L.logger.debug("\n" + json.dumps(response_json, ensure_ascii=False,
                                                  sort_keys=True, indent=2, separators=(',', ': ')))
        except ValueError:
            self.L.logger.debug(response)
        return response.decode("utf-8")

    def get(self, url, headers=header):
        client = requests.session()
        response = client.get(url=url, headers=headers).content
        try:
            self.L.logger.debug('''
                                   request: %s,
                                   response: %s
                                ''' % (url, response.decode("utf-8")))
            response_json = json.loads(response.decode("utf-8"))
            self.L.logger.debug("\n" + json.dumps(response_json, ensure_ascii=False,
                                                  sort_keys=True, indent=2, separators=(',', ': ')))
        except ValueError:
            self.L.logger.debug(response)
        return response.decode("utf-8")

    def post_file(self, url, file_path, file_key, data_dict=None):
        file_name = file_path.split("/")[-1:][0]
        file_bin_data = open(file_path, 'rb')
        content_type = str(mimetypes.types_map.get("." + file_path.split(".")[-1:][0], None))
        encode_file_name = urllib.parse.quote(file_name, safe='&?=:/', encoding='UTF-8', errors=None)
        files = {file_key: (encode_file_name, file_bin_data, content_type)}
        resp = requests.post(url=url, data=data_dict, files=files).content
        self.L.logger.debug('''
                               request: %s,
                               file: %s,
                               data: %s,
                               response: %s
                            ''' % (url, file_path, data_dict, resp.decode("utf-8")))
        try:
            response_json = json.loads(resp)
            self.L.logger.debug("\n" + json.dumps(response_json, ensure_ascii=False,
                                                  sort_keys=True, indent=2, separators=(',', ': ')))
        except ValueError:
            self.L.logger.debug(resp)
        return resp


class DataBaseOperate(object):
    L = Log("DataBaseOperate")

    def operate(self, host_ip, database_name, sql):
        if host_ip == "39.104.28.40":
            user, password, port = "root", "YYJNo$QsaaSjgb8U3JoigB", 3306
        elif host_ip == "47.74.129.65":
            user, password, port = "farm_test", "r2rublBL4qJMc", 3306
        elif host_ip == "67.218.159.111":
            user, password, port = "root", "Knight01", 3306
        elif host_ip == "132.232.47.119":
            user, password, port = "ms", "MiaoShu@2018", 3306
        else:
            raise Exception('数据库IP地址错误: %s' % host_ip)
        try:
            db = pymysql.connect(host=host_ip,
                                 port=port,
                                 user=user,
                                 db=database_name,
                                 passwd=password)
            con = db.cursor(cursor=pymysql.cursors.DictCursor)
            con.execute(sql)
            results = con.fetchall()
            # print(results)
            for result in results:
                for fields in result:
                    if isinstance(result[fields], datetime.datetime):
                        result[fields] = str(result[fields].strftime('%Y-%m-%d %H:%M:%S'))
                    elif isinstance(result[fields], datetime.date):
                        result[fields] = str(result[fields].strftime('%Y-%m-%d'))
                    elif isinstance(result[fields], decimal.Decimal):
                        result[fields] = float(result[fields])
            db.commit()
            con.close()
            # print(results)
            self.L.logger.debug("\n" + json.dumps(results, ensure_ascii=False,
                                                  sort_keys=True, indent=2, separators=(',', ': ')))
            return results
        except Exception as e:
            self.L.logger.error(e)


class Redis(object):
    L = Log("Redis")
    pool = redis.ConnectionPool(host='39.104.28.40', port=6379, db=2, password='YYJNo$QsaaSjgb8U3JoigB')
    r = redis.Redis(connection_pool=pool)

    def set(self, key, value):
        self.r.set(key, value)
        self.L.logger.debug('Set %s = %s' % (str(key), str(value)))

    def get(self, key):
        value = self.r.get(key)
        self.L.logger.debug('Get %s = %s' % (str(key), str(value)))
        if value is not None:
            value = value.decode()
        return value

    def delete(self, key):
        self.r.delete(key)
        self.L.logger.debug('Delete %s' % str(key))

    def exists(self, key):
        exist = self.r.exists(key)
        self.L.logger.debug('exist? %s' % str(exist))
        return exist


class RedisNew(object):
    L = Log("Redis")
    pool = redis.ConnectionPool(host='67.218.159.111', port=6699, db=7, password='Knight01')
    r = redis.Redis(connection_pool=pool)

    def set(self, key, value):
        self.r.set(key, value)
        self.L.logger.debug('Set %s = %s' % (str(key), str(value)))

    def get(self, key):
        value = self.r.get(key)
        self.L.logger.debug('Get %s = %s' % (str(key), str(value)))
        return value.decode()

    def delete(self, key):
        self.r.delete(key)
        self.L.logger.debug('Delete %s' % str(key))

    def exists(self, key):
        exist = self.r.exists(key)
        self.L.logger.debug('exist? %s' % str(exist))
        return exist


class AndroidTool(object):
    from uiautomator import device as d
    L = Log("AndroidTool")

    def run_command(self, shell_command):
        handle = subprocess.Popen(shell_command, stdout=subprocess.PIPE, shell=True)
        self.L.logger.debug("%s 命令已执行" % shell_command)
        value = handle.stdout.read().decode("utf-8")
        return value

    def reset_app(self, package_name):
        status = self.run_command("adb shell pm clear %s" % package_name)
        if status == "Success":
            self.L.logger.debug(u"初始化苗叔 %s" % status)
            return True
        else:
            self.L.logger.debug(u"初始化苗叔 %s" % status)
            return False

    def get_device(self):
        if self.run_command("adb devices") == "List of devices attached\n\n":
            self.L.logger.debug("No Android Device Connected, Please Connect One")
            return False
        else:
            return True

    @staticmethod
    def get_info(shell_command):
        handle = subprocess.Popen(shell_command, stdout=subprocess.PIPE, shell=True)
        response = handle.stdout.read().decode("utf-8")
        if response:
            if platform.system() == "Windows":
                return response.split(":")[1][1:-3]
            elif platform.system() == "Darwin":
                return response.split(":")[1][1:-2]
        else:
            return 'unknown'

    def get_brand(self):
        # 手机品牌
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.product.brand"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.product.brand"')

    def get_model(self):
        # 手机型号
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.product.model"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.product.model"')

    def get_android_version(self):
        # Android版本号
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.build.version.release"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.build.version.release"')

    def get_sdk_version(self):
        # SDK版本号
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.build.version.sdk"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.build.version.sdk"')

    def get_manufacturer(self):
        # 手机制造商
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.product.manufacturer"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.product.manufacturer"')

    def get_sn(self):
        # 序列号
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.serialno"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "persist.sys.product.serialno"')

    def get_device_name(self):
        # 设备号
        if platform.system() == "Windows":
            name = self.get_info('adb shell getprop | findstr "ro.serialno"')
            return name
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.serialno"')[1:]

    def get_resolution(self):
        # 设备分辨率
        # adb shell dumpsys window displays | head -n 3
        if platform.system() == "Windows":
            return self.run_command('adb shell dumpsys window displays | findstr "init"').split(" ")[4][5:]
        elif platform.system() == "Darwin":
            return self.run_command('adb shell dumpsys window displays | grep "init" | head -n 3').split(" ")[4][5:]
        # return self.getInfo('adb shell wm size') #仅适用于高通平台

    def get_cpu(self):
        # 处理器
        if platform.system() == "Windows":
            return self.get_info('adb shell cat /proc/cpuinfo | findstr "Processor"')[:-12]
        elif platform.system() == "Darwin":
            return self.get_info('adb shell cat /proc/cpuinfo | grep "Processor"')

    def get_device_info(self):
        return ("%s]_[%s]_%s_%s_%s" % (
            self.get_model(), self.get_resolution(), self.get_android_version(),
            self.get_sdk_version(), self.get_cpu()))

    def set_unicode_ime(self):
        adb_return = self.run_command("adb shell ime list -a")
        ime_list = re.findall('.*/.*:', str(adb_return))
        try:
            unicode_index = ime_list.index('io.appium.android.ime/.UnicodeIME:')
            set_ime_return = self.run_command("adb shell ime set %s" % ime_list[unicode_index][:-1])
            self.L.logger.debug(set_ime_return)
            self.L.logger.debug(u"unicode输入法 已设置")
        except ValueError:
            self.L.logger.debug(u"未安装 unicode输入法")
            install_return = self.run_command("adb install -r ./unicode_keyboard.apk")
            self.L.logger.debug(install_return)
            self.L.logger.debug(u"unicode输入法 已安装")
            adb_return = self.run_command("adb shell ime list -a")
            ime_list = re.findall('.*/.*:', str(adb_return))
            unicode_index = ime_list.index('io.appium.android.ime/.UnicodeIME:')
            set_ime_return = self.run_command("adb shell ime set %s" % ime_list[unicode_index][:-1])
            self.L.logger.debug(set_ime_return)
            self.L.logger.debug(u"unicode输入法 已设置")

    def reset_ime(self):
        set_ime_return = self.run_command("adb shell ime set %s" % "com.sohu.inputmethod.sogou.xiaomi/.SogouIME")
        self.L.logger.debug(set_ime_return)
        self.L.logger.debug(u"输入法 已恢复")

    def get_screen_shot(self):
        self.d.screenshot('error.jpg')

    def swipe_up_miaoshu(self):
        middle_x = self.d.info['displayWidth'] / 2
        start_y = self.d.info['displayHeight'] * 0.8
        end_y = self.d.info['displayHeight'] * 0.2
        while self.d.swipe(middle_x, start_y, middle_x, end_y) is False:
            self.L.logger.info("滑动失败")
        self.L.logger.info("滑动成功")

    def get_package_name(self, apk_path):
        activity_line = self.run_command("aapt d badging %s | grep 'package'" % apk_path)
        package_name = activity_line.split("'")[1]
        return  package_name

    def get_launch_activity_name(self, apk_path):
        activity_line = self.run_command("aapt d badging %s | grep 'launchable'" % apk_path)
        activity_name = activity_line.split("'")[1]
        return activity_name

    def check_app_exist(self, package_name):
        exist = self.run_command("adb shell pm list packages | grep %s" % package_name)
        if exist:
            self.L.logger.info("%s应用已安装" % package_name)
            return True
        else:
            self.L.logger.warning("%s应用未安装" % package_name)
            return False

    def install_apk(self, apk_path):
        self.run_command("adb install -t %s" % apk_path)

    def install_app(self, apk_path):
        self.d.watcher("检查是否有授权弹窗").when(text="继续安装").click(text="继续安装")
        p = Process(target=self.install_apk, args=(apk_path,))
        p.start()
        sleep(2)
        self.d(text="guoyong").exists
        print("是否找到文本：" + str(self.d(text="guoyong").exists))
        print("是否执行守望者：" + str(self.d.watchers.triggered))
        self.d.watchers.reset()
        # print("已安装或安装过程中，请稍后...")

    def launch_app_by_apk(self, apk_path):
        self.unlock_screen("1983")
        activity_name = self.get_launch_activity_name(apk_path)
        package_name = self.get_package_name(apk_path)
        if self.check_app_exist(package_name) is False:
            self.install_app(apk_path)
        self.set_up_miaoshu()
        launchable_act_name = activity_name.replace(package_name, package_name + '/')
        self.run_command("adb shell am start -n %s" % launchable_act_name)
        self.L.logger.info("测试开始, 启动%s成功" % package_name)

    def unlock_screen(self, password):
        self.d.screen.off()
        self.d.screen.on()
        self.swipe_up_miaoshu()
        self.run_command("adb shell input text %s && adb shell input keyevent 66" % password)

    def set_up_miaoshu(self):
        self.L.logger.info("测试设备: " + self.get_device_info())
        self.set_unicode_ime()
        self.reset_app("com.dnkj.family.farm")
        self.d.wait.update()

    def tear_down_miaoshu(self):
        self.reset_ime()
        self.reset_app("com.dnkj.family.farm")
        self.L.logger.info("测试完成, 清理测试")

    def login_miaoshu(self, login_mobile, verify_code):
        self.d.wait.update()
        self.d(text="允许").click()
        self.d.wait.update()
        self.d(text="我的").click()
        self.d.wait.update()
        self.d(text="请输入手机号").set_text(str(login_mobile))
        self.d(text="请输入验证码").set_text(str(verify_code))
        self.d(text="登录").click()
        self.d.wait.update()
        self.L.logger.info("手机号 %s 登录成功" % str(login_mobile))

    def enter_shop(self, shop_name):
        self.d.wait.update()
        shop_name_str = str(shop_name)
        self.d(resourceId="com.dnkj.family.farm:id/root_layout").click()
        self.d(resourceId="com.dnkj.family.farm:id/et_search").set_text(shop_name_str)
        self.d.press.enter()
        sleep(4)
        self.d(text=shop_name_str)[1].click()

    def pay_product(self):
        self.d.wait.update()
        self.d(text="立即购买").click()
        self.d.wait.update()
        self.d(text="确定").click()
        sleep(3)
        self.L.logger.info("加入购物车 成功")
        self.d(text="确认订单")[1].click()
        self.d.wait.update()
        self.L.logger.info("确认订单 成功")
        self.d.wait.update()
        self.d(text="确认支付  ￥").click()
        self.L.logger.info("确认支付 成功")
        self.d(text="立即支付").click()
        self.d.wait.update()
        self.L.logger.info("支付成功")
        InputWalletPassWord("123123")
        self.d.wait.update()
        self.d(text="返回商家").click()
        sleep(5)
        self.d(text="查看订单").click()
        self.d.wait.update()
        self.swipe_up_miaoshu()
        self.d.wait.update()
        self.d.screenshot("order.jpg")


class Mail(object):

    def send_html_email(self):
        sender = 'xin.heng@worldfarm.com'
        receiver = ['qa@worldfarm.com', 'changle.yu@worldfarm.com', 'xi.he@worldfarm.com']
        smtp = smtplib.SMTP()
        smtp.connect('smtp.exmail.qq.com')
        smtp.login('xin.heng@worldfarm.com', 'Knight01')
        log_content = open("/Users/hengxin/PycharmProjects/MiaoShuAutoTest/utils/Logs/AndroidTool.log", 'r')\
            .read().replace('\n', '<br />')
        file_content = open("./order.jpg", 'rb').read()
        msg_image = MIMEImage(file_content)
        msg_image.add_header('Content-ID', '<order>')
        msg = MIMEMultipart('related')
        msg_alt = MIMEMultipart('alternative')
        msg_text = MIMEText('<p><img src="cid:order" height="720" width="360"></p>'
                            '<p>%s</p>' % log_content, 'html')
        msg['Subject'] = '苗叔一期自动化付款流程'
        msg['from'] = sender
        msg['to'] = ','.join(receiver)
        msg.attach(msg_text)
        msg.attach(msg_alt)
        msg.attach(msg_image)
        smtp.sendmail(from_addr=sender, to_addrs=receiver, msg=msg.as_string())
        smtp.quit()


class InputWalletPassWord(object):
    from uiautomator import device as d

    def __init__(self, passWord):
        self.passWord = passWord
        self.passWordZone = self.d(resourceId="com.tencent.mm:id/ak2").bounds
        self._inputPassWord()

    def _cellLocation(self):
        keys = [()]
        passWordVertical = int((self.passWordZone["bottom"] - self.passWordZone["top"]) / 4)
        passWordCrosswise = int((self.passWordZone["right"] - self.passWordZone["left"]) / 3)
        # 计算1位置,keys1
        keys.append((passWordCrosswise / 2 + self.passWordZone["left"], passWordVertical / 2 + self.passWordZone["top"]))
        #计算2-9-0位置
        for i in range(2, 11):
            if i < 4:
                #计算横向2-3坐标点
                keys.append((keys[i-1][0] + passWordCrosswise, keys[i-1][1]))
            elif i == 10:
                # 计算0位置,相对位置8
                keys[0] = (keys[8][0], keys[8][1] + passWordVertical)
            else:
                #竖向计算4-9坐标点
                keys.append((keys[i-3][0], keys[i-3][1] + passWordVertical))
        return keys

    def _inputPassWord(self):
        key = self._cellLocation()
        for i in self.passWord:
            self.d.click(key[int(i)][0], key[int(i)][1])


# if __name__ == '__main__':
#     db = DataBaseOperate()
    # Request().post_file(url="http://192.168.62.253:31012/mobile/supplier/upload", data_dict={},
    #                     file_path="./../actions/2.jpg", file_key="identityFile")
    # print(Redis().get('ShopManagerImpl:modify_shop_mobile:1025_15283855883'))

