# visual studio wasn't working with sys.stdin (lines too long so was adding its own newlines?) so changed input method

def solve1(lines):

    allergens = {}
    ingred = {}
    for line in range(len(lines)):
        for j in lines[line].split(" (contains ")[1][:-1].split(", "):
            try:
                allergens[j].append(line)
            except KeyError:
                allergens[j] = [line]
        for j in lines[line].split(" (contains ")[0].split():
            try:
                ingred[j].append(line)
            except KeyError:
                ingred[j] = [line]

    x=0
    for inglocs in ingred.values():
        for allergenlocs in allergens.values():
            if all(i in inglocs for i in allergenlocs) and len(inglocs)>len(allergenlocs):
              break                
        else:
            x += len(inglocs)
    return x

def solve2(lines):

    allergens = {}
    ingred = {}
    for line in range(len(lines)):
        for j in lines[line].split(" (contains ")[1][:-1].split(", "):
            try:
                allergens[j].append(line)
            except KeyError:
                allergens[j] = [line]
        for j in lines[line].split(" (contains ")[0].split():
            try:
                ingred[j].append(line)
            except KeyError:
                ingred[j] = [line]

    inert = []
    for ing in ingred.keys():
        for allergenlocs in allergens.values():
            if all(i in ingred[ing] for i in allergenlocs) and len(ingred[ing])>len(allergenlocs):
              break                
        else:
            inert.append(ing)
    for i in inert:
        del ingred[i]

    poss = {}
    for i in ingred.keys():
        x=[]
        for j in allergens.keys():
            if all(k in ingred[i] for k in allergens[j]) and len(ingred[i])>len(allergens[j]):
                x.append(j)
        poss[i] = x
    
    final = {}
    while True:
        for i in poss.keys():
            if len(poss[i])==1:
                final[i] = poss[i][0]
                break
        else: break
        newposs = {}
        for j in poss.keys():
            newposs[j] = [k for k in poss[j] if k!=poss[i][0]]
        del poss[i]
        poss = dict(newposs)


    return ','.join(sorted(final.keys(),key=lambda x:final[x]))



lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")
