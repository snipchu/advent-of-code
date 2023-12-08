import re, itertools, sys
sys.setrecursionlimit(9999999)
file = open("./day8.txt", "r").read().splitlines()

directions = file.pop(0)
directions = re.sub("L", "1", directions)
directions = re.sub("R", "2", directions)
#print(directions)

network = []
for line in file:
    line = re.split(" = \(|, |\)",line)
    line.pop()
    network.append(line)

def findnode(nodename):
    for node in range(len(network)):
        if network[node][0]==nodename:
            return node

iter=0
def sdfs(nodename):
    global iter
    node = findnode(nodename)
    nodename=network[node][int(directions[iter%len(directions)])]
    iter+=1
    
    if nodename != "ZZZ":
        sdfs(nodename)

sdfs("AAA")
print(iter)
