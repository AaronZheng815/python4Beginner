# _*_ coding: utf-8 -*_
# 第四课，list and tuple

### list
#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
family = ['Aaron','Nina','Cici','Allen']
print family

#用len()函数可以获得list元素的个数
print len(family)

#用索引来访问list中每一个位置的元素，记得索引是从0开始
print family[0]
print family[1]
print family[2]
print family[3]

#取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print family[-1]
print family[-2]
print family[-3]
print family[-4]

#list是一个可变的有序表，所以，可以往list中追加元素到末尾
family.append('piggy')
print family

#把元素插入到指定的位置，比如索引号为1的位置
family.insert(1,'georgy')
print family

#删除list末尾的元素，用pop()方法
family.pop()
print family

#删除指定位置的元素，用pop(i)方法，其中i是索引位置
family.pop(1)
print family

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
family[0] = 'Dad'
print family

#list里面的元素的数据类型也可以不同
listTst = ['Dad',124,True]
print listTst
listTst.append(family)
print listTst
#list中增加了list，相当于二维数组
print listTst[3][0]

### tuple
#另外有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
friend = ('Michael','Bob','Alex')
print friend
#tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
print friend[1]
print friend[-1]

#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
tuple_1 = (1,'Aaron')
print tuple_1

tuple_2 = (1,2,['aaa','bbb'])
print tuple_2
tuple_2[2][0] = 'ccc'
tuple_2[2][1] = 'ddd'
print tuple_2

#list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
