#!/usr/bin/python
#coding=utf-8




#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

def log(func):
	def wrapper(*args,**kw):
		print 'call %s():' % func.__name__
		return func(*args,**kw)
	return wrapper	

#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
	
@log
def now():
	print '2016-10-11'

now()	
f = now
f()	

#函数对象有一个__name__属性，可以拿到函数的名字：
# print now.__name__

#print f.__name__
	
