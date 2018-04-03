#!/usr/bin/python
# -*- coding:utf-8 -*-

class Calc():
	
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def __add__(self):
		return self.a + self.b
	
	def __sub__(self):
		return self.a - self.b
	
	def mul(self):
		return self.a * self.b
	
	def div(self):
		if self.b == 0:
			return '除数不能为0'
		return self.a / self.b


if __name__ == '__main__':
	while(True):
		try:
			a = int(raw_input('请输入第一个数字：'))
		except ValueError:
			print '输入的为非数字，请重新输入'
		else:
			print a
			break
	while(True):
		try:
			b = int(raw_input('请输入第二个数字：'))
		except ValueError:
			print '输入的为非数字，请重新输入'
		else:
			print b
			break
	calc = Calc(a, b)
	
	xxx = raw_input('请输入你要做的运算(+,-,*,/):')
	def foo(var, func):
		return {
			'+' : func.__add__(),
			'-' : func.__sub__(),
			'*' : func.mul(),
			'/' : func.div(),
		}.get(var, '输入的运算方式错误')
	print foo(xxx, calc)
