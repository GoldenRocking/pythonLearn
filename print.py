#!/usr/bin/python
#coding=utf-8
#输出
#用print加上字符串，就可以向屏幕上输出指定的文字
print 'hello,world'

#print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出：
print 'The quick brown fox','jumps over','the lazy dog'

#print会依次打印每个字符串，遇到逗号“,”会输出一个空格

#print也可以打印整数，或者计算结果：
print 300
print 100 + 300
print '100 + 300 =',100 + 300

#Python提供了一个raw_input，可以让用户输入字符串，并存放到一个变量里。
name = raw_input('name: ')
print(name)

print 'hello,', name

# 字符转义
print "i'm ok"
print 'i\'m ok'
print '\\'
print "I'm \n ok"

#布尔类型
print 3 > 2
print 3 > 5

print True and False

print 3 > 2 or 3 > 5

print not 3 > 4

if 3 > 5:
   print 'Hello'
else:
	print 'World'
	
#格式化输出
print 'Hello,%s' % 'world'	
print 'Hi,%s,you have $%d.' % ('Tom',100)

print'%05d' % 3
print '%.2f' % 3.1415926

print 'growth rate: %d %%' % 7


	