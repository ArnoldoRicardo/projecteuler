def isPal(i):
	a=str(i)
	al=a[::-1]
	alr=int(al)
	if alr == i:
		return True
	return False

buf1 = 0
buf2 = 0

for i in range(100, 1000):
	for j in range(100, 1000):
		mul = i * j
		if isPal(mul):
			if buf2 > buf1:
				mayor = buf2
			else:
				mayor = buf1
			buf1 = buf2
			buf2 = mul

print mayor
