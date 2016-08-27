#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

HOSTS_PATH = "/etc/hosts"

def getLines():
    fp = open(HOSTS_PATH, "r+")
    lines = fp.readlines()
    fp.close()
    print lines

def addHost(name, hostList):
    if len(hostList) > 0:
        fp = open(HOSTS_PATH, "a")
        fp.write("###" + name + "###\n")
        for line in hostList:
            fp.write(line)
        fp.write("###" + name + "###")
        fp.flush()
        fp.close()
        return 1
    return 0