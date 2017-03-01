#!/usr/bin/python
#coding=utf-8
import math

#函数
print(abs(-100))

print(cmp(1, 2))

print(cmp(2,1))

print(cmp(2,2))

print(int('123'))

#函数定义
#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
		
print my_abs(-3)	

#pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
	pass
	
#数据类型检查可以用内置函数isinstance实现	
def my_abs1(x):
	if not isinstance(x, (int,float)):
		raise TypeError('error type')
	if x >= 0:
		return x
	else:
		return -x	
		
#print my_abs1('a')	

#返回多个值
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny
	
x,y = move(100, 100, 60,math.pi/6)	
print x,y

#其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60,math.pi/6)
print r		
#函数可以同时返回多个值，但其实就是一个tuple

#默认参数
#默认参数必须指向不变对象！
def enroll(name,gender,age = 18,city='Beijing'):
	print 'name:',name
	print 'gender:',gender
	print 'age:',age
	print 'city:',city
	
enroll('Bon', 'M')
enroll('Joben', 'F',16,'SHangg')
enroll('Lucy', 'F',18)
enroll('Lily', 'F',city ='SHangg')

#可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
	
print(calc(1,2,3))	

nums = [1,2,3]
print(calc(*nums))	

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def person(name,age,**kw):
	print 'name:',name,'age:',age,'other:',kw
	
person('Tom', 18)	
person('Lucy', 20, city='Beijing')
person('Lucy', 20, city='Beijing',gender='F')

kw = {'city':'Beijing','job':'Engineer'}
person('Jack', 18, city=kw['city'],job=kw['job'])

person('Lilei',24,**kw)

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

def func(a,b,c=0,*args,**kw):
	print 'a =',a,'b =',b,'c =',c,'args =',args,'kw =',kw
	
func(1, 2)

func(1, 2,c=3)

func(1, 2,3,'a','b')

func(1, 2,3,'a','b',x=99)

args = (1,2,3,4)
kw = {'x':99}
func(*args, **kw)

#递归函数
#如果一个函数在内部调用自身本身，这个函数就是递归函数

def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)	
	
print(fact(5))	

	
	