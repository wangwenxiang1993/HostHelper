#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse

import config.configTools as configTooles
import edit.editTool as editor
import config.hostfile as hostfile

addParser = argparse.ArgumentParser()
addParser.add_argument('name', help='host组名称')

def command(arg):
    args = addParser.parse_args(arg)
    __add(args.name)

def __add(name):
    lines = configTooles.addContent(name) #获取之前的内容
    newLines = editor.openFile(lines) #以之前的内容打开编辑器,并返回修改后的内容
    hostfile.writeContent(name, newLines)
