# _*_ coding: utf-8 -*_
# 第七课 buildin function
# you can find the info for buildin function on line. 
# Address:  https://docs.python.org/2/library/functions.html

# Built-in Functions		
# abs()	divmod()	input()	open()	staticmethod()
# all()	enumerate()	int()	ord()	str()
# any()	eval()	isinstance()	pow()	sum()
# basestring()	execfile()	issubclass()	print()	super()
# bin()	file()	iter()	property()	tuple()
# bool()	filter()	len()	range()	type()
# bytearray()	float()	list()	raw_input()	unichr()
# callable()	format()	locals()	reduce()	unicode()
# chr()	frozenset()	long()	reload()	vars()
# classmethod()	getattr()	map()	repr()	xrange()
# cmp()	globals()	max()	reversed()	zip()
# compile()	hasattr()	memoryview()	round()	__import__()
# complex()	hash()	min()	set()	
# delattr()	help()	next()	setattr()	
# dict()	hex()	object()	slice()	
# dir()	id()	oct()	sorted()

#you can user help(xxx) for detail info. eg. help(abs)

print abs(-100)

print cmp(1,2)
print cmp(2,1)

print sum(range(100))

# 类型转换
print int('123456')
print float('12.345')
print str(123456)
print str(12.3456)
print bool(1)


#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
test_abs = abs
print test_abs(-123)

