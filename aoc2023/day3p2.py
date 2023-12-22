import re
file = open("./day3.txt", "r").read().splitlines()
numran=[]

for line in range(len(file)):
    symls=list(filter(None, re.split("\d|\.", file[line])))
    numls=re.findall("\d+", file[line])
    for num in range(len(numls)):
        numloc=file[line].find(numls[num])
        numrange=range(numloc,numloc+len(str(numls[num])))
        numran.append(numrange)

    for sym in range(len(symls)):
        symloc=file[line].find(symls[sym])
        #print(file[line][symloc])

        for x in range(-1,2):
            for y in range(-1,2):
                print(file[line+x][symloc+y], end=" ")
                if file[line+x][symloc+y].isdigit():
                    #start = 0
                    #end = 0
                    # for i in range(0, line + x):
                    #for j in range(line + x, len(file[line])):

            print()
        print()

#print(numran)
