def solve1(lines):
    a = lines[0].split()
    targetx = [*map(int, a[2][2:-1].split(".."))]
    targety = [*map(int, a[3][2:].split(".."))]
    maxy = None
    for Y in range(targety[0], targety[1]+1):
        for X in range(targetx[0], targetx[1]+1):
            # assume max y vel lies in this range
            for y in range(500):
                sq = (2*y+1)**2 - 8*Y
                if sq < 0: continue
                if int(sq**0.5)**2 != sq: continue
                for k in (0, 1):
                    n = int((2*y+1 + (-1)**k*sq**0.5)/2)
                    x = (Y + n*(n-1)//2)/n
                    n_dash = min(n, x)
                    x = (Y + n_dash*(n_dash-1)//2)/n
                    if int(x) != x: continue
                    if maxy == None or y>maxy:
                        maxy = y
    return maxy*(maxy+1)//2

def solve2(lines):
    # assume target x range is +ive
    a = lines[0].split()
    targetx = [*map(int, a[2][2:-1].split(".."))]
    targety = [*map(int, a[3][2:].split(".."))]

    vels = []
    for Y in range(targety[0], targety[1]+1):
        for X in range(targetx[0], targetx[1]+1):
            # assume initial y vel lies in this range
            for y in range(-500, 500):
                sq = (2*y+1)**2 - 8*Y
                if sq < 0: continue
                if int(sq**0.5)**2 != sq: continue
                for k in (0, 1):
                    n = int((2*y+1 + (-1)**k*sq**0.5)/2)
                    if n<0: continue
                    x = (X + n*(n-1)//2)/n
                    if n>x: x = ((8*X+1)**0.5 - 1)/2
                    if int(x) != x: continue
                    vels.append((int(x),y))
    return len(list(set(vels)))

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")