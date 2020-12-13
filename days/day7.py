import re

def solve1(lines):
    
    graph = {}

    for line in lines:
        neighbours = []
        for asdf in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            neighbours.append(asdf[1])
        graph[re.match(r'(.+?) bags c', line)[1]] = neighbours
    # print(graph)

    valid = [["shiny gold"]]
    for i in range(69):
        newvalid = []
        for node in graph.keys():
            if any(j in graph[node] for j in valid[-1]):
                newvalid.append(node)
        valid.append(newvalid)
    
    asdf = []
    for v in valid:
        for i in v:asdf.append(i)
    
    x=list(set(asdf))
    # print(x)
    return len(x)-1

def solve2(lines):
    
    graph = {}

    for line in lines:
        neighbours = []
        for n, neighbour in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            neighbours.append([neighbour, int(n)])
        graph[re.match(r'(.+?) bags c', line)[1]] = neighbours
    # print(graph)

    def getcost(bag):
        total = 0
        for i in graph[bag]:
            total += (getcost(i[0])+1)*i[1]
        return total

    return getcost("shiny gold")

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")