#!/usr/bin/python
#coding=utf-8

#函数作为返回值
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
	
f = lazy_sum(1,3,5,7,9)
print f
print f()			
