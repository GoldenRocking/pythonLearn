#!/usr/bin/python
#coding=utf-8

import os
print os.name
print os.uname()

#在操作系统中定义的环境变量，全部保存在os.environ这个dict中，可以直接查看
#print os.environ

#要获取某个环境变量的值，可以调用os.getenv()函数：
#print os.getenv('PATH')

# 查看当前目录的绝对路径:
print os.path.abspath('.')	

# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。	
print os.path.join('/Users/guoruiqing/skill/serverlet/python/basic', 'testdir')
# 然后创建一个目录:
os.mkdir('/Users/guoruiqing/skill/serverlet/python/basic/testdir')
# 删掉一个目录:
os.rmdir('/Users/guoruiqing/skill/serverlet/python/basic/testdir')	

#os.path.split()函数，可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
#os.path.splitext()可以直接让你得到文件扩展名
