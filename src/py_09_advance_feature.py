# _*_ coding: utf-8 -*_
# 第九课 advance feature

### 1 切片 ###
list_1 = ['a','b','c','d','e']
print list_1[0:3]
print list_1[1:2]
#如果第一个索引是0，还可以省略
print list_1[:5]
print list_1[-2:]

list_2 = range(100)
print list_2[:10]
print list_2[-10:]
print list_2[10:20]
print list_2[:10:2]  #前10个数，每两个取一个
print list_2[::5]    #所有数，每5个取一个

#tuple也是一种list，唯一区别是tuple不可变。
#因此，tuple也可以用切片操作，只是操作的结果仍是tuple
tuple_1 = (1,2,3,4,5,6,7,8,9)
print tuple_1
print tuple_1[:3]

#字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。
#因此，字符串也可以用切片操作，只是操作结果仍是字符串
string_1 = "AaronZheng"
print string_1[:5]
#针对字符串提供了很多各种截取函数，其实目的就是对字符串切片。
#Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。

### 2 迭代 ###
#在Python中，迭代是通过for ... in来完成的
list_3 = ['aaron','nina','cici','allen']
for people in list_3:
	print people

dict_1 = {'a':1, 'b':2, 'c':3, 'd':4}
for key in dict_1:                      #默认 key
	print key
for value in dict_1.itervalues():       #values
	print value
for key,value in dict_1.iteritems():    #key & values
	print key,':',value,

#由于字符串也是可迭代对象，因此，也可以作用于for循环
for ch in string_1:
	print ch

#如何判断一个对象是可迭代对象呢？
#方法是通过collections模块的Iterable类型判断
from collections import Iterable
print isinstance('abcd', Iterable)
print isinstance(123, Iterable)

#for循环里，同时引用了两个变量，在Python里是很常见的
for x,y in [(1,1),(2,2),(3,3)]:
	print x,y

#Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
	print i,value

### 3 列表生成式 ###
# 即List Comprehensions，
# 是Python内置的非常简单却强大的可以用来创建list的生成式

print range(1,5)
list_3 = []
for x in range(1,11):
	list_3.append(x*x)
print list_3

#一行来生成
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print [x*x  for x in range(1,11)]
#带上if判断
print [x*x for x in range(1,11) if x % 2 ==0]  
#两次循环
print [m+n  for m in 'ABC' for n in 'XYZ']

#列出当前所有文件和文件夹
import os
cdir = [d for d in os.listdir('.')]
for name in cdir:
	print name

#key-value
print [k + '=' + str(v) for k,v in dict_1.iteritems()]

list_4 = ['Hello','World','Aaron','Zheng']
print [s.lower() for s in list_4]


### 4 生成器 ###
#在Python中，这种一边循环一边计算的机制，称为生成器（Generator）
#创建一个generator，有很多种方法。
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
#generator保存的是算法，每次调用next()，就计算出下一个元素的值，直到计算到最后一个元素，
#没有更多的元素时，抛出StopIteration的错误。
gen = (x * x for x in range(10))
for n in gen:
	print n

#定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for n  in fib(6):
	print n

#generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator
