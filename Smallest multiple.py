# 2520 es el número más pequeño que puede ser dividido entre cada uno de los números del 1 al 10 sin quedar ningún resto.
# ¿Cuál es el menor número positivo que es divisible entre todos los números del 1 al 20?

import factor_prime

def main():
	numeros = list(range(0,21))
	primes = tuple(range(0,21))
	print numeros
	print primes

if __name__ == '__main__':
	main()