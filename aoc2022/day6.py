txt = str(open(r"./day6.txt","r").read())
txt = list(txt)
list = txt[0:14]
update = 1
while len(list) != len(set(list)):
    list = txt[update:14+update]
    update += 1
print(13+update)
