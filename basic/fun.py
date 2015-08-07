#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import math

def my_abs(x):
	if not isinstance(x, (int,float)):
		raise(TypeError('bad operand type'))
	if x >= 0:
		return x
	else:
		return -x

def quadratic(a,b,c):
	x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
	x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
	return x1, x2

n = my_abs(-20)
print(n)

x,y = quadratic(1, 2, 1)
print(x, y)