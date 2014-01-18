import math

def isPrime(num):
	# num = int(math.sqrt(num))
	if (num < 2):
  		return False

  	i=2
  	for i in range(2,num):
	    if ((num%i) == 0):
	    	return False

	return True

i=1
r=0
n=int(math.sqrt(600851475143))
while(i<=n):
	if (600851475143%i ==0):
		if isPrime(i):
			print i
	i=i+1