
txt = open(r"C:\Users\do556325\Documents\coding\PythonFun\2022\advent of code\day5.txt", "r")

# Hell
list1 = ["H","R","B","D","Z","F","L","S"]
list2 = ["T","B","M","Z","R"]
list3 = ["Z","L","C","H","N","S"]
list4 = ["S","C","F","J"]
list5 = ["P","G","H","W","R","Z","B"]
list6 = ["V","J","Z","G","D","N","M","T"]
list7 = ["G","L","N","W","F","S","P","Q"]
list8 = ["M","Z","R"]
list9 = ["M","C","L","G","V","R","T"]
templist = []

def numtolist(num):
    if num == 1:
        return list1
    elif num == 2:
        return list2
    elif num == 3:
        return list3
    elif num == 4:
        return list4
    elif num == 5:
        return list5
    elif num == 6:
        return list6
    elif num == 7:
        return list7
    elif num == 8:
        return list8
    else:
        return list9

for line in txt:
    # line to list
    list = line.split()
    list.pop(4)
    list.pop(2)
    list.pop(0)
    list = [int(i) for i in list]
    
    for i in range(list[0]):
        poplet = numtolist(list[1]).pop()
        templist.append(poplet)
    templist.reverse()
    numtolist(list[2]).extend(templist)
    templist.clear()

print(list1[-1], end="")
print(list2[-1], end="")
print(list3[-1], end="")
print(list4[-1], end="")
print(list5[-1], end="")
print(list6[-1], end="")
print(list7[-1], end="")
print(list8[-1], end="")
print(list9[-1])