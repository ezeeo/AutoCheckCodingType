# 编码类型判断
## 使用
    相应目录添加进sys.path后  
    from AutoCheckCodingType import CodingTypeDetector
    即可
    然后创建检测器对象
    de=CodingTypeDetector(report_type='html')
    可设置的参数:
    path='检测引擎所在目录'，可不写，默认为CheckEngines
    report_type=('console','html','other')设置报告模式，可不写，默认为console
    html即为生成html文件，console即为直接输出
    默认为console

    然后调用Detector(data)方法即可
    
## 注意
    如果检测引擎的输出模式为console，则结果不会出现在最终报告内

## 开发说明
    建议检测引擎使用自带的_MetaEng作为元类
    否则的话必须拥有set_data(self,data)方法  

* 必须重写的方法  

    check(self)
    此方法的返回方式由文件开始的注释定义  
    #output 输出方式(normal|file|console)

说明:

    normal:(概率,运行过程的说明,解码后的结果)
    概率范围为0-1，其他两项为字符串，最后返回三元组
    file:需要返回文件路径标准格式为(第一行0-1,后面的#开头为描述,否则为结果)
    console:输到控制台,返回None即可

* 类的注意  
如果文件内有多个类的话  
文件内第一个出现的类必须是要直接使用的类

* 开始部分注释的必写项  
#name 检测引擎名称(必须与第一个出现的类名相同)  
#version 版本  
#output 输出方式  
#describe 描述,可以多行  

示例:
```
#encoding=utf-8
#name MetaEngine
#version 1.0
#output normal
#describe 元类
```
