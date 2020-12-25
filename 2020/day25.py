def solve1(lines):
    asdf = 1
    count=0
    while True:
        asdf*=7
        asdf%=20201227
        count+=1
        if asdf==int(lines[0]):
            break
    q=int(lines[1])
    asdf = 1
    for i in range(count):
        asdf*=q
        asdf%=20201227
    return asdf

lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
# print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")