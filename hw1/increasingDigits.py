def isIncreasing(n):
	lst = []
	while n > 0:
		end = n % 10
		lst.append(end)
		n //= 10
	for i in range(1, len(lst)):
		if lst[i] > lst[i - 1] or lst[i] == lst[i - 1]:
			return False
	return True


if __name__ == '__main__':
	import sys
	n = int(sys.argv[1])
	count = 0
	for i in range(1, n + 1):
		if isIncreasing(i):
			count += 1
	print(count)