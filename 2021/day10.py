def solve1(lines):
    t=0
    for line in lines:
        invalid = False
        asdf = []
        for i in line:
            if i in "([{<": asdf.append(i)
            else:
                d = {")":"(", "]":"[", "}":"{", ">":"<"}
                if d[i] != asdf.pop(-1):
                    t+={")":3, "]":57, "}":1197, ">":25137}[i]
                    invalid = True
            if invalid: break
    return t

def solve2(lines):
    a = []
    for line in lines:
        invalid = False
        asdf = []
        for i in line:
            if i in "([{<": asdf.append(i)
            else:
                d = {")":"(", "]":"[", "}":"{", ">":"<"}
                if d[i] != asdf.pop(-1):
                    invalid = True
            if invalid: break
        else:
            a.append("".join(asdf))
    d = {"(":")", "[":"]", "{":"}", "<":">"}
    a = [''.join(d[i] for i in j[::-1]) for j in a]
    c = {i:0 for i in a}
    for i in c.keys():
        t=0
        for j in i:
            t*=5
            t+={")":1, "]":2, "}":3, ">":4}[j]
        c[i] = t
    f = sorted(c.keys(), key=lambda x:c[x])
    return c[f[len(f)//2]]


import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")