def solve1(lines):
    x=0
    count=0
    for line in lines:
        if line[x%len(line)]=="#":
            count+=1
        x+=3
    return count

def solve2(lines):
    def f(slope):
        return [lines[i][i*slope[0]//slope[1]%len(lines[i])] for i in range(0,len(lines),slope[1])].count("#")
    return f([1,1])*f([3,1])*f([5,1])*f([7,1])*f([1,2])

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")