# advent of code 2017 day 1
# 10/30/23 to 10/30/23

input = open("day1.txt", "r").read().strip()
sum = 0

skip = int(len(input)/2)
input += input[:skip]

for i in range(len(input)-(skip+1)):
    if input[i] == input[i+skip]:
        sum += int(input[i])

print(sum)
