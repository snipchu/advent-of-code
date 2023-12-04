import re
file = open(r"./day2.txt", "r").read().splitlines()
validids = 0

for i in range(len(file)):
    validrounds = 0
    cubelist=re.split("; |: ", file[i])
    cubelist.pop(0)
    for draw in cubelist:
        red = 0
        green = 0
        blue = 0
        itemlist=re.split(", ", draw)
        for item in itemlist:
            num = int(re.sub('\D', '', item))
            if "red" in item:
                red += num
            elif "green" in item:
                green += num
            else:
                blue += num
        if red <= 12 and green <= 13 and blue <= 14:
            validrounds+=1

    if validrounds == len(cubelist):
        validids += i+1



print(validids)
