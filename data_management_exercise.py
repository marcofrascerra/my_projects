# Ex. 1

data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
		['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
		['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
		['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
		['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
		['D5', 98], ['D6', 32]]


def answer_1(data):

	print(f"1. There are {len(data)} sites")


def answer_2(data):

	print(f"2. There are {data[6][1]} birds in the 7th site")


def answer_3(data):

	print(f"3. There are {data[len(data)-1][1]} birds in the last site")


def answer_4(data):

	total_birds = 0

	for i in data:

		total_birds += i[1]

	return total_birds


def answer_5(data):

	birds = answer_4(data)

	average_birds = birds / len(data)

	print(f"5. There are {round(average_birds)} birds in average")


def answer_6(data):

	birds = 0

	for i in data:
		if i[0][0] == 'C':
			birds += i[1]

	print(f"6 .There are {birds} birds in the 'C' sites")


answer_1(data)
answer_2(data)
answer_3(data)
print(f"4. There are {answer_4(data)} birds in all sites")
answer_5(data)
answer_6(data)
