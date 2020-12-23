def solve1(lines):
    cups = list(map(int,lines[0]))
    pos = 0
    for _ in range(100):
        pickup = (cups*2)[pos+1:pos+4]
        curcup = cups[pos]
        asdf = []
        for i in pickup:asdf.append(cups.pop(cups.index(i)))
        nextcup = cups[(cups.index(curcup)+1)%len(cups)]
        destinationcup = int(curcup)-1
        while destinationcup not in cups:
            destinationcup-=1
            if destinationcup<min(cups):
                destinationcup=max(cups)
                break
        cups = cups[:cups.index(destinationcup)+1]+asdf+cups[cups.index(destinationcup)+1:]
        pos = cups.index(nextcup)
        pos%=len(cups)
    return ''.join(map(str,(cups*2)[cups.index(1)+1:cups.index(1)+9]))
        
def solve2(lines):
    class Node:
        def __init__(self,next,val):
            self.next = next
            self.val = val

    cups = list(map(int,lines[0]))

    nodes = [Node(None, i) for i in range(1,1000001)]
    for i in range(len(cups)):
        nodes[i].val = cups[i]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    nodes[-1].next = nodes[0]

    nodes = {i.val:i for i in nodes}

    curcup = nodes[cups[0]]
    for _ in range(10000000):
        pickup = curcup.next
        curcup.next = pickup.next.next.next
        destinationcup = curcup.val
        while destinationcup in [curcup.val, pickup.val, pickup.next.val, pickup.next.next.val]:
            destinationcup-=1
            if destinationcup==0:
                destinationcup = 1000000
        pickup.next.next.next = nodes[destinationcup].next
        nodes[destinationcup].next = pickup
        curcup = curcup.next
    
    return nodes[1].next.val * nodes[1].next.next.val

lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")