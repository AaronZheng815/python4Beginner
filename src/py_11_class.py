#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a class test module '

__author__ = 'Aaron Zheng'

import sys

class Student(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def print_age(self):
		print '%s %s years old' %(self.name, self.age)

aaron = Student("Aaron Zheng",12)
aaron.print_age()

#Python中，实例的变量名如果以__开头，
#就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student1(object):
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
	def print_age(self):
		print '%s %s years old' %(self.__name, self.__age)

nina = Student1("Nina",12)
nina.__name  = 'test'
nina.__age = 13
print nina.__name