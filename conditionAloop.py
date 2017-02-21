#!/usr/bin/python
#coding=utf-8

#条件判断和循环

age = 20
if age >= 18:
	print 'your age is:',age
	print 'adult'
else:
	print 'your age is:',age
	print 'teenager'

# elif是else if的缩写	
age = 3
if age >= 18:
	print 'adult'
elif age >= 6:
	print 'teenager'
else:
	print 'kid'	

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False	
x = 1
if x:
	print 'True'
	
#for...in循环
names = ['Michael','Bob','Tracy']
for name in names:
	print 'name:',name
	
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print 'sum:',sum

#range(101)就可以生成0-100的整数序列
sum = 0
for x in range(101):
	sum = sum + x
print 'sum:',sum

#while循环
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print 'sum:',sum

#从raw_input()读取的内容永远以字符串的形式返回，把字符串和整数比较就不会得到期待的结果，必须先用int()把字符串转换为我们想要的整型
birth = int(raw_input('birth:'))
if birth < 2000:
	print('00前')
else:
	print '00后'	
		
					
		
