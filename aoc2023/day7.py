from operator import itemgetter
import re
file = open("./day7.txt", "r").read().splitlines()

def returntype(cards):
    count=[]
    for letter in cards:
        count.append(cards.count(letter))
    if 5 in count: #Five of a Kind
        return 7
    if 4 in count: #Four of a Kind
        return 6
    if 3 in count and 1 in count: #Three of a kind
        return 4
    if 3 in count and 2 in count: #Full house
        return 5 
    if count.count(2) == 4: #Two pair
        return 3
    if count.count(2) == 2 and count.count(1)==3: #One pair
        return 2
    return 1

for line in range(len(file)):
    file[line] = re.sub("A", "E", file[line])
    file[line] = re.sub("T", "A", file[line])
    file[line] = re.sub("J", "B", file[line])
    file[line] = re.sub("Q", "C", file[line])
    file[line] = re.sub("K", "D", file[line])
    file[line] = f"{str(returntype(file[line][:5]))} {file[line]}"
    file[line] = re.split(" ", file[line])
file = sorted(file, key=itemgetter(0,1), reverse=True)

total = 0
for line in range(len(file)):
    file[line][0] = len(file) - line
    sum = int(file[line][2]) * file[line][0]
    #print(f"{file[line]}\t{sum}")
    total+=sum

print(total)
