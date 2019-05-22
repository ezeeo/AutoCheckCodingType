#encoding=utf-8
#name JSFuckCodeEng
#version 1.0
#output normal
#describe 检测是不是JSFuck,JSFuck可以让你只用6个字符[ ]( ) ! +来编写 JavaScript 程序


from _MetaEng import MetaEngine,auto_return
import sys


class JSFuckCodeEng(MetaEngine):
    def __init__(self, data = ''):
        super().__init__(data)
        self.txttable='[]()!+'
    
    @auto_return
    def check(self):
        if not self.check_in_txttable(ex_allow=' '):
            pass
        else:
            pass
