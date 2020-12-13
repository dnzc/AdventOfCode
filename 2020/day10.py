from functools import lru_cache

def solve1(lines):
    lines = sorted(map(int,lines))
    lines = [0] + lines + [lines[-1]+3]
    diffs = [b-a for a,b in zip(lines[:-1],lines[1:])]
    return diffs.count(1)*diffs.count(3)

def solve2(lines):
    lines = sorted(map(int,lines))
    lines = [0] + lines + [lines[-1]+3]
    asdf = {}

    for i in lines:
        asdf[i] = [j for j in [i+1,i+2,i+3] if j in lines]

    print(asdf)
    print(lines)

    @lru_cache(maxsize=None)
    def count(start):
        total=0
        print(start)
        if start==max(lines):
            return 1
        for i in asdf.get(start,[]):
            total += count(i)
        return total

    return count(lines[0])

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")