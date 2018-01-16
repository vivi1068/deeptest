# -*- coding:utf-8 -*-
__author__ = 'nancy'

import sys

if __name__ == "__main__":

    #arg
    print("command line number: %d" % len(sys.argv))
    print("command line list:%s" % str(sys.argv))

# terminal execute cmd
# python cmd_arg.py 1 2 t