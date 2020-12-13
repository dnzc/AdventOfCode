def solve2(lines):
    count=0
    for line in lines:
        a,c,pw=line.split()
        c=c[:-1]
        n1,n2=map(int,a.split("-"))
        if pw[n1-1]!=pw[n2-1] and (pw[n1-1]==c or pw[n2-1]==c): count+=1
    return count

def solve1(lines):
    count=0
    for line in lines:
        a,c,pw=line.split()
        c=c[:-1]
        n1,n2=map(int,a.split("-"))
        if pw.count(c) in range(n1,n2+1):count+=1
    return count

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")