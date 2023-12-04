import re
file = open("./day4.txt", "r").read().splitlines()
total = 0
for line in file:
    points = 0
    result = re.split(": | \| ", line)
    result.pop(0)
    winninglist = re.split(" ", result[0])
    mylist = re.split(" ", result[1])
    print(mylist)
    winninglist = [i for i in winninglist if i]
    mylist = [i for i in test_list if i]
    for i in range(len(mylist)):
        if points==0 and mylist[i] in winninglist:
            points=1
            print(f"first: {mylist[i]}")
        elif points>0 and mylist[i] in winninglist:
            points= points*2
            print(f"new: {mylist[i]}")

    print(points)
    total += points

print(total)
