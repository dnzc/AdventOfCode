def solve1(lines):
    cards1 = [int(i) for i in '\n'.join(lines).split("\n\n")[0].split("\n")[1:]]
    cards2 = [int(i) for i in '\n'.join(lines).split("\n\n")[1].split("\n")[1:]]
    while True:
        if len(cards1)==0:
            return sum((a+1)*b for a,b in enumerate(cards2[::-1]))
        if len(cards2)==0:
            return sum((a+1)*b for a,b in enumerate(cards1[::-1]))

        c1 = cards1.pop(0)
        c2 = cards2.pop(0)
        if c1<c2:
            cards2.extend([c2,c1])
        elif c2<c1:
            cards1.extend([c1,c2]) 

def solve2(lines):
    cards1 = [int(i) for i in '\n'.join(lines).split("\n\n")[0].split("\n")[1:]]
    cards2 = [int(i) for i in '\n'.join(lines).split("\n\n")[1].split("\n")[1:]]

    def score(cards):
        return sum((a+1)*b for a,b in enumerate(cards[::-1]))

    def game(cards1, cards2):
        seen = []
        while True:
            if [cards1,cards2] in seen:
                return (1, score(cards1))
            seen.append([list(cards1),list(cards2)])

            c1 = cards1.pop(0)
            c2 = cards2.pop(0)

            if len(cards1)>=c1 and len(cards2)>=c2:
                a = list(cards1[:c1])
                b = list(cards2[:c2])
                if game(a,b)[0] == 1:
                    cards1.extend([c1,c2]) 
                else:
                    cards2.extend([c2,c1]) 
            else: 
                if c1<c2:
                    cards2.extend([c2,c1])
                else:
                    cards1.extend([c1,c2]) 
                
            if len(cards1)==0:
                return (2, score(cards2))
            if len(cards2)==0:
                return (1, score(cards1))

    return game(cards1,cards2)[1]

lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")
