crates = {
1:['T','Q','V','C','D','S','N'],
2:['V','F','M'],
3:['M','H','N','P','D','W','Q','F'],
4:['F','T','R','Q','D'],
5:['B','V','H','Q','N','M','F','R'],
6:['Q','W','P','N','G','F','C'],
7:['T','C','L','R','F','W'],
8:['S','N','Z','T'],
9:['N','H','Q','R','J','D','S','M']
}
def finalScore_1(input) -> str:
    global crates
    message = []
    with open(input) as file:
        for line in file:
            splittedCommand = line.strip().split(" ")
            for i in range(int(splittedCommand[1])):
                crates[int(splittedCommand[5])].insert(0,crates[int(splittedCommand[3])].pop(0))
    newcrates = crates.copy()    
    for i in range(1,10):
        message.append(newcrates[i].pop(0))
    return ''.join(message)


def finalScore_2(input) -> str:
    global crates
    message = []
    with open(input) as file:
        for line in file:
            splittedCommand = line.strip().split(" ")
            if int(splittedCommand[1]) == 1:
                crates[int(splittedCommand[5])].insert(0,crates[int(splittedCommand[3])].pop(0))
                continue
            for i in range(int(splittedCommand[1])):
                crates[int(splittedCommand[5])].insert(i,crates[int(splittedCommand[3])].pop(0))
    newcrates = crates.copy()    
    for i in range(1,10):
        message.append(newcrates[i].pop(0))
    return ''.join(message)
                

#print(finalScore_1("input.txt"))
#print(finalScore_2("input.txt"))
