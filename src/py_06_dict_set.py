# _*_ coding: utf-8 -*_
# 第六课  dict and set

###  字典dict
# dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度

# 定义
dict_1 = {'Aaron':1,'Nina':2}
print dict_1

#索引查询
print dict_1['Aaron']

# 赋值
#一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
dict_1['Aaron'] = 3
print dict_1

# 判断key是否存在，有两种方法，
# 一是通过in判断key是否存在， 返回True/False。
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print 'Aaron' in dict_1
print 'Cici' in dict_1
print dict_1.get('Aaron')
print dict_1.get('Cici')
print dict_1.get('Cici', -1)  #自定义输出

# 删除
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
dict_1.pop('Aaron')
print dict_1

# 增加
dict_1['Aaron'] = 5
print dict_1

#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的
#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而增加；
#需要占用大量的内存，内存浪费多，

#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。

#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，
# 需要牢记的第一条就是dict的key必须是不可变对象

### set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

#创建一个set，需要提供一个list作为输入集合
set_1 = set([1,1,2,3,4,5,6,6])
print set_1

#add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
set_1.add(7)
print set_1

#remove(key)方法可以删除元素
set_1.remove(7)
print set_1

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2

#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
#因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
