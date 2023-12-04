file = open(r"./day1.txt", "r")
sum = 0
elves = []

for line in file:
    if line.strip() != "":
        sum+=int(line)
    else:
        elves.append(sum)
        sum = 0

elves.sort(reverse=True)
print(elves[:3])

file.close()
