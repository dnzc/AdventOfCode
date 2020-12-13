def solve1(lines):
    earliest = int(lines[0])
    s = [int(i) for i in lines[1].split(",") if i!="x"]
    x=0
    while True:
        x+=1
        for i in s:
            if (earliest+x)%i==0:
                return x*i


from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def solve2(lines):
    n = []
    a = []
    for i in enumerate(lines[1].split(",")):
        if i[1]!="x":
            n.append(int(i[1]))
            a.append(int(i[1])-i[0])
    return chinese_remainder(n,a)

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")