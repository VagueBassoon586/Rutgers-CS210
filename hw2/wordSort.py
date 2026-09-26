if __name__ == '__main__':
	import sys
	path = sys.argv[1]
	with open(path, "r") as file:
		words = (" ".join([i.strip() for i in file.readlines()])).split(" ")
	
	caseInsensitiveWords = sorted([(word.lower(), index) for index, word in enumerate(words)])
	for i in caseInsensitiveWords:
		print(words[i[1]], end = "\n")