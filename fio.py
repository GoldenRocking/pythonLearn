#!/usr/bin/python
#coding=utf-8

f = open('/Users/guoruiqing/Downloads/2017-02-28.txt','r')
print f.read()
f.close()

with open('/Users/guoruiqing/Downloads/2017-02-28.txt','r') as f:
	print f.read()

#调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
f = open('/Library/WebServer/Documents/mainwork/storestatic/html/images/aboutus/1.jpg','rb')
print f.read(1000)

#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
f = open('/Users/guoruiqing/Downloads/2017-02-28.txt','w')
f.write("I love u")
f.close()
