if __name__ == '__main__':
	with open("roster1.dat", "r") as file:
		rosterData = [i.strip() for i in file.readlines()]

	summary = {}
	for i in rosterData:
		name, major, gpa, credits = i.split(",")
		if major not in summary:
			summary[major] = [float(gpa), float(credits), 1]
		else:
			summary[major][0] += float(gpa)
			summary[major][1] += float(credits)
			summary[major][2] += 1

	for major in summary.keys():
		avgGPA = summary[major][0] / summary[major][2]
		avgCredits = summary[major][1] / summary[major][2]
		print(f"{major},{avgGPA},{avgCredits},{summary[major][2]}")
