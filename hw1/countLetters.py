if __name__ == '__main__':
	string = str(input())
	string.lower()
	counter = [0] * 26
	for i in string:
		if i.isalpha():
			counter[ord(i) - 97] += 1
	Val_Ind_list = []
	for i in range(len(counter)):
		if counter[i] != 0:
			Val_Ind_list.append((counter[i], i))
	Val_Ind_list.sort(reverse = True)
	for i in range(len(Val_Ind_list)):
		print(f"'{chr(Val_Ind_list[i][1] + 97)}': {Val_Ind_list[i][0]}")
