#!/usr/bin/bash
# -*- coding:utf-8 -*-

import random

class MySort():
	
	def __init__(self, start, end, count):
		data = []
		for i in range(0, count):
			data.append(random.randint(start, end))
		self.data = data
		self.__mysort__()
		data = self.data

	def __mysort__(self):
		for i in range(0, len(self.data)):
			for j in range(1, len(self.data) - i):
				if self.data[j - 1] > self.data[j]:
					self.data[j - 1], self.data[j] = self.data[j], self.data[j - 1]
				j += 1
			i += 1 

if __name__ == '__main__':
	sort_data = MySort(10, 1000, 100).data
	print sort_data
