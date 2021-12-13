from itertools import permutations

def solve1(lines):
    t=0
    for line in lines:
        a = line.split(" | ")
        for i in a[1].split():
            if len(i) in [2, 3, 4, 7]: t+=1
    return t

def solve2(lines):
    t=0
    for line in lines:
        a = line.split(" | ")
        four = a[1].split()
        codes = a[0].split()
        for p in permutations("abcdefg"):
            d = {"abcdefg"[i] : p[i] for i in range(7)}
            decoded = []
            for i in codes: decoded.append(''.join(sorted(d[j] for j in i)))
            correct = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
            if all(j in correct for j in decoded):
                b = ""
                for i in four: b += str(correct.index(''.join(sorted(d[j] for j in i))))
                t += int(b)
    return t



import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")
