from collections import defaultdict

def solve1(lines):
    # start is 0, end is $
    g = defaultdict(list)
    for line in lines:
        x,y = line.split("-")
        g[x].append(y)
        g[y].append(x)

    # start, end, small
    def getnumpathstoend(visited, node):
        t = 0
        for i in g[node]:
            if i == "end": t += 1
            elif i=="start": continue
            elif i not in visited:
                t += getnumpathstoend(visited if node.isupper() else visited+[node], i)
        return t
    return getnumpathstoend([], "start")

def solve2(lines):
    # start is 0, end is $
    g = defaultdict(list)
    for line in lines:
        x,y = line.split("-")
        g[x].append(y)
        g[y].append(x)

    # start, end, small
    def getnumpathstoend(visited, node, usedtwice):
        t = 0
        for i in g[node]:
            if i == "end": t += 1
            elif i=="start": continue
            elif i not in visited:
                t += getnumpathstoend(visited if node.isupper() else visited+[node], i, usedtwice)
            elif not usedtwice:
                    t += getnumpathstoend(visited if node.isupper() else visited+[node], i, True)
        return t
    return getnumpathstoend([], "start", False)



import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")
