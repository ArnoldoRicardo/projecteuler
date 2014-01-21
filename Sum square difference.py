#!/usr/bin/python
# -*- encoding: utf-8 -*-

# La suma de los cuadrados de los diez primeros números naturales es,
# 
# 12 + 22 + ... + 102 = 385
# El cuadrado de la suma de los diez primeros números naturales es,
# 
# (1 + 2 + ... + 10)2 = 552 = 3025
# Por tanto, la diferencia entre la suma de los cuadrados de los diez primeros números naturales y el cuadrado de la suma de estos es 3025 - 385 = 2640.
# 
# Halla la diferencia entre la suma de los cuadrados de los primeros cien números naturales y el cuadrado de la suma de estos.

num = 100
suma = 0
sumsqrt	= 0

i = 1
while i <=num:
	sumsqrt = sumsqrt + i**2
	suma = suma + i

	i = i +1

print suma**2 - sumsqrt