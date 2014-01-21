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
	i=1
	n=int(math.sqrt(600851475143))
	while(i<=n):
		if (600851475143%i ==0):
			if isPrime(i):
				print i
		i=i+1

if __name__ == '__main__':
	main()