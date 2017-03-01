#!/usr/bin/python
#coding=utf-8

class Student(object):
	pass
	
s = Student()
s.name = 'Michael' #动态给实例绑定一个属性
print s.name	

#还可以尝试给实例绑定一个方法
def set_age(self,age):
	self.age = age
	
from types import MethodType
s.set_age = MethodType(set_age,s,Student) #给实例绑定一个方法
s.set_age(25)
print s.age

#给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
#s2.set_age(25)	

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
	self.score = score
	
Student.set_score = MethodType(set_score,None,Student)

s.set_score(99)
print s.score	

s2.set_score(98)
print s2.score

#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
class Grade(object):
	__slots__ = ('name','age')  # 用tuple定义允许绑定的属性名称
g = Grade()
g.name = 'Tom'
print g.name

g.age = 24
print g.age	

#g.score = 99

#使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
#除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__
