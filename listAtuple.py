#!/usr/bin/python
#coding=utf-8
#list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Tom','Lilei','HanMei']
print classmates

#用len()函数可以获得list元素的个数
print len(classmates)

#用索引来访问list中每一个位置的元素，记得索引是从0开始的
print classmates[0]

tt = classmates[2]
print tt

#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print classmates[-1] 

#以此类推，可以获取倒数第2个、倒数第3个：
print classmates[-2]

#可以往list中追加元素到末尾
classmates.append("Lucy")
print classmates

#也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, "Lily")
print classmates

#要删除list末尾的元素，用pop()方法
classmates.pop()
print classmates

#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(0)
print classmates

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Selina'
print classmates

#list里面的元素的数据类型也可以不同，比如：
List2 = ["Apple",123,True]
print List2

#list元素也可以是另一个list，比如：
List3 = ['python', 'java', ['asp', 'php'], 'scheme']
print List3
print len(List3)

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
tuple1 = ('HanMei',"Jolon","Tom")
print tuple1

#tuple没有append()，insert()这样的方法
#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来

#只有1个元素的tuple定义时必须加一个逗号,
tuple2 = (1,)
print tuple2
print tuple2[0]
print len(tuple2)

# '可变'tuple
t = ('a','b',['A','B'])
print t
t[2][0] = 'X'
t[2][1] = 'Y'
print t