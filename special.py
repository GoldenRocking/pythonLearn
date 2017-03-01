#!/usr/bin/python
#coding=utf-8
from collections import Iterable

#切片
L = ['Michael','Sarah','Tracy','Bob','Jack']

#如何取前3个元素？
print L[0],L[1],L[2]

#取前n个元素呢：
r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)

#使用切片
print L[0:3]

K = L[1:3]
print K	

#python支持倒数切片
print L[-2:]
print L[-2:-1]

L = range(100)
print L
print L[:10]
print L[-10:]
print L[10:20]

#前10个数，每两个取一个：
print L[:10:2]

#所有数，每5个取一个：
print L[::5]

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print (0,1,2,3,4,5)[:3]

#字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]

#迭代
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
#在Python中，迭代是通过for ... in来完成的
#Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上
#dict迭代:
d = {'a':1,'b':2,'c':3}
for key in d:
	print key
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
#dict迭代value:
for value in d.itervalues():
	print value
	
#同时迭代key和value
for k,v in d.iteritems():
	print 'k:',k,'value:',v
	
#通过collections模块的Iterable类型判断	对象是否可以迭代
print isinstance('abc', Iterable)

print isinstance([1,2,3], Iterable)

print isinstance(123, Iterable)

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['A','B','C']):
	print i,value
	
for x,y in [(1,1),(2,4),(3,9)]:
	print x,y
	
#列表生成式
print [x * x for x in range(1, 11)]
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print [x * x for x in range(1, 11) if x % 2 == 0]		

#还可以使用两层循环，可以生成全排列：
print [m + n for m in 'ABC' for n in 'XYZ']

import os
#列出当前目录下的所有文件和目录名，可以通过一行代码实现：
print [d for d in os.listdir('.')]

#列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }

e = [k + '=' + v for k, v in d.iteritems()]
print e

#把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
LS = [s.lower() for s in L]
print LS

#生成器
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
#如果要一个一个打印出来，可以通过generator的next()方法
print g.next()
print g.next()
print g.next()	

#当然，上面这种不断调用next()方法实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
g = (x * x for x in range(10))
for n in g:
	print n
	
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print b
		a,b = b,a+b
		n=n+1
		
fib(6)	

 #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：		
def fib1(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n=n+1