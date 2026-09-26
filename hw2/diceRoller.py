if __name__ == '__main__':
	import sys
	from random import randint
	n = int(sys.argv[1])
	average = 0
	for _ in range(n):
		count = 0
		dice1 = 0
		dice2 = 0
		while dice1 + dice2 != 7:
			dice1 = randint(1, 6)
			dice2 = randint(1, 6)
			count += 1
		average += count / n
	print(average)