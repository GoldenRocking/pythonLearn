#!/usr/bin/python
#coding=utf-8

#set/get方法
class Student(object):
	def get_score(self):
		return self._score
	
	def set_score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value
		
s = Student()
s.set_score(60)
print s.get_score()

#使用property 把一个getter方法变成属性
class Grade(object):
	
	@property
	def score(self):
		return self._score
		
	@score.setter
	def score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must betwween 0~100!')
		self._score = value
		
	@property
	def birth(self):
		return self._birth
		
	@birth.setter
	def birth(self,value):
		self._birth = value
		
	@property
	def age(self):
		return 2017 - self._birth			
		
g = Grade()
g.score = 59
print g.score	

#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
#上面的birth是可读写属性，而age就是一个只读属性							
		    		
