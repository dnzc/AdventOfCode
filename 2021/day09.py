def solve1(lines):
    a = [[10000000] * (len(lines[0]) + 1)]
    for i in lines: a.append([1000000000000] + list(map(int, i.strip())) + [100000000000])
    a.append([100000000]*(len(lines[0])+1))
    t = 0
    for y in range(1, len(a)-1):
        for x in range(1, len(a[0])-1):
            if all(a[y][x] < a[y+dy][x+dx] for dy,dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]):
                t += a[y][x] + 1
    return t


def solve2(lines):
    basins = []
    a = [[10000000] * (len(lines[0]) + 1)]
    for i in lines: a.append([1000000000000] + list(map(int, i.strip())) + [100000000000])
    a.append([100000000]*(len(lines[0])+1))
    
    for y in range(1, len(a)-1):
        for x in range(1, len(a[0])-1):
            if all(a[y][x] < a[y+dy][x+dx] for dy,dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]):
                b = [(x+dx, y+dy) for dx,dy in [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)] if x+dx != 0 and x+dx != len(a[0])-1 and y+dy != 0 and y+dy != len(a)-1 and a[y+dy][x+dx] != 9]
                basins.append([set(b), b])

    while True:
        changed = False
        # print(basins)
        for basin in basins:
            newedges = []
            for x,y in basin[1]:
                b = [(x+dx, y+dy) for dx,dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] if x+dx != 0 and x+dx != len(a[0])-1 and y+dy != 0 and y+dy != len(a)-1 and a[y+dy][x+dx] > a[y][x] and a[y+dy][x+dx] != 9 and a[y+dy][x+dx] not in basin[0]]
                if len(b) > 0: changed = True
                newedges.extend(b)
            new = list(set(newedges))
            basin[0].update(new)
            basin[1] = list(new)
        if not changed: break

    c = sorted(len(i[0]) for i in basins)
    # print(c)
    return c[-1] * c[-2] * c[-3]



import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")