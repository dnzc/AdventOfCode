import re

# proud of part 1, just glad that I managed to solve part 2, it's ugly but works :)

def solve1(lines):
    asdf = {}
    for i in '\n'.join(lines).split("\n\n")[0].split("\n"):
       asdf[int(i.split(": ")[0])] = i.split(": ")[1]

    def getrule(num):
        if "\"" in asdf[num]: return asdf[num][1:-1]
        ret = []
        for i in asdf[num].split(" | "):
            q=[]
            for j in i.split():
                if j.isdigit():q.append(getrule(int(j)))
            ret.append(''.join(q))
        return '(' + '|'.join(ret) + ')'
        
    rule = getrule(0)
    # print(rule)

    count = 0
    for line in '\n'.join(lines).split("\n\n")[1].split("\n"):
        if re.sub(rule,'',line) == "": count+=1
    
    return count

def solve2(lines):
    asdf = {}
    for i in '\n'.join(lines).split("\n\n")[0].split("\n"):
       asdf[int(i.split(": ")[0])] = i.split(": ")[1]
    asdf[8] = "42 | 42 8"
    asdf[11] = "42 31 | 42 11 31"
    
    def getrule(num, seen, depth):
        seen = dict(seen)
        try:
            seen[num] += 1
        except KeyError:
            seen[num] = 1
        stop = seen[num] > depth
        if "\"" in asdf[num]: return asdf[num][1:-1]
        ret = []
        for i in asdf[num].split(" | "):
            q=[]
            for j in i.split():
                if stop: return ""
                if j.isdigit():q.append(getrule(int(j), seen, depth))
            ret.append(''.join(q))
        return '(' + '|'.join(ret) + ')'
        
    def get(depth):
        seen = []
        rule = getrule(0, seen, depth)
        return "^"+rule+"$"

    rules = [get(i) for i in range(10)]
    count = 0
    for line in '\n'.join(lines).split("\n\n")[1].split("\n"):
        if any(re.sub(rule,'',line) == "" for rule in rules): count+=1
    
    return count

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")
