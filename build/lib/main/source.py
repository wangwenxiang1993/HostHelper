#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse

import config.configTools as configTooles
import host.hostTool as hostTool

addParser = argparse.ArgumentParser()
addParser.add_argument('name', help='host组名称')

def command(arg):
    args = addParser.parse_args(arg)
    __source(args.name)

def __source(name):
    lines = configTooles.sourceContent(name)  # 获取之前的内容
    if hostTool.addHost(name, lines):
        configTooles.changeStatus(name, 2)
