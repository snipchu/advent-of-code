from operator import itemgetter
from statistics import mode
import re
file = open("./day7.txt", "r").read().splitlines()

def returntype(cards):
    returnval = 0
    jval=0
    count=[]
    for letter in cards:
        if letter=="1":
            letter=mode(cards)
        else:
            count.append(cards.count(letter))

    if 5 in count: #Five of a Kind
        returnval=6
    if 4 in count: #Four of a Kind
        returnval=5
    if 3 in count and 2 in count: #Full house
        returnval=4
    if 3 in count and 1 in count: #Three of a kind
        returnval=3
    if count.count(2) == 4: #Two pair
        returnval=2
    if count.count(2) == 2 and count.count(1)==3: #One pair
        returnval=1
    return returnval

for line in range(len(file)):
    file[line] = re.sub("A", "D", file[line])
    file[line] = re.sub("T", "A", file[line])
    file[line] = re.sub("J", "1", file[line])
    file[line] = re.sub("Q", "B", file[line])
    file[line] = re.sub("K", "C", file[line])
    file[line] = f"{str(returntype(file[line][:5]))} {file[line]}"
    file[line] = re.split(" ", file[line])
file = sorted(file, key=itemgetter(0,1), reverse=True)

total = 0
for line in range(len(file)):
    file[line][0] = len(file) - line
    sum = int(file[line][2]) * file[line][0]
    print(f"{file[line]}\t{sum}")
    total+=sum

print(total)
