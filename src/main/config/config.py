#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Config(object):
    """1-未启用,2-启用"""
    def __init__(self, name, status):
        self.name = name
        self.status = status