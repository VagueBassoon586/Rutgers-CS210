if __name__ == '__main__':
	import sys
	path = sys.argv[1]
	with open(path, "r") as file:
		count = (" ".join([i.strip() for i in file.readlines()])).count(" ")
	print(count + 1)