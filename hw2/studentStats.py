if __name__ == '__main__':
	import numpy as np
	with open("roster2.dat", "r") as file:
		rosterData = [i.strip() for i in file.readlines()]
		
	data = np.array([], dtype = {'names': ('name', 'age', 'major', 'gpa'),'formats': ('U50', 'i4', 'U4', 'f8')})
	for i in rosterData:
		name, age, major, gpa = i.split(",")
		data = np.append(data, np.array([(name, int(age), major, float(gpa))], dtype = data.dtype))
	print(np.mean(data['gpa']))
	print(np.max(data[data['major'] == 'CS']['gpa']))
	print(np.size(data[data['gpa'] > 3.5]['gpa']))
	print(np.mean(data[data['age'] >= 25]['gpa']))
	filtered = data[data['age'] <= 22]
	averageGPA = {}
	for major in set(filtered['major']):
		averageGPA[str(major)] = float(np.mean(filtered[filtered['major'] == major]['gpa']))
	highest = max(averageGPA.values())
	for major in averageGPA.keys():
		if averageGPA[major] == highest:
			print(major)
