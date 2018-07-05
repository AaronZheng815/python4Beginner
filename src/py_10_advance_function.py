# _*_ coding: utf-8 -*_
# 第十课 advance function

### map 函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回

def fun(x):
    return x * x

res = map(fun, range(10))
print list(res)


res = list(map(str, range(10)))
print res

### reduce 函数
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
#reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce

def add(x,y):
    return x + y

res = reduce(add, range(10))
print res

#如果要把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x*10 + y
print reduce(fn, [1,3,5,7,9])

#实现 string 转 int的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    
    return reduce(fn,map(char2num,s))

print str2int("123456")

# using lambda
def char2num(s):
    return DIGITS[s]
def str2int_1(s):
    return reduce(lambda x,y:x*10+y, map(char2num,s))

print str2int_1("123456")

