def finalScore_1(input) -> int:
    sum = 0
    with open(input) as file:
        for line in file:
            round = line.strip().split(",")
            firstRange = round[0].split("-")
            secondRange =round[1].split("-")
            if ((int(firstRange[0]) <= int(secondRange[0])) and int(firstRange[1]) >= int(secondRange[1])):
                sum+=1
            elif ((int(firstRange[0]) >= int(secondRange[0])) and int(firstRange[1]) <= int(secondRange[1])):
                sum+=1
            
    return sum



def finalScore_2(input) -> int:
    sum = 0
    with open(input) as file:
        for line in file:
            round = line.strip().split(",")
            firstRange = round[0].split("-")
            secondRange =round[1].split("-")
            if ((int(firstRange[1]) - int(firstRange[0]))) >= (int(secondRange[1]) - int(secondRange[0])):
                frange = [x for x in range(int(firstRange[0]),int(firstRange[1])+1)]
                
                if (int(secondRange[0]) in frange) or (int(secondRange[1]) in frange):
                    print("yes")
                    sum +=1
            else:
                srange = [x for x in range(int(secondRange[0]),int(secondRange[1])+1)]
                if (int(firstRange[0]) in srange) or (int(firstRange[1]) in srange):
                    print("yes 2")
                    sum +=1

    return sum
                

print(finalScore_1("input.txt"))
print(finalScore_2("input.txt"))