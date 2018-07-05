# _*_ coding: utf-8 -*_
# 第二课，数据类型和变量

### 整数，浮点数表示
var_i = 10
var_f = 3.1415926
var_f_1 = 1.23e9  
var_f_2 = 1.23e-5
var_i_hex = 0x1adf

print var_i,var_f,var_f_1,var_f_2,var_i_hex  #十六进制会打印成十进制数

### 字符串
str_1 = 'Aaron'
str_2 = "Nina"
print str_1, str_2

### 布尔值
print True, False
print 3>2
print 3<2

### and or not
print True and True
print True and False
print not True
if 18 < 9:
	print "error happend."
else:
	print "18 < 9, False"

### 空值
#是Python里一个特殊的值，用None表示。None不能理解为0，
#因为0是有意义的，而None是一个特殊的空值。

### 变量
#变量名必须是大小写英文、数字和_的组合，且不能用数字开头
abc = 123
abc = 'aaron zheng'
#在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
#这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错.
a = 'ABC'
#Python解释器干了两件事情：
#	在内存中创建了一个'ABC'的字符串；
#	在内存中创建了一个名为a的变量，并把它指向'ABC'。
b = a
a = 'XYZ'
print a, b

### 常量
#所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
PI = 3.14159265359
#事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。

### 整数除法
print 10/3  #得到整数
print 10.0/3  #得到精确数，需要被除数为浮点型
print 10%3  #取余