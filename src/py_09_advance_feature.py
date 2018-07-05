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
