s=0
def solve1(lines):

    def decode(p):
        if len(p) < 8: return "", 0
        print("parsing:", p)
        ver = int(p[:3], 2)
        global s
        s += ver
        p_id = int(p[3:6], 2)
        p = p[6:]
        if p_id == 4:
            a = [p[i] for i in range(0, len(p), 5)].index('0')*5 + 5
            print("when parsing literal value, found subsection:", p[:a])
            o = ""
            for i in range(0, a, 5):
                o += p[:a][i+1:i+5]
            return p[a:], int(o, 2)
        else:
            l_id = p[0]
            p = p[1:]
            if l_id == "0":
                length = int(p[:15], 2)
                p = p[15:]
                subpackets = p[:length]
                while len(subpackets) > 0:
                    subpackets, x = decode(subpackets)
                return p[length:], 0
            else:
                numpackets = int(p[:11], 2)
                p = p[11:]
                for i in range(numpackets):
                    p, x = decode(p)
                return p, 0


    decode(''.join(bin(int(i, 16))[2:].zfill(4) for i in lines[0]))
    return s

def solve2(lines):

    def calc(p_id, data):
        a = int(p_id)
        if a == 0:
            return sum(data)
        elif a == 1:
            t = 1
            for i in data: t*=i
            return t
        elif a == 2:
            return min(data)
        elif a == 3:
            return max(data)
        elif a == 5:
            return int(data[0] > data[1])
        elif a == 6:
            return int(data[0] < data[1])
        elif a == 7:
            return int(data[0] == data[1])

    def decode(p):
        if len(p) < 8: return "", 0
        ver = int(p[:3], 2)
        p_id = int(p[3:6], 2)
        p = p[6:]
        if p_id == 4:
            a = [p[i] for i in range(0, len(p), 5)].index('0')*5 + 5
            o = ""
            for i in range(0, a, 5):
                o += p[:a][i+1:i+5]
            return p[a:], int(o, 2)
        else:
            data = []

            l_id = p[0]
            p = p[1:]
            if l_id == "0":
                length = int(p[:15], 2)
                p = p[15:]
                subpackets = p[:length]
                while len(subpackets) > 0:
                    subpackets, x = decode(subpackets)
                    data.append(x)
                return p[length:], calc(p_id, data)
            else:
                numpackets = int(p[:11], 2)
                p = p[11:]
                for i in range(numpackets):
                    p, x = decode(p)
                    data.append(x)
                return p, calc(p_id, data)

    return decode(''.join(bin(int(i, 16))[2:].zfill(4) for i in lines[0]))

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
# note: annoyingly, stdin line limited to 4096 bytes
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")