from copy import deepcopy

def solve1(lines):
    lines = [list(j) for j in lines]

    prevstate = deepcopy(lines)
    while True:
        neighbours = deepcopy(lines)

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                numoccupied=0
                for j in [-1,0,1]:
                    for k in [-1,0,1]:
                        if y+j in range(len(lines)) and x+k in range(len(lines[y])) and lines[y+j][x+k] == "#":
                            numoccupied+=1
                if lines[y][x]=="#":numoccupied-=1
                neighbours[y][x] = numoccupied

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == "L" and neighbours[y][x] == 0:
                    lines[y][x] = "#"
                elif lines[y][x] == "#" and neighbours[y][x]>=4:
                    lines[y][x] = "L"

        if prevstate==lines:break

        prevstate = deepcopy(lines)

    return sum([i.count("#") for i in lines])

def solve2(lines):
    lines = [list(j) for j in lines]

    prevstate = deepcopy(lines)
    while True:
        neighbours = deepcopy(lines)

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                numoccupied=0
                for j in [-1,0,1]:
                    for k in [-1,0,1]:
                        direction = [j,k]
                        if direction==[0,0]:continue
                        count=0
                        found=False
                        while not found:
                            count+=1
                            if y+direction[0]*count in range(len(lines)) and x+direction[1]*count in range(len(lines[y])):
                                if lines[y+direction[0]*count][x+direction[1]*count]=="#":
                                    numoccupied+=1
                                if lines[y+direction[0]*count][x+direction[1]*count] in "#L":
                                    found=True
                            else:found=True
                neighbours[y][x] = numoccupied

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == "L" and neighbours[y][x] == 0:
                    lines[y][x] = "#"
                elif lines[y][x] == "#" and neighbours[y][x]>=5:
                    lines[y][x] = "L"

        if prevstate==lines:break

        prevstate = deepcopy(lines)

    return sum([i.count("#") for i in lines])

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")