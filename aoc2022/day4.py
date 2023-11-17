import re
txt = open(r"C:\Users\do556325\Documents\coding\PythonFun\2022\advent of code\day4.txt", "r")
count = 0

for line in txt:
    
    # making the line into a list
    list = re.split(r"-|,|\n",line,4)
    list.pop()
    list = [int(i) for i in list]
    
    if (
        list[0] >= list[2] and list[1] <= list[3] or
        list[2] >= list[0] and list[3] <= list[1] or
        list[0] < list[2] and (list[1] < list[3] and list[1] >= list[2]) or
        list[2] <= list[0] and (list[3] <= list[1] and list[3] >= list[0])
    ):
        count+=1
print(count)
txt.close()