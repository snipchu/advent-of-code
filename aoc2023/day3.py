import re
file = open("./day3.txt", "r").read().splitlines()
sum = 0

file.insert(0,len(file[0])*'.')
file.append(len(file[0])*'.')
for line in range(len(file)):
    file[line] = '.'+file[line]
    file[line] += '.'

def lol():
    for digit in numrange:
        templist= [ file[line-1][digit-1], file[line-1][digit], file[line-1][digit+1], 
                    file[line][digit-1], file[line][digit], file[line][digit+1],
                    file[line+1][digit-1], file[line+1][digit], file[line+1][digit+1]] 
        for i in templist:
            if i.isalnum()==False and i!=".":
                return int(linenums[number])
    return 0

for line in (range(len(file))):
    linenums = re.findall("\d+", file[line])

    for number in range(len(linenums)):
        numlocation = file[line].find(linenums[number])
        numrange = range(numlocation, numlocation+len(linenums[number]))
        sum += lol()

print(sum)
