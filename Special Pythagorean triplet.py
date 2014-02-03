#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Una terna pitagórica es un conjunto de tres números naturales, a < b < c, para el cual,

# a2 + b2 = c2
# Por ejemplo, 32 + 42 = 9 + 16 = 25 = 52.

# Existe una única terna pitagórica para la cual a + b + c = 1000.
# Halla el producto abc.

for n in range(1,20):
	for m in range(2,21):
		if n<m:
			# print 'm ' + str(m)
			# print 'n ' + str(n)
			a = m*m - n*n
			b = 2 * m * n
			c = m*m + n*n
			# print a
			# print b
			# print c
			if (a + b + c == 1000):
				print a*b*c