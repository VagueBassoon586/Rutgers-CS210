def findZeroTriples(n):
	length = len(n)
	triples = []
	for i in range(length):
		for j in range(i + 1, length):
			for k in range(j + 1, length):
				if n[i] + n[j] + n[k] == 0:
					triples.append((n[i], n[j], n[k]))
	return triples


if __name__ == '__main__':
	n = []
	hasNeg = False
	hasPos = False
	num = int(input())
	while num != -12345:
		n.append(num)
		if num > 0:
			hasPos = True
		elif num < 0:
			hasNeg = True
		num = int(input())
	if not (hasNeg and hasPos):
		print("0 triples found")
	else:
		res = findZeroTriples(n)
		if len(res) != 0:
			print(f"{len(res)} triples found: ")
			for i in res:
				print(f"{i[0]}, {i[1]}, {i[2]}")
		else:
			print("0 triples found")
