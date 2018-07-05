# _*_ coding: utf-8 -*_
# 第八课 function

### 1 函数的定义 ###
#	def func(x):
#		...
#		return

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print my_abs(-100)

#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None

### 2 空函数 ###
# 如果想定义一个什么事也不做的空函数，可以用pass语句
def func_todo():
	pass
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
#就可以先放一个pass，让代码能运行起来。
#pass还可以用在其他语句里，比如：
#	if age >= 18:
#	    pass
#缺少了pass，代码运行就会有语法错误。

### 3 参数检查 ###
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
def my_abs_new(x):
	if not isinstance(x, (int,float)):
		raise TypeError('bad operand type')

	if x >= 0:
		return x
	else:
		return -x

#my_abs_new('aaa')

### 4 返回多个值 ###
def func_1(x):
	a = x;
	b = x+1;
	return a,b

r1,r2 = func_1(100)
print r1,r2

rt = func_1(200)
print rt
#原来返回值是一个tuple！但是，在语法上，
#返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便

### 5 默认参数 ###
#默认参数必须指向不变对象！避免掉到坑里
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5)
print power(5,3)
#从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错；
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

#当有多个默认参数时，如果只希望给出某一个默认参数，其它使用默认值，可以指定默认参数赋值  func(1,2,a = 3), 这里a 是某一个默认参数名

### 6 可变参数 ###
#可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
def calculate(*number):
	sum = 0
	for n in number:
		sum += n
	return sum

print calculate(1,2,3,4,5)

#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
num_lst = [1,2,3,4,5,6,7,8]
print calculate(*num_lst)

### 7 关键字参数 ###
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
	print 'name : ', name, ', age : ', age
	print 'other:'
	print kw

person('Aaron', 24)
person('Aaron', 24, address='shenzhen')

kwPara = {'address':'shenzhen', 'score':100}
person('Aaron',24,**kwPara)

### 8 参数组合 ###
#在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，
#或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
def func_comb(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func_comb(1,2)
func_comb(1,2,3)
func_comb(1,2,3,'a','b')
func_comb(1,2,3,'a','b',x=99)

args = (1, 2, 3, 4)
kw = {'x': 99}
func_comb(*args, **kw)
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
