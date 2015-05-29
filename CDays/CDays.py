__author__ = 'mpb'
# -*- coding: utf-8 -*-

import sys
import cmd

class CDays(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)


    def help_test(self):
        print('这是帮助，应该出来不？')

    def do_test(self,arg):
        arg = sys.argv
        print arg

if __name__ == '__main__':
    cdc = CDays()
    cdc.cmdloop()