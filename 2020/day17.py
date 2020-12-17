def solve1(lines):
    world = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                world.append((0,y,x))

    for _ in range(6):
        ns = {}
        for i in world:
            try:
                ns[i]
            except KeyError:
                ns[i] = 0
            for dx in range(-1,2):
                for dy in range(-1,2):
                    for dz in range(-1,2):
                        if not (dx==dy==dz==0):
                            try:
                                ns[(i[0]+dz,i[1]+dy,i[2]+dx)] += 1
                            except KeyError:
                                ns[(i[0]+dz,i[1]+dy,i[2]+dx)] = 1
        for n in ns.keys():
            if n in world and ns[n] not in [2,3]:
                world.remove(n)
            elif ns[n] == 3 and n not in world:
                world.append(n)
    return len(world)

def solve2(lines):
    world = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                world.append((0,0,y,x))

    for _ in range(6):
        ns = {}
        for i in world:
            try:
                ns[i]
            except KeyError:
                ns[i] = 0
            for dx in range(-1,2):
                for dy in range(-1,2):
                    for dz in range(-1,2):
                        for dw in range(-1,2):
                            if not (dx==dy==dz==dw==0):
                                try:
                                    ns[(i[0]+dw,i[1]+dz,i[2]+dy,i[3]+dx)] += 1
                                except KeyError:
                                    ns[(i[0]+dw,i[1]+dz,i[2]+dy,i[3]+dx)] = 1
        for n in ns.keys():
            if n in world and ns[n] not in [2,3]:
                world.remove(n)
            elif ns[n] == 3 and n not in world:
                world.append(n)
    return len(world)

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")