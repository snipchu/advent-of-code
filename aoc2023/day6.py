import re
file = open("./day6.txt", "r").read().splitlines()

for line in range(len(file)):
    file[line] = re.split(" ", file[line])
    file[line] = [int(i) for i in file[line] if i.isdigit()]
#print(file[0])
total = 1
for time in range(len(file[0])):
    lol=0
    for speed in range(1,file[0][time]):
        dist = (file[0][time]-speed)*speed
        if dist>file[1][time]:
            lol+=1
    print(lol)
    total*=lol
print(total)
