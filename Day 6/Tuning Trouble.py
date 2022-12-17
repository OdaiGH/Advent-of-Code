def finalScore_1(input) -> int:
    marker = 0
    with open(input) as file:
        string = file.readline()
        for i in range(len(string)):
            sequence = string[i:i+4]
            if len(set(sequence)) != len(sequence):
                continue
            marker = i+4
            break
    return marker


def finalScore_2(input) -> int:
    marker = 0
    with open(input) as file:
        string = file.readline()
        for i in range(len(string)):
            sequence = string[i:i+14]
            if len(set(sequence)) != len(sequence):
                continue
            marker = i+14
            break
    return marker
                

print(finalScore_1("input.txt"))
print(finalScore_2("input.txt"))
