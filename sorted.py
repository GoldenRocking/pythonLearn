#!/usr/bin/python
#coding=utf-8

#Python内置的sorted()函数就可以对list进行排序
print sorted([36,5,12,9,21])

#sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序
#如果要倒序排序，我们就可以自定义一个reversed_cmp函数：
def reversed_cmp(x,y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0
	
print sorted([36,5,12,9,21],reversed_cmp)

print sorted(['bob','about','Zoo','Credit'])	
#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。		
#忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较
def cmp_ignore_case(s1,s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	return 0
	
print sorted(['bob','about','Zoo','Credit'],cmp_ignore_case)			
