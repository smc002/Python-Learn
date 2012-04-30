#!/usr/bin/python
# Filename: func_param.py

def printMax(a, b):
	if a > b:
		print(a, 'is maximun')
	elif a == b:
		print(a, 'is maximun')
	else:
		print(b, 'is maximun')

printMax(3, 5)

x = 5

y = 7

printMax(x, y)
