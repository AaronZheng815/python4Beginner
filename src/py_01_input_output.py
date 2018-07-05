# _*_ coding: utf-8 -*_
# 第一课，python的基础 输入输出

### 1 基本输出
print 'hello world!'  #用单引号
print "hello world!"  #用双引号，必须配对

#打印多个字符串，用逗号分割，python打印时，替换成空格
print "Aaron","Nina", "Cici", "Allen" 

print '100 + 200 = ', 100+200

### 2 基本输入
# 通过raw_input()
print "Please input your name: "
name = raw_input()
print "Hello, ", name

#或者直接输入提示参数，更加优雅
name = raw_input("Please input your name again:")
print "Hello again,", name

### 3 字符串打印
#字符串打印中，如果包含' ，外面可以通过""括起来打印
print "I am' Aaron Zheng."
print 'I am\' Aaron Zheng.' #或者转义符 \
print 'Hello\nAaron\tZheng'  #\n \t 等转义符
print r'\n' #r'' 内部的字符不转义

#多行打印，例如输出代码等
print '''line1
line2
line3'''
#还可以加上r输出代码段
print r'''
#include "stdio.h"
int main()
{
	printf("Hello World!\n");
	return 0
}'''
