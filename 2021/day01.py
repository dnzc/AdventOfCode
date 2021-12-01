def solve1(lines):
    prev = 1000000000000000
    c=0
    for i in lines:
        if int(i) > prev: c+=1
        prev = int(i)
    return c

def solve2(lines):
    prev = 1000000000000000
    c=0
    for i in range(len(lines)-2):
        a = sum(int(i) for i in lines[i:i+3])
        if a > prev: c+=1
        prev = a
    return c


import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")