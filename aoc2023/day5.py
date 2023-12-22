import re
file = open("./day5.txt", "r").read().splitlines()
seeds = re.split(": | ", file[0])
seeds.pop(0)
file.pop(0)
file.pop(0)

seeds = [eval(i) for i in seeds]
file = [i for i in file if ("-" not in i)]

actualfile=[]
numbers=[]
for set in file:
    if set:
        numbers.append(set)
    else:
        actualfile.append(numbers)
        numbers=[]

for map in actualfile:
    for line in map:
        lol = re.split("\D", line)
        lol = [int(i) for i in lol if i.isdigit()]
        numbers.append(lol)
print(numbers)
