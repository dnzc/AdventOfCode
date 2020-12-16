def solve1(lines):
    lines = '\n'.join(lines).split("\n\n")
    nums = []
    for asdf in lines[0].split():
        if "-" in asdf:
            for i in range(int(asdf.split("-")[0]), int(asdf.split("-")[1])+1):
                nums.append(i)
    nums = sorted(list(set(nums)))
    total=0
    for asdf in lines[2].split("\n"):
        if "," in asdf:
            for i in map(int,asdf.split(",")):
                if i not in nums:total+=i
    return total 

def solve2(lines):
    lines = '\n'.join(lines).split("\n\n")
    nums = []
    for asdf in lines[0].split():
        if "-" in asdf:
            for i in range(int(asdf.split("-")[0]), int(asdf.split("-")[1])+1):
                nums.append(i)
    nums = sorted(list(set(nums)))

    tickets = []
    for asdf in lines[2].split("\n")[1:]:
        valid=True
        for i in map(int,asdf.split(",")):
            if i not in nums:
                valid = False
                break
        if valid: tickets.append(list(map(int,asdf.split(","))))

    ranges={}
    for line in lines[0].split("\n"):
        vals=[]
        name = line.split(": ")[0]
        for i in line.split(": ")[1].split():
            if "-" in i:
                for j in range(int(i.split("-")[0]), int(i.split("-")[1])+1):vals.append(j)
        ranges[name] = vals

    asdf = {}

    for name in ranges.keys():
        for i in range(len(tickets[0])):
            if all(j[i] in ranges[name] for j in tickets):
                try:
                    asdf[name].append(i)
                except KeyError:
                    asdf[name] = [i]

    print(asdf)
    # not going to lie in the real thing i did it manually from here since i could backtrack from seeing that the xth field has x possible values so you can find the one with one possible value, which tells you the one with two, which tells you the one with three etc.
    # so below is added code to automate that process

    q = sorted(asdf, key=lambda k: len(asdf[k]))
    final = {}
    seen = []
    for i in q:
        for a in asdf[i]:
            if a not in seen:
                final[i] = a
                seen.append(a)
                break
    w = [final[i] for i in final.keys() if "departure" in i]
    myticket = list(map(int,lines[1].split("\n")[1].split(",")))
    total = 1
    for i in w:total*=myticket[i]
    return total

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")