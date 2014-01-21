#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Haciendo una lista de los seis primeros números primos obtenemos: 2, 3, 5, 7, 11 y 13, podemos ver que el sexto primo es 13.
# ¿Cuál es el 10.001er número primo?
import math

def isPrime(num):
	sqrnum = int(math.sqrt(num))
	if (num < 2):
  		return False

  	i=2
  	while(i<=sqrnum):
	    if ((num%i) == 0):
	    	return False
	    i = i + 1

	return True

j = 0
i = 2
while j < 10001:
	if isPrime(i):
		numero = i
		j = j + 1
	i = i + 1

print j
print numero