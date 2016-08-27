#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys
import config, hostfile

PROJECT_ROOT = os.path.abspath(os.path.expanduser('~')+"/.HostHelper")
DEFINITIONS_ROOT = os.path.join(PROJECT_ROOT, 'config')
CONFIG_NAME = "host.properties"
HOST_PROPERTIES = os.path.join(DEFINITIONS_ROOT, CONFIG_NAME)
if not os.path.exists(DEFINITIONS_ROOT):
    os.makedirs(DEFINITIONS_ROOT)
if not os.path.exists(HOST_PROPERTIES):
    # os.mknod(CONFIG_NAME)
    os.system("touch " + HOST_PROPERTIES)

def __readlines():
    """获取host.properties的文件内容"""
    fp = open(HOST_PROPERTIES, 'r+')
    return fp.readlines()

def __apend(content):
    fp = open(HOST_PROPERTIES, 'a')
    fp.write(content)
    fp.flush()
    fp.close()

def __getconfigs():
    lines = __readlines()
    configs = []
    for line in lines:
        if line != "":
            linearray = line.strip('\n').split(" ")
            configs.append(config.Config(linearray[0], linearray[1]))
    return configs

def __addconfigs(name):
    content = name+" "+str(1)+"\n"
    __apend(content)

"""根据名称获取内容"""
def addContent(name):
    list = __getconfigs()
    have = 0
    for config in list:
        if config.name == name:
            have = 1
            break
    if (not have):
        __addconfigs(name)
    return hostfile.getConfit(name)

def sourceContent(name):
    list = __getconfigs()
    have = 0
    for config in list:
        if config.name == name:
            if config.status == str(2):
                print "不能重复生效"
                sys.exit(0)
            have = 1
            break
    if (not have):
        print "没有该配置,请先添加[hh add "+ name +"]"
        sys.exit(0)
    return hostfile.getConfit(name)

def __write(configs):
    fp = open(HOST_PROPERTIES, "w+")
    for config in configs:
        fp.write(config.name + " " + str(config.status) + "\n")
    fp.flush()
    fp.close()

def changeStatus(name, status):
    configs = __getconfigs()
    for config in configs:
        if config.name == name and not config.status == status:
            config.status = status
            break
    __write(configs)