import copy

def solve1(lines):
    line=0
    acc=0
    seenlines=[]
    while True:
        seenlines.append(line)
        asdf = lines[line].split()
        if asdf[0]=="nop":line+=1
        elif asdf[0]=="acc":
            acc+=int(asdf[1])
            line+=1
        elif asdf[0]=="jmp":
            line += int(asdf[1])
        if line in seenlines:
            return acc

def solve2(lines):

    def trylines(l):
     line = 0
     acc=0

     seenlines=[]
     while line<len(l):
        seenlines.append(line)
        asdf = l[line].split()
        if asdf[0]=="nop":line+=1
        elif asdf[0]=="acc":
            acc+=int(asdf[1])
            line+=1
        elif asdf[0]=="jmp":
            line += int(asdf[1])
        if line in seenlines:
            return (False,None)
     return (True,acc)

    asdf = ["nop","jmp"]
    
    for i in range(len(lines)):
        q=copy.deepcopy(lines)
        if q[i][:3] in asdf:
            q[i] = asdf[1-asdf.index(q[i][:3])] + q[i][3:]
            x=trylines(q)
            if x[0]:return x[1]

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")