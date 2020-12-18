import re

# especially proud of this

def solve1(lines):
    def evalexp(inp):
        if "(" in inp:
            for i in re.findall(r"\([^\(\)]+\)",inp):
                inp = inp.replace(i,str(evalexp(i[1:-1])))
            return evalexp(inp)
        else:
            q = inp.split()
            t = q[0]
            for i in range(0,len(q[1:]),2):
                t = eval(str(t)+''.join(q[1:][i:i+2]))
            return int(t)
    return sum(evalexp(line) for line in lines)

def solve2(lines):
    def evalexp(inp):
        if "(" in inp:
            for i in re.findall(r"\([^\(\)]+\)",inp):
                inp = inp.replace(i,str(evalexp(i[1:-1])))
            return evalexp(inp)
        else:
            q=1
            for i in inp.split("*"):
                q*=eval(i)
            return q
    return sum(evalexp(line) for line in lines)

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
# print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")