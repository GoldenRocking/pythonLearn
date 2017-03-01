#!/usr/bin/python
#coding=utf-8

#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
#Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

#变量可以指向函数

print abs(-10)

x = abs(-10)
print x

f = abs
print f(-10)

#传入函数
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

def add(x,y,f):
	return f(x) + f(y)
	
print add(-5, 6, abs)	