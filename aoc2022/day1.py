file = open(r"C:\Users\do556325\Documents\coding\PythonFun\2022\advent of code\day1.txt", "r")
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