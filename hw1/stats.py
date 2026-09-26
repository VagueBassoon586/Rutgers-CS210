def findMean(n, length):
	return sum(n) / length

def findMedian(n, length):
	if length % 2 == 0:
		return (n[(length // 2) - 1] + n[length // 2]) / 2
	return n[(length - 1) // 2]

def getStandardDeviation(n, length, mean):
	val = 0
	for i in n:
		val += (i - mean) ** 2
	return (val / (length - 1)) ** 0.5


if __name__ == '__main__':
	n = []
	num = int(input())
	while num != -12345:
		n.append(num)
		num = int(input())
	
	length = len(n)
	
	mean = findMean(n, length)
	print(f"mean: {mean}")
	median = findMedian(n, length)
	print(f"mean: {median}")
	standard_deviation = getStandardDeviation(n, length, mean)
	print(f"standard deviation: {standard_deviation}")