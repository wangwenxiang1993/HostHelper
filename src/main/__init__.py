#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys, os
import main.source as source
import main.add as add

def main(args=None):
    if args is None:
        args = sys.argv
        if len(args) < 2:
            print 'help info'
            sys.exit(0)

        if os.geteuid():
            sudo = "sudo"
            for command in args:
                sudo += " " + command
            os.system(sudo)
            sys.exit(0)

        val = args[1]
        if val == 'add':
            add.command(args[2:])
        if val == 'source':
            source.command(args[2:])


if __name__ == "__main__":
    main()