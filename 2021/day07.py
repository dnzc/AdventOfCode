def solve1(lines):
    a = list(map(int,lines[0].split(",")))
    costs = []
    for i in range(max(a)+1):
        cost = sum(abs(j-i) for j in a)
        costs.append(cost)
    return min(costs)

def solve2(lines):
    a = list(map(int,lines[0].split(",")))
    costs = []
    for i in range(max(a)+1):
        cost = sum(abs(j-i)*(abs(j-i)+1)//2 for j in a)
        costs.append(cost)
    return min(costs)


import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")