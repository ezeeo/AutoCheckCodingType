#encoding=utf-8
#name TestEngine
#version 1.0
#output normal
#describe 测试


from _MetaEng import MetaEngine

class TestEngine(MetaEngine):
    '''测试类,请在内部捕获所有异常'''
    def __init__(self,data=''):
        assert isinstance(data,str)
        self.data=data
    
    def set_data(self,data):
        assert isinstance(data,str)
        self.data=data

    def check(self):
        return (1,self.data,self.data)
