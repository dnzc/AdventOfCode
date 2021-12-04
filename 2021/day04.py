def win(board):
    for row in board:
        if all(i[1] == -1 for i in row): return True
    for col in zip(*board):
        if all(i[1] == -1 for i in col): return True
    return False

def solve1(lines):
    a = list(lines)
    numbers = [*map(int, a.pop(0).split(","))]
    a.pop(0)
    b = '\n'.join(a).split("\n\n")
    boards = [ [list(map(lambda x: [int(x), int(x)],j.split())) for j in i.split("\n")] for i in b]

    for i in numbers:
        for x in range(len(boards)):
            for y in range(len(boards[x])):
                for z in range(len(boards[x][y])):
                    if boards[x][y][z][1] == i: boards[x][y][z][1] = -1

        for b in boards:
            if win(b):
                return i*sum(sum(i[0] for i in row if i[0]==i[1]) for row in b)

def solve2(lines):
    a = list(lines)
    numbers = [*map(int, a.pop(0).split(","))]
    a.pop(0)
    b = '\n'.join(a).split("\n\n")
    boards = [ [list(map(lambda x: [int(x), int(x)],j.split())) for j in i.split("\n")] for i in b]

    found = False
    for i in numbers:
        for x in range(len(boards)):
            for y in range(len(boards[x])):
                for z in range(len(boards[x][y])):
                    if boards[x][y][z][1] == i: boards[x][y][z][1] = -1

        if not found:
            states = [win(b) for b in boards]
            if states.count(0) == 1:
                found = True
                ind = states.index(0)
        elif win(boards[ind]):
            return i*sum(sum(i[0] for i in row if i[0]==i[1]) for row in boards[ind])



import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")