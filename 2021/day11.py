def solve1(lines):
    borderval = -1000
    arr = [[[borderval, False]]*(len(lines[0])+2)]
    for line in lines:
        arr.append([[borderval, False]] + [[int(i), False] for i in line] + [[borderval, False]])
    arr.append([[borderval, False]]*(len(lines[0])+2))
    # print(arr)

    flashes = 0
    for _ in range(100):
        for y in range(1, len(arr) - 1):
            for x in range(1, len(arr[y]) - 1):
                arr[y][x][0] += 1
        while True:
            unchanged = True
            for y in range(1, len(arr) - 1):
                for x in range(1, len(arr[y]) - 1):
                    if arr[y][x][0] > 9:
                        arr[y][x] = [0, True]
                        flashes += 1
                        unchanged = False
                        for dy in [-1, 0, 1]:
                            for dx in [-1, 0, 1]:
                                if dx != 0 or dy != 0:
                                    if not arr[y+dy][x+dx][1]:
                                        arr[y+dy][x+dx][0] += 1
            if unchanged: break

        for y in range(1, len(arr) - 1):
            for x in range(1, len(arr[y]) - 1):
                arr[y][x][1] = False
    # print(arr)

    return flashes

def solve2(lines):
    borderval = -1000
    arr = [[[borderval, False]]*(len(lines[0])+2)]
    for line in lines:
        arr.append([[borderval, False]] + [[int(i), False] for i in line] + [[borderval, False]])
    arr.append([[borderval, False]]*(len(lines[0])+2))
    # print(arr)

    iteration = 0
    while True:
        iteration += 1
        for y in range(1, len(arr) - 1):
            for x in range(1, len(arr[y]) - 1):
                arr[y][x][0] += 1
        while True:
            unchanged = True
            for y in range(1, len(arr) - 1):
                for x in range(1, len(arr[y]) - 1):
                    if arr[y][x][0] > 9:
                        arr[y][x] = [0, True]
                        unchanged = False
                        for dy in [-1, 0, 1]:
                            for dx in [-1, 0, 1]:
                                if dx != 0 or dy != 0:
                                    if not arr[y+dy][x+dx][1]:
                                        arr[y+dy][x+dx][0] += 1
            if unchanged: break
        

        stop = True
        for y in range(1, len(arr) - 1):
            for x in range(1, len(arr[y]) - 1):
                if arr[y][x][0] != 0:
                    stop = False
                    break
            if not stop: break
        if stop: return iteration

        for y in range(1, len(arr) - 1):
            for x in range(1, len(arr[y]) - 1):
                arr[y][x][1] = False

    # print(arr)

    return flashes

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")