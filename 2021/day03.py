def solve1(lines):
    asdf = [''.join(i) for i in zip(*[list(i) for i in lines])]
    g = ""
    e = ""
    for i in asdf:
        g += "0" if i.count("0") > i.count("1") else "1"
        e += "1" if i.count("0") > i.count("1") else "0"
    return int(g, 2) * int(e, 2)

def solve2(lines):
    a = lines
    a2 = []
    for i in range(len(lines[0])):
        asdf = [''.join(i) for i in zip(*[list(i) for i in a])]
        t = "0" if asdf[i].count("0") > asdf[i].count("1") else "1"
        a2 = [j for j in a if j[i]==t]
        a = list(a2)
        if len(a) == 1: break
    ox = int(a[0], 2)

    a = lines
    a2 = []
    for i in range(len(lines[0])):
        asdf = [''.join(i) for i in zip(*[list(i) for i in a])]
        t = "1" if asdf[i].count("0") > asdf[i].count("1") else "0"
        a2 = [j for j in a if j[i]==t]
        a = list(a2)
        if len(a) == 1: break
    co = int(a[0], 2)

    return ox*co



import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")