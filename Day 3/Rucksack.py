def finalScore_1(input) -> int:
    sum = 0
    with open(input) as file:
        for line in file:
            s1 = set(line[:int(len((line.strip())) / 2)])
            s2 = set(line[int(len((line.strip())) / 2):])
            commonLetters = list(s1&s2)
            for letter in commonLetters:
                if letter.isupper():
                    sum += ord(letter) - 38
                else:
                    sum += ord(letter) - 96
        return sum


def finalScore_2(input) -> int:
    sum = 0
    with open(input) as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    for line in range(0,len(lines),3):
        s1 = set(lines[line])
        s2 = set(lines[line+1])
        s3 = set(lines[line+2])
        commonLetters = list(s1&s2&s3)
        for letter in commonLetters:
                if letter.isupper():
                    sum += ord(letter) - 38
                else:
                    sum += ord(letter) - 96
    return sum
    


print(finalScore_1("input.txt"))
print(finalScore_2("input.txt"))