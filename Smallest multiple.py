#!/usr/bin/python
# -*- encoding: utf-8 -*-
# 2520 es el número más pequeño que puede ser dividido entre cada uno de los números del 1 al 10 sin quedar ningún resto.
# ¿Cuál es el menor número positivo que es divisible entre todos los números del 1 al 20?
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

def factorPrime(num):
	factores = []

	primes = list(filter(isPrime, range(num + 1)))

	i = 0
	while(i<len(primes)):
		while num >=1:
			if num % primes[i] == 0:
				factores.append(primes[i])
				num =num / primes[i]
			else:
				break
		i = i + 1

	return factores

def comparar(l1,l2,n):
	if l1.count(n) < l2.count(n):
		return l2
	else:
		return l1

def lmc(factores, num, n):
	i = 2
	buf = []
	while i <= num:
		mayor = comparar(buf, factores[i-2], n)
		if mayor == factores[i-2]:
			buf = factores[i-2]
		i = i + 1

	return mayor

def main(num):
	numbers = [i for i in range(2,num+1)]
	factores = []
	facom = []

	for number in numbers:
		factores.append(factorPrime(number))

	print factores

	
	for i in list(filter(isPrime, range(num + 1))):
		facom.append(lmc(factores, num, i))
	
	print facom

	r = 1
	for fac in facom:
		for i in fac:
			r = r * i

	print r

if __name__ == '__main__':
	main(20)