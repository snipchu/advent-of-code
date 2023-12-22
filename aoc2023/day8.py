# World's most horrendous code ever
import re, itertools, sys
sys.setrecursionlimit(999999999)
file = open("./day8.txt", "r").read().splitlines()

directions = file.pop(0)
directions = re.sub("L", "1", directions)
directions = re.sub("R", "2", directions)

network = []
startnodes=[]

for line in file:
    line = re.split(" = \(|, |\)",line)
    line.pop()
    network.append(line)
    if line[0][2]=="A":
        startnodes.append(line)

def findnode(nodename):
    for node in range(len(network)):
        if network[node][0]==nodename:
            return node

iter=0
nodelist = []
steps=[]
def sdfs(startnodes):
    global iter
    global nodelist
    for nodes in startnodes:
        nodelist.append(findnode(nodes[0])) #nodename
    for node in nodelist:
        smth(node,nodelist)
        iter=0

templist=[]
othertemplist=[]
def smth(node,nodelist):    
    global iter
    global steps
    global othertemplist
    global templist
    nodename=network[node][int(directions[iter%len(directions)])]
    templist.append(nodename[2])
    iter+=1

    if templist.count("Z")==1 and nodename[2]=="Z":
        print(f"Took {iter} steps to reach the first Z")
        othertemplist.append(iter)
        smth(findnode(nodename), nodelist)
    elif templist.count("Z")==2:
        print(f"Took {iter-othertemplist[0]} steps to reach the next Z")
        othertemplist.append(iter-othertemplist[0])
        othertemplist.append(0)
        steps.append(othertemplist)
        print(othertemplist)
        othertemplist=[]
        templist=[]

    else:
        smth(findnode(nodename), nodelist)

sdfs(startnodes)
print(steps)
count = 0
sums=[line[2] for line in steps]

print(f"{count} | {steps} | {sums}")
while len(set(sums))!=1:
    for line in steps:
        if count%line[1]==0:
            line[2] += line[1]

    sums=[line[2] for line in steps]
    count +=1
    print(f"{count} | {steps} | {sums}")

print(count)
