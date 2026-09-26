def isPrime(n):
	if n == 1:
		return False
	elif n == 2 or n == 3 or n == 5:
		return True
	elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
		return False
	for i in range(5, int((n ** 0.5) + 1), 6):
		if n % i == 0 or n % (i + 2) == 0:
			return False
	return True

def getPrimeFactor(n):
	while n % 2 == 0:
		n /= 2
		print(2, end = " ")
	for i in range(3, int(n ** 0.5) + 1, 2):
		while n % i == 0:
			n /= i
			print(i, end = " ")
	if n > 2:
		print(int(n))


if __name__ == '__main__':
	import sys
	n = int(sys.argv[1])
	if isPrime(n):
		print(n)
	else:
		getPrimeFactor(n)