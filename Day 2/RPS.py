'''
PART 1
-------------------------
Elf input can be one of these 
A: Rock
B: Paper
C: Scissors

Your input can be one of these
X: Rock
Y: Paper
Z: Scissors

your final score = (1 for Rock, 2 for Paper, and 3 for Scissors) + the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
-------------------------

PART 2

column 2 tells you what to do 
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
'''


score = {"X":1,"Y":2,"Z":3}

score_2 = {"A":3,"B":1,"C":2}

score_3 = {"A":1,"B":2,"C":3}

score_4 = {"A":2,"B":3,"C":1}




def finalScore_1(input) -> int:
    sum = 0
    with open(input) as file:
        for line in file:
            #sum = 0
            round = line.strip().split(" ")
            if (round[0] == 'A' and round[1] == 'X') or (round[0] == 'B' and round[1] == 'Y') or (round[0] =='C' and round[1] == 'Z'):
                sum += 3 + score[round[1]]
            elif (round[0] == 'A' and round[1] == 'Y') or (round[0] == 'B' and round[1] == 'Z') or (round[0] =='C' and round[1] == 'X'):
                sum += 6 + score[round[1]]
            else:
                sum += 0 + score[round[1]]    
            
    return sum

def finalScore_2(input) -> int:
    sum = 0
    with open(input) as file:
        for line in file:
            #sum = 0 
            round = line.strip().split(" ")
            if round[1] == 'X':
                sum += 0 + score_2[round[0]]
            elif round[1] == 'Y':
                sum += 3 + score_3[round[0]]
            else:
                sum += 6 + score_4[round[0]]    
    return sum
    

print(finalScore_1("input.txt"))
print(finalScore_2("input.txt"))