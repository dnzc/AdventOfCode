import re

def solve1(lines):
    black = []
    for line in lines:
        curpos=[0,0]
        for i in re.findall("e|se|sw|w|nw|ne", line):
            if i=="e":
                curpos[0]+=1
            elif i=="w":
                curpos[0]-=1
            elif i=="se":
                curpos[0]+=curpos[1]%2
                curpos[1]-=1
            elif i=="sw":
                curpos[0]+=curpos[1]%2-1
                curpos[1]-=1
            elif i=="nw":
                curpos[0]+=curpos[1]%2-1
                curpos[1]+=1
            elif i=="ne":
                curpos[0]+=curpos[1]%2
                curpos[1]+=1
        if curpos not in black:
            black.append(list(curpos))  
        else:
            black.remove(list(curpos))
    return len(black)


def solve2(lines):
    black = []
    for line in lines:
        curpos=[0,0]
        for i in re.findall("e|se|sw|w|nw|ne", line):
            if i=="e":
                curpos[0]+=1
            elif i=="w":
                curpos[0]-=1
            elif i=="se":
                curpos[0]+=curpos[1]%2
                curpos[1]-=1
            elif i=="sw":
                curpos[0]+=curpos[1]%2-1
                curpos[1]-=1
            elif i=="nw":
                curpos[0]+=curpos[1]%2-1
                curpos[1]+=1
            elif i=="ne":
                curpos[0]+=curpos[1]%2
                curpos[1]+=1
        if curpos not in black:
            black.append(list(curpos))  
        else:
            black.remove(list(curpos))
        
    for i in range(100):
        nbs = {}
        for cell in black:
            if tuple(cell) not in nbs.keys():
                nbs[tuple(cell)] = 0
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx==dy==0 or dx==(-1)**(cell[1]%2) and dy!=0:
                        continue
                    adj = (cell[0]+dx,cell[1]+dy)
                    if adj in nbs.keys():
                        nbs[adj] += 1
                    else:
                        nbs[adj] = 1
        newblack=list(black)
        for cell in nbs.keys():
            if list(cell) in black and nbs[cell] not in [1,2]:
                if list(cell) in newblack: newblack.remove(list(cell))
            elif list(cell) not in black and nbs[cell]==2:
                if list(cell) not in newblack: newblack.append(list(cell))
        black = list(newblack)
    return len(black) 


    
lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")