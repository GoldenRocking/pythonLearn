#!/usr/bin/python
#coding=utf-8

#继承
class Animal(object):
	def run(self):
		print 'Animal is running...'
		

class Dog(Animal):
	def run(self):
		print 'Dog is running...'
	
class Cat(Animal):
	def run(self):
		print 'Cat is running...'	
		
#当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。		
dog = Dog()
dog.run()

cat = Cat()
cat.run()

#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类
print isinstance(cat, Cat)

print isinstance(cat, Animal)
