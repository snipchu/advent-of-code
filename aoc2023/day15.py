import re

file = open("./day15.txt", "r").read()
file = re.split(",|\n", file)
file.pop()

results =[]
for item in range(len(file)):
    currval = 0
    for letter in range(len(file[item])):
        currval += ord(file[item][letter])
        currval *= 17
        currval = currval%256
    results.append(currval)

print(sum(results))
