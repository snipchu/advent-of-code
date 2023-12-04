import re
file = open("./day4.txt", "r").read().splitlines()
copies = []
modifiedfile = []

for line in range(len(file)):
    scratchcards = 0

    result = re.split(": | \| ", file[line])
    result[0] = int(result[0][5:])
    winninglist = re.split(" ", result[1])
    winninglist = [i for i in winninglist if i]
    mylist = re.split(" ", result[2])
    mylist = [i for i in mylist if i]

    for i in range(len(mylist)):
        if mylist[i] in winninglist:
            scratchcards+=1

    copies.append(scratchcards)
    modifiedfile.append(result)

for i in range(len(copies)):
    for ii in range(1,copies[i]+1):
        for iii in range(modifiedfile.count(modifiedfile[i])):
            modifiedfile.append(modifiedfile[i+ii])

modifiedfile.sort()
print(len(modifiedfile))
