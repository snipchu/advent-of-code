import re
file = open("./day9.txt", "r").read().splitlines()

def newsequence(oldsequence):
    list = []
    for line in range(1,len(oldsequence)):
        list.append(oldsequence[line]-oldsequence[line-1])
    return list

sum = 0
for line in range(len(file)):
    file[line] = re.split(" ", file[line])
    file[line] = [int(i) for i in file[line]]
    archive = [file[line], newsequence(file[line])]

    while archive[-1].count(0) != len(archive[-1]):
        archive.append(newsequence(archive[-1]))

    archive[-1].append(0)
    archive.reverse()

    for line in range(1,len(archive)):
        archive[line].insert(0,archive[line][0]-archive[line-1][0])
        #archive[line].append(archive[line][-1]+archive[line-1][-1])
    sum += archive[-1][0]
print(sum)
