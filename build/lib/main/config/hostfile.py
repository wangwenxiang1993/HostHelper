#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

PROJECT_ROOT = os.path.abspath(os.path.expanduser('~')+"/.HostHelper")
DEFINITIONS_ROOT = os.path.join(PROJECT_ROOT, 'hostfile')
if not os.path.exists(DEFINITIONS_ROOT):
    os.makedirs(DEFINITIONS_ROOT)



def getConfit(name):
    HOST_FILE = os.path.join(DEFINITIONS_ROOT, name)
    if not os.path.exists(HOST_FILE):
        os.system("touch " + HOST_FILE)
    fp = open(HOST_FILE, 'r+')
    return fp.readlines()

def writeContent(name, content):
    if len(content) > 0:
        HOST_FILE = os.path.join(DEFINITIONS_ROOT, name)
        fp = open(HOST_FILE, "w+")
        for line in content:
            fp.write(line)
        fp.flush()
        fp.close()
