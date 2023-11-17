file2 = open(r"C:\Users\do556325\Documents\coding\PythonFun\2022\day2.txt", "r")
score = 0
for line in file2:
    line = line.split()
    # X - lose
    # Y - tie
    # Z - win
    if (
        line[0] == "B" and line[1] == "X" or
        line[0] == "A" and line[1] == "Y" or
        line[0] == "C" and line[1] == "Z"
    ):
        line[1] = "X" # Rock
    elif (
        line[0] == "C" and line[1] == "X" or
        line[0] == "B" and line[1] == "Y" or
        line[0] == "A" and line[1] == "Z"
    ):
        line[1] = "Y" # Paper
    else:
        line[1] = "Z" # Scissors

    if (
        line[0] == "A" and line[1] == "X" or
        line[0] == "B" and line[1] == "Y" or
        line[0] == "C" and line[1] == "Z"
    ):
        score += 3
    elif (
        line[0] == "A" and line[1] == "Z" or
        line[0] == "B" and line[1] == "X" or
        line[0] == "C" and line[1] == "Y"
    ):
        pass
    else:
        score += 6

    if line[1] == "X":
        score +=1
    elif line[1] == "Y":
        score +=2
    else:
        score+=3

print(score)
file2.close()