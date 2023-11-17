file = open(r"C:\Users\do556325\Documents\coding\PythonFun\2022\advent of code\day3.txt", "r")
sum = 0
counter = 1

def tonumber(letter):
    if letter.islower() == True:
        letter = ord(letter)-96
    else:
        letter = ord(letter)-38
    return letter
    
for line in file:
    if counter == 1:
        test = set(line)
        test.remove("\n")
    elif counter == 2:
        test2 = set(line)
        test2.remove("\n")
    else:
        test3 = set(line)
        test3.remove("\n")
        commonletter = test.intersection(test2, test3)
        commonletter = ''.join(map(str, commonletter))
        sum += tonumber(commonletter)
        counter = 0
    counter+=1
    
#for line in file:
#    test = (list(line)).pop()
#    firsthalf = set(test[:len(test)//2])
#    secondhalf = set(test[len(test)//2:])
#    
#    commonletter = firsthalf.intersection(secondhalf)
#    commonletter = ''.join(map(str, commonletter))
#    sum += tonumber(commonletter)

print(sum)
file.close()