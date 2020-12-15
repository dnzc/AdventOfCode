def solve1(lines):
    asdf = "\n".join(lines).split("\n\n")
    count=0
    for pw in asdf:
        if all(i in pw for i in "byr iyr eyr hgt hcl ecl pid".split()):count+=1
    return count

def solve2(lines):
    asdf = "\n".join(lines).split("\n\n")
    count=0
    for pw in asdf:
        valid=True
        if any(i not in pw for i in "byr iyr eyr hgt hcl ecl pid".split()):valid=False
        l = pw.split()
        for e in l:
            q = e.split(":")
            if q[0]=="byr":
                if not (all(i.isdigit() for i in q[1]) and 1920<=int(q[1])<=2002):valid=False
            elif q[0]=="iyr":
                if not (all(i.isdigit() for i in q[1]) and 2010<=int(q[1])<=2020):valid=False
            elif q[0]=="eyr":
                if not (all(i.isdigit() for i in q[1]) and 2020<=int(q[1])<=2030):valid=False
            elif q[0]=="hgt":
                if q[1][-2:]=="cm":
                    w = q[1].replace("cm","")
                    if not (all(i.isdigit() for i in w) and 150<=int(w)<=193):valid=False
                elif q[1][-2:]=="in":
                    w = q[1].replace("in","")
                    if not(all(i.isdigit() for i in w) and 59<=int(w)<=76):valid=False
                else:
                    valid=False
            elif q[0]=="hcl":
                if not(q[1][0]=="#" and all(i in "1234567890abcdef"for i in q[1][1:])):valid=False
            elif q[0]=="ecl":
                if not(any(q[1]==i for i in "amb blu brn gry grn hzl oth".split())):valid=False
            elif q[0]=="pid":
                if not(all(i.isdigit()for i in q[1]) and len(q[1])==9):valid=False

        if valid:count+=1

    return count

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")