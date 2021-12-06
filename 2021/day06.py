def solve1(lines):
    l = [*map(int,lines[0].split(","))]
    for i in range(80):
        newl = []
        for i in l:
            if i>0:
                newl.append(i-1)
            else:
                newl.append(6)
                newl.append(8)
        l = list(newl)
    return len(l)

def solve2(lines):
    l = [*map(int,lines[0].split(","))]
    a = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for i in range(9): a[i] = l.count(i)
    for i in range(256):
        add = a[0]
        for i in range(8): a[i] = a[i+1]
        a[8] = add
        a[6] += add
    return sum(a.values())



import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")