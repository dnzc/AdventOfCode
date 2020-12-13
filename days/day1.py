def solve1(lines):
    x=list(map(int,lines))
    for a in x:
        for b in x:
            if a+b==2020:
                return a*b

def solve2(lines):
    x=list(map(int,lines))
    for a in x:
        for b in x:
            for c in x:
                if a+b+c==2020: return a*b*c

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")