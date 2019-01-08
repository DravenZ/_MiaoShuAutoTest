#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/8/11'
"""

from utils.Log import Log
from utils.Util import Request
from utils.Config import Config
import smtplib
from email.mime.text import MIMEText
import os
import re
import json
import codecs
import time
import datetime
import difflib
import sys

L = Log('Update')
hosts = Config('config').data['hosts']['DEV']


def search_files_by_type(path, file_type):
    # return SORTED file list according to CREATED TIME
    file_list = []
    file_name = []
    # rootPath = []
    tmp_dict = {}
    purpose = []
    for root, dirs, files in os.walk(path):
            for fn in files:
                    file_list.append(root+'/'+fn)
                    file_name.append(fn)
                    # rootPath.append(root)
    for num in range(len(file_name)):
            if file_name[num][(0-len(file_type)):] == file_type:
                    tmp_dict[os.stat(file_list[num]).st_mtime] = file_list[num]
    # print(tmp_dict)
    sort_time_stamps = sorted(tmp_dict.keys())
    # print(sort_time_stamps)
    for k in sort_time_stamps:
        purpose.append(tmp_dict[k])
        # time_array = time.localtime(k)
        # other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        # print(other_style_time)
        # print tmpDict[k]
    # print(purpose)
    return purpose


def get_paths_txt(file_name, host_name):
    json_content = Request().get(str(host_name) + '/v2/api-docs')
    paths = json.loads(json_content)["paths"]
    path_detail_list = []
    for p in paths:
        para_desc_list = []
        try:
            desc = paths[p]["post"].get("tags", [])[0]
            para_desc_list.append(desc)
            # L.logger.debug("{'%s': '%s'}" % (p, desc))
            paras = paths[p]["post"].get("parameters", [])
        except KeyError:
            desc = paths[p]["get"].get("tags", [])[0]
            para_desc_list.append(desc)
            # L.logger.debug("{'%s': '%s'}" % (p, desc))
            paras = paths[p]["get"].get("parameters", [])
        p_dict = {}
        if paras is None:
            pass
        else:
            for para in paras:
                p_dict[para['name']] = u"%s_%s_%s" % (para.get('type', 'noType'),
                                                      para.get('required', 'noRequired'),
                                                      para.get('description', 'noDescription'))
        para_desc_list.append(p_dict)
        path_detail_list.append({p: para_desc_list})
    # demand_list = sorted(path_detail_list)
    now = time.strftime("_%Y-%m-%d_%H%M%S", time.localtime())
    # L.logger.debug(path_detail_list)
    current_path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(current_path + "/Docs"):
        os.makedirs(current_path + "/Docs")
    with codecs.open('./' + str(file_name) + now + '.txt', 'a', 'utf-8') as f:
        f.write(host_name + '\n')
        for item in path_detail_list:
            for k, v in item.items():
                if isinstance(v[1], dict):
                    f.write('\n  %s, %s\n' % (k, v[0]))
                    for x, y in v[1].items():
                        f.write('    %s, %s\n' % (x, y))


def get_paths_yaml(file_name, host_name):
    json_content = Request().get(str(host_name) + '/v2/api-docs')
    paths = json.loads(json_content)["paths"]
    path_detail_list = []
    for p in paths:
        para_desc_list = []
        try:
            desc = paths[p]["post"].get("tags", [])[0]
            para_desc_list.append(desc)
            # L.logger.debug("{'%s': '%s'}" % (p, desc))
            paras = paths[p]["post"].get("parameters", [])
        except KeyError:
            desc = paths[p]["get"].get("tags", [])[0]
            para_desc_list.append(desc)
            # L.logger.debug("{'%s': '%s'}" % (p, desc))
            paras = paths[p]["get"].get("parameters", [])
        p_dict = {}
        if paras is None:
            pass
        else:
            for para in paras:
                p_dict[para['name']] = u"%s_%s_%s" % (para.get('type', 'noType'),
                                                      para.get('required', 'noRequired'),
                                                      para.get('description', 'noDescription'))
        para_desc_list.append(p_dict)
        path_detail_list.append({p: para_desc_list})
    # demand_list = sorted(path_detail_list)
    now = time.strftime("_%Y-%m-%d_%H%M%S", time.localtime())
    # L.logger.debug(path_detail_list)
    current_path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(current_path + "/Docs"):
        os.makedirs(current_path + "/Docs")
    with codecs.open('./' + str(file_name) + now + '.yaml', 'a', 'utf-8') as f:
        f.write(host_name + ':\n')
        for item in path_detail_list:
            for k, v in item.items():
                if isinstance(v[1], dict):
                    f.write('  %s:\n' % k)
                    for x, y in v[1].items():
                        f.write('    %s:\n' % x)


def get_api_statistics(file_name, host_name):
    json_content = Request().get(str(host_name) + '/v2/api-docs')
    paths = json.loads(json_content)["paths"]
    path_detail_list = []
    for p in paths:
        para_desc_list = []
        try:
            desc = paths[p]["post"].get("tags", [])[0]
            para_desc_list.append(desc)
            # L.logger.debug("{'%s': '%s'}" % (p, desc))
            paras = paths[p]["post"].get("parameters", [])
        except KeyError:
            desc = paths[p]["get"].get("tags", [])[0]
            para_desc_list.append(desc)
            # L.logger.debug("{'%s': '%s'}" % (p, desc))
            paras = paths[p]["get"].get("parameters", [])
        p_dict = {}
        if paras is None:
            pass
        else:
            for para in paras:
                p_dict[para['name']] = u"%s_%s_%s" % (para.get('type', 'noType'),
                                                      para.get('required', 'noRequired'),
                                                      para.get('description', 'noDescription'))
        para_desc_list.append(p_dict)
        path_detail_list.append({p: para_desc_list})
    # demand_list = sorted(path_detail_list)
    now = time.strftime("_%Y-%m-%d_%H%M%S", time.localtime())
    # L.logger.debug(path_detail_list)
    current_path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(current_path + "/Docs"):
        os.makedirs(current_path + "/Docs")
    # with codecs.open('./Docs/' + str(host_name).split(".")[1] + now + '.txt', 'a', 'utf-8') as f:
    with codecs.open('./PATH_ONLY_' + str(file_name) + now + '.txt', 'a', 'utf-8') as f:
        for item in path_detail_list:
            for k, v in item.items():
                if isinstance(v[1], dict):
                    f.write('%s%s, %s\n' % (host_name, k, v[0]))


def get_action_statistics(file_name):
    with codecs.open('./../actions/' + str(file_name) + '.py', 'r', 'utf-8') as f:
        content = f.read()
        demand = re.findall("http[^\n',]*", content)
        for d in demand:
            print(d)


def get_diff(t1, t2):
    with codecs.open(t1, 'r', 'utf-8') as a:
        t1_set = set(a.readlines())
    with codecs.open(t2, 'r', 'utf-8') as b:
        t2_set = set(b.readlines())
    print(u"%s相对于%s新增了如下接口" % (t2, t1))
    for t in (t2_set-t1_set):
        print(t[:-1])
    print(u"%s相对于%s减少了如下接口" % (t2, t1))
    for t in (t1_set - t2_set):
        print(t[:-1])


# get_diff('./9601_2018-06-28_00_00_18.txt', './9604_2018-06-27_22_32_25.txt')


def run_compare(f1, f2):
    """主函数"""
    # try:
    #     # 获取文件名
    #     f1 = sys.argv[1]
    #     f2 = sys.argv[2]
    # except Exception as e:
    #     print("Error: " + str(e))
    #     print("Usage : python compareFile.py filename1 filename2")
    #     sys.exit()
    # # 参数不够
    # if f1 == "" or f2 == "":
    #     print("Usage : python compareFile.py filename1 filename2")
    #     sys.exit()
    tf1 = read_file(f1)
    tf2 = read_file(f2)

    # 创建一个实例difflib.HtmlDiff
    d = difflib.HtmlDiff()
    # 生成一个比较后的报告文件，格式为html
    write_file(d.make_file(tf1, tf2))


def read_file(filename):
    """读取文件，并处理"""
    try:
        file_handle = open(filename, "r")
        text = file_handle.read().splitlines()
        file_handle.close()
        return text
    except IOError as e:
        print("Read file error: " + str(e))
        sys.exit()


def write_file(file_name):
    """写入文件"""
    html_name = 'diff_{}.html'.format(datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.%f"))
    diff_file = open(html_name, "w")
    diff_file.write("<meta charset='UTF-8'>")
    diff_file.write(file_name)
    # 提示文件生成在什么地方
    print("The file on {}".format(os.path.abspath(str(diff_file.name))))
    diff_file.close()


def del_one_of_two_txt():
    files = search_files_by_type("./Docs", "txt")
    for key, host in hosts.items():
        print(key)
        # 删除多余文件
        group = []
        for f in files:
            # get_api_statistics(key, host)
            if f.startswith("./Docs/%s" % key):
                group.append(f)
            else:
                pass
        if len(group) > 1:
            group_dict = {}
            for g in group:
                print("文件:%s 创建时间:%s" % (g, os.path.getctime(g)))
                group_dict[os.path.getctime(g)] = g
            min_time_stamp = min(group_dict.keys())
            print("每个服务最小时间戳: %s" % min(group_dict.keys()))
            oldest_file_name = group_dict[min_time_stamp]
            print("每个服务最小时间戳文件: %s" % oldest_file_name)
            os.remove(oldest_file_name)
            print("每个服务最小时间戳文件 %s 删除成功" % oldest_file_name)
        else:
            print("每个服务文件数不足2个")


def add_latest_txt():
    for key, host in hosts.items():
        print(key)
        try:
            get_paths_txt(key, host)
        except Exception as e:
            print(e)


def add_latest_yaml():
    for key, host in hosts.items():
        print(key)
        try:
            get_paths_yaml(key, host)
        except Exception as e:
            print(e)


def add_path_only_txt():
    for key, host in hosts.items():
        print(key)
        try:
            get_api_statistics(key, host)
        except Exception as e:
            print(e)


def get_diff_html():
    files = search_files_by_type("/Users/hengxin/PycharmProjects/MiaoShuAutoTest/utils/Docs", "txt")
    for key, host in hosts.items():
        print(key)
        # 删除多余文件
        group = []
        for f in files:
            if f.startswith("/Users/hengxin/PycharmProjects/MiaoShuAutoTest/utils/Docs/%s" % key):
                group.append(f)
            else:
                pass
        print(group)
        run_compare(group[0], group[1])
        html = search_files_by_type("./", "html")
        for h in html:
            if h.startswith(".//diff"):
                os.rename(h, "./Docs/%s_%s.html" % (key, datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")))


def send_html_report():
    files = search_files_by_type("./", "html")
    sender = 'xin.heng@worldfarm.com'
    receiver = 'xin.heng@worldfarm.com'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')
    smtp.login('xin.heng@worldfarm.com', 'Knight01')
    for f in files:
        print(f)
        file_content = open(f, 'r').read()
        msg = MIMEText(file_content, 'html', 'utf-8')
        msg['Subject'] = '%s API Compare' % f[7:-12]
        msg['from'] = sender
        msg['to'] = receiver
        smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    # run_compare('/Users/hengxin/PycharmProjects/MiaoShuAutoTest/utils/Docs/MS_PASSPORT_2018-11-21_135006.txt',
    #             '/Users/hengxin/PycharmProjects/MiaoShuAutoTest/utils/Docs/MS_PASSPORT_2018-12-17_161831.txt')
    # search_files_by_type("/Users/hengxin/PycharmProjects/MiaoShuAutoTest/utils/Docs", "txt")
    # get_latest_path_only
    # add_path_only_txt()
    # add_latest_yaml()
    # 删除旧的服务端接口txt
    # del_one_of_two_txt()
    # 获得最新的服务端接口txt
    # add_latest_txt()
    # 生成新的对比html文件
    # try:
    #     get_diff_html()
    # except Exception as e:
    #     print(e)

    # 使用邮件发送html报告
    send_html_report()
