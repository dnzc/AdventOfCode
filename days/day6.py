def solve1(lines):
    count=0
    asdf = '\n'.join(lines).split("\n\n")
    for ans in asdf:
        count+=len(list(set(''.join(ans.split()))))
    return count

def solve2(lines):
    count=0
    asdf = '\n'.join(lines).split("\n\n")
    for ans in asdf:
        everyone=ans.split("\n")[0]
        for i in ans.split("\n"):
            new=""
            for char in everyone:
                if char in i:
                    new+=char
            everyone=new
        print(everyone)
        count+=len(everyone)
    return count

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")