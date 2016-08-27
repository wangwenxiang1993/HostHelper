#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

PROJECT_ROOT = os.path.abspath(os.path.expanduser('~')+"/.HostHelper")
DEFINITIONS_ROOT = os.path.join(PROJECT_ROOT, 'config')
CONFIG_NAME = "editor"
EDIT_PROPERTIES = os.path.join(DEFINITIONS_ROOT, CONFIG_NAME)
if not os.path.exists(DEFINITIONS_ROOT):
    os.makedirs(DEFINITIONS_ROOT)
if not os.path.exists(EDIT_PROPERTIES):
    os.system("touch " + EDIT_PROPERTIES)


def __write(content):
    fp = open(EDIT_PROPERTIES, 'w')
    for line in content:
        fp.write(line)
    fp.flush()
    fp.close()

def __readAndRomove():
    fp = open(EDIT_PROPERTIES, 'r+')
    lines = fp.readlines()
    __write("")
    return lines


def openFile(content):
    if len(content) > 0:
        __write(content)
    if not os.system("vim "+EDIT_PROPERTIES):
        return __readAndRomove()