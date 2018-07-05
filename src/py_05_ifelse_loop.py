# _*_ coding: utf-8 -*_
# 第五课，if/else and loop

### if 语法
#   if <条件判断1>:
#       <执行1>
#   elif <条件判断2>:
#       <执行2>
#   elif <条件判断3>:
#       <执行3>
#   else:
#       <执行4>

#注意两点： 缩进 和 if/else后面的冒号
age = 3
if age >= 18:
    print 'your age is', age
    print 'adult'
elif age > 6:
    print 'your age is', age
    print 'teenager'
else:
	print 'kid'


### 循环
# 第一种循环  for x in ...
# 把每个元素代入变量x，然后执行缩进块的语句
family = ['Aaron','Nina','Cici','Allen']
for person in family:
	print person

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum

#Python提供一个range()函数，可以生成一个整数序列
print range(5)
sum = 0
for x in range(101):
    sum = sum + x
print sum


# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

