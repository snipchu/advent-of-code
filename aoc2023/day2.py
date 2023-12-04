import re
file = open(r"./day2.txt", "r").read().splitlines()
powersum = 0

for i in range(len(file)):
    cubelist=re.split("; |: ", file[i])
    cubelist.pop(0)
    red = 0
    green = 0
    blue = 0
    for draw in cubelist:
        itemlist=re.split(", ", draw)
        for item in itemlist:
            num = int(re.sub('\D', '', item))
            if "red" in item and num > red:
                red = num
            elif "green" in item and num > green:
                green = num
            elif "blue" in item and num > blue:
                blue = num
    powersum += red*green*blue


print(powersum)
