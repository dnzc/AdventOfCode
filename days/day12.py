def move(dir,pos,amt):
        if dir=="N":pos[1]+=amt
        elif dir=="S":pos[1]-=amt
        elif dir=="E":pos[0]+=amt
        elif dir=="W":pos[0]-=amt
        return pos

def solve1(lines):
    pos = [0,0]
    direc = "E"
    for line in lines:
        dir = line[0]
        amt = int(line[1:])
        if dir in "NSEW":
            pos = move(dir,pos,amt)
        elif dir=="F":
            pos=move(direc,pos,amt)
        elif dir=="L":
            direc = "NWSENWSE"["NWSENWSE".index(direc)+amt//90]
        elif dir=="R":
            direc = "NESWNESW"["NESWNESW".index(direc)+amt//90]
    return abs(pos[0])+abs(pos[1])

def solve2(lines):
    pos = [0,0]
    waypoint = [10,1]
    for line in lines:
        dir = line[0]
        amt = int(line[1:])
        if dir in "NSEW":
            waypoint = move(dir,waypoint,amt)
        elif dir=="F":
            pos[0]+=waypoint[0]*amt
            pos[1]+=waypoint[1]*amt
        else:
            if line in ["R270","L90"]:
                #left
                waypoint = [-waypoint[1],waypoint[0]]
            elif line in ["R90","L270"]:
                #right
                waypoint = [waypoint[1],-waypoint[0]]
            else:
                #180deg
                waypoint = [-waypoint[0],-waypoint[1]]
    return abs(pos[0])+abs(pos[1])

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")