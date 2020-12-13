def solve1(lines):
    lines = list(map(int,lines))
    preamblelength = 25
    asdf =lines[:preamblelength]

    def is_valid(l, next, preamblelength):
        for a in range(len(l)):
                for b in range(a+1,len(l)):
                    if l[a]+l[b]==next:
                        return True
        return False

    for i in range(preamblelength,len(lines)):
        if is_valid(asdf,lines[i], preamblelength):
            asdf.append(lines[i])
            asdf.pop(0)
        else:
            return lines[i]

def solve2(lines):
    lines=list(map(int,lines))
    for i in range(len(lines)):
        for j in range(i+2,len(lines)+1):
            asdf = sum(lines[i:j])
            if asdf==1492208709:
                return min(lines[i:j])+max(lines[i:j])

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")