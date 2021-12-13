def solve1(lines):
    coords = []
    a = "\n".join(lines).split("\n\n")
    for line in a[0].split("\n"):
        coords.append([*map(int,line.split(","))])
    for line in a[1].split("\n"):
        if line[11] == "x":
            for i in range(len(coords)):
                coords[i][0] = min(coords[i][0], 2*int(line[13:]) - coords[i][0])
        elif line[11] == "y":
            for i in range(len(coords)):
                coords[i][1] = min(coords[i][1], 2*int(line[13:]) - coords[i][1])
        return len(list(set((i,j) for i,j in coords)))

def solve2(lines):
    coords = []
    a = "\n".join(lines).split("\n\n")
    for line in a[0].split("\n"):
        coords.append([*map(int,line.split(","))])
    for line in a[1].split("\n"):
        if line[11] == "x":
            for i in range(len(coords)):
                coords[i][0] = min(coords[i][0], 2*int(line[13:]) - coords[i][0])
        elif line[11] == "y":
            for i in range(len(coords)):
                coords[i][1] = min(coords[i][1], 2*int(line[13:]) - coords[i][1])

    maxx, maxy = max(i[0] for i in coords), max(i[1] for i in coords)

    asdf = [[" " for i in range(maxx+1)] for j in range(maxy+1)]
    for i in coords:
        asdf[i[1]][i[0]] = "#"
    for i in asdf:
        print("".join(i))



import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")
