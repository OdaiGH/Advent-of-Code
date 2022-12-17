def maxCalroieCounting(input) -> int:
	values = []
	with open(input) as file:
		for line in file:
			if line == "\n":
				values.append(0)
				continue
			if not values:
				values.append(int(line))
				continue
			values[len(values)-1]+= int(line)
	return max(values)

def maxCalroieCounting_2(input) -> int:
	values = []
	sum = 0 
	with open(input) as file:
		for line in file:
			if line == "\n":
				values.append(0)
				continue
			if not values:
				values.append(int(line))
				continue
			values[len(values)-1]+= int(line)
	values = sorted(values)
	return values[-1]+values[-2]+values[-3]

print(maxCalroieCounting("input.txt"))
print(maxCalroieCounting_2("input.txt"))
