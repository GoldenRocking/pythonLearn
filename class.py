#!/usr/bin/python
#coding=utf-8

#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
		
	def print_score(self):
		print '%s: %s' % (self.__name,self.__score)
		
	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
	def get_name(self):
		return self.__name					
		
bart = Student("Tom", 21)
bart.print_score()
print bart.get_grade()	
print bart.get_name()

#我们来判断对象类型，使用type()函数：
print type(bart)

#基本类型都可以用type()判断
print type(123)
print type('123')

import types

print type('abc') == types.StringType

#如果要获得一个对象的所有属性和方法，可以使用dir()函数
print dir(bart)

#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
print hasattr(bart, 'score')

#如果试图获取不存在的属性，会抛出AttributeError的错误
#print getattr(bart, 'score')
#可以传入一个default参数，如果属性不存在，就返回默认值：
print getattr(bart, 'score',404)
		
		
	

