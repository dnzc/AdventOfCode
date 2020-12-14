def solve1(lines):
    mask = ""
    mem = {}
    for line in lines:
        if line.split()[0] == "mask":
            mask = line.split()[2]
        else:
            asdf = line.split()
            addr = int(asdf[0][4:-1])
            val = list(str(bin(int(asdf[2])))[2:].zfill(36))
            for i in range(36):
                if mask[i] == "1": val[i] = "1"
                elif mask[i] == "0": val[i] = "0"
            val = int(''.join(val),2)
            mem[addr] = val
    return sum(mem.values())

def solve2(lines):
    mask = ""
    mem = {}
    for line in lines:
        if line.split()[0] == "mask":
            mask = line.split()[2]
        else:
            asdf = line.split()
            addr = list(str(bin(int(asdf[0][4:-1])))[2:].zfill(36))
            val = int(asdf[2])
            for i in range(36):
                if mask[i] == "1": addr[i] = "1"
                if mask[i] == "X": addr[i] = "0"
            addr = ''.join(addr)
            q = [2**(35-i) for i in range(36) if mask[i] == "X"]
            for i in range(2**len(q)):
                w = list(map(int,list(str(bin(i))[2:].zfill(len(q)))))
                e = [j for j in q]
                for j in range(len(e)): e[j]*=w[j]
                r = int(addr,2)+sum(e)
                mem[r] = val
    return sum(mem.values())

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")