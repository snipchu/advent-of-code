txt = str(open(r"C:\Users\do556325\Documents\coding\PythonFun\2022\advent of code\day6.txt","r").read())
txt = list(txt)
list = txt[0:14]
update = 1
while len(list) != len(set(list)):
    list = txt[update:14+update]
    update += 1
print(13+update)