def solve1(lines):
    # should have done
    # return max([int(p[:-3].replace("F","0").replace("B","1"), 2)*8 + int(p[-3:].replace("L","0").replace("R","1"), 2) for p in lines])
    asdf = []
    for p in lines:
        r=[0,128]
        for a in p[:-3]:
            if a=="F":
                r[1]=(r[1]-r[0])//2 + r[0]
            else:
                r[0]=(r[1]-r[0])//2 + r[0]
        row=r[0]
        r=[0,8]
        for a in p[-3:]:
            if a=="L":
                r[1]=(r[1]-r[0])//2 + r[0]
            else:
                r[0]=(r[1]-r[0])//2 + r[0]
        col=r[0]
        asdf.append(row*8+col)
    return max(asdf)

def solve2(lines):
    asdf = []
    for p in lines:
        r=[0,128]
        for a in p[:-3]:
            if a=="F":
                r[1]=(r[1]-r[0])//2 + r[0]
            else:
                r[0]=(r[1]-r[0])//2 + r[0]
        row=r[0]
        r=[0,8]
        for a in p[-3:]:
            if a=="L":
                r[1]=(r[1]-r[0])//2 + r[0]
            else:
                r[0]=(r[1]-r[0])//2 + r[0]
        col=r[0]
        asdf.append([row,col])
    
    q=[]
    for r in range(1,127):
        for c in range(1,7):
            if [r,c] not in asdf and [r+1,c+1] in asdf and [r-1,c-1] in asdf:
                q.append([r,c])
    return q[0][0]*8+q[0][1]

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")