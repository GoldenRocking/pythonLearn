#!/usr/bin/python
#coding=utf-8

d = {'Tom':95,'Bob':75,'Trace':85}
print(d['Tom'])
d['Lucy'] = 80
print 'Lucy:',d['Lucy']

#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['Tom'] = 100
print 'Tom:',d['Tom']

#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
if 'Lili' in d:
	print 'In'
else: 
    print 'Out'	

#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Lily'))
print(d.get('Lily',-1))

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d)
d.pop('Tom')
print(d)

#dict内部存放的顺序和key放入的顺序是没有关系的
#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而增加；
#需要占用大量的内存，内存浪费多。

#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。

#set
s = set([1,2,3])
print s
#注意，传入的参数[1, 2, 3]是一个list，而显示的set([1, 2, 3])只是告诉你这个set内部有1，2，3这3个元素，显示的[]不表示这是一个list

#重复元素在set中自动被过滤：
s = set([1,1,1,2,4,5,2,3,6,3,])
print(s)

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
s.add(7)
s.add(7)
print s
#通过remove(key)方法可以删除元素：
s.remove(4)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1 & s2)

print s1 | s2