def maxCalroieCounting(input) -> int:
	values = []
	with open("input.txt") as file:
		for line in file:
			if line == "\n":
				values.append(0)
				continue
			if not values:
				values.append(int(line))
				continue
			values[len(values)-1]+= int(line)
	return max(values)

print(maxCalroieCounting("input.txt"))
