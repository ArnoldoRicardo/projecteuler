#!/usr/bin/python
# -*- encoding: utf-8 -*-
# La suma de los números primos por debajo de 10 es 2 + 3 + 5 + 7 = 17.
# Halla la suma de todos los primos por debajo de dos millones.

import math

def isPrime(num):
	# num = int(num**(0.5) + 1)
	sqrnum = int(math.sqrt(num))
	if (num < 2):
  		return False

  	i=2
  	while(i<=sqrnum):
  	# for i in range(2,num):
	    if ((num%i) == 0):
	    	# print "si"
	    	return False
	    # print i
	    i = i + 1
	# print "hola"

	return True

def main():
	r = 0
	i=1
	n=2000000
	while(i<=n):
		if isPrime(i):
			r += i
		i=i+1
	print r

if __name__ == '__main__':
	main()