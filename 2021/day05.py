from collections import defaultdict

def solve1(lines):
    a = defaultdict(int)
    for line in lines:
        b,c = line.split(" -> ")
        x1,y1 = map(int,b.split(","))
        x2,y2 = map(int,c.split(","))
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2)+1): a[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2)+1): a[(x, y1)] += 1

    return sum(1 for i in a.keys() if a[i] > 1)

def solve2(lines):
    a = defaultdict(int)
    for line in lines:
        b,c = line.split(" -> ")
        x1,y1 = map(int,b.split(","))
        x2,y2 = map(int,c.split(","))
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2)+1): a[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2)+1): a[(x, y1)] += 1
        elif abs(x1-x2) == abs(y1-y2):
            asdf = abs(x1-x2)
            xmult = 1 if x2 > x1 else -1
            ymult = 1 if y2 > y1 else -1
            for x in range(asdf+1): a[(x1+x*xmult, y1+x*ymult)] += 1

    return sum(1 for i in a.keys() if a[i] > 1)



import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")