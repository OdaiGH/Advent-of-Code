def finalScore(input) -> int:
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
    


print(finalScore("input.txt"))