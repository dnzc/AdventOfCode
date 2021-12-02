def solve1(lines):
    depth = 0
    hor = 0
    for i in lines:
        a = i.split()
        if a[0]=="forward": hor += int(a[1])
        elif a[0]=="down": depth += int(a[1])
        elif a[0]=="up": depth -= int(a[1])
    return depth*hor

def solve2(lines):
    depth = 0
    hor = 0
    aim = 0
    for i in lines:
        a = i.split()
        if a[0]=="forward":
            hor += int(a[1])
            depth += aim*int(a[1])
        elif a[0]=="down": aim += int(a[1])
        elif a[0]=="up": aim -= int(a[1])
    return depth*hor



import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")