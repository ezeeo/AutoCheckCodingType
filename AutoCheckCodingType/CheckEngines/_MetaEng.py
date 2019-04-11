#encoding=utf-8
#name MetaEngine
#version 1.0
#output normal
#describe 元类

from abc import ABC,abstractmethod
class MetaEngine(ABC):
    '''元类,请在内部捕获所有异常'''
    def __init__(self,data=''):
        assert isinstance(data,str)
        self.data=data
        self.possibility=0#是此编码的可能性0-1
        self.describe=''#随意
        self.result=''#解码后的数据


    def set_data(self,data):
        assert isinstance(data,str)
        self.__clear()
        self.data=data

    @abstractmethod#虚函数
    def check(self):
        if isinstance(self.possibility,float):self.possibility=round(self.possibility,2)
        return (self.possibility,self.describe,self.result)

    def __clear(self):
        self.possibility=0#是此编码的可能性0-1
        self.describe=''#随意
        self.result=''#解码后的数据