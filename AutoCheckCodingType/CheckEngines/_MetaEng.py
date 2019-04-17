#encoding=utf-8
#name MetaEngine
#version 1.0
#output normal
#describe 元类

from abc import ABC,abstractmethod
class MetaEngine(ABC):
    '''元类'''
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

    def check_in_txttable(self,ex_allow=None,desc=True):
        '''检查data里的数据是不是都在txttable里'''
        try:
            tmp=self.txttable
            if ex_allow:
                if isinstance(tmp,list):
                    if isinstance(ex_allow,list):
                        tmp+=ex_allow
                    elif isinstance(ex_allow,str):
                        tmp+=[e for e in ex_allow]
                    else:
                        pass
                elif isinstance(tmp,str):
                    if isinstance(ex_allow,list):
                        tmp+=''.join(ex_allow)
                    elif isinstance(ex_allow,str):
                        tmp+=ex_allow
                    else:
                        pass
                else:
                    pass
                
        except :
            return False
        if not tmp:
            return False
        for d in self.data:
            if d not in tmp:
                if desc==True:self.describe+=d+' is not allow'
                return False
        return True

def auto_return(func):
    def wrapper(me_instance):
        func(me_instance)
        if isinstance(me_instance.possibility,float):me_instance.possibility=round(me_instance.possibility,2)
        if me_instance.possibility>1:me_instance.possibility=1
        return (0 if me_instance.possibility<0 else me_instance.possibility,me_instance.describe,me_instance.result)
    return wrapper