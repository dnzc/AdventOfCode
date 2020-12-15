def solve1(lines):
    nums = list(map(int,lines[0].split(",")))
    asdf = len(nums)
    toappend = 0
    seen = {nums[i]:[i] for i in range(len(nums))}
    for i in range(2020-asdf):
        if len(seen[nums[-1]]) == 1:
            toappend = 0
            seen[toappend].append(len(nums))
            nums.append(toappend)
        else:
            toappend = seen[nums[-1]][1] - seen[nums[-1]][0]
            nums.append(toappend)
            try:
                seen[toappend].append(len(nums)-1)
            except KeyError:
                seen[toappend] = [len(nums)-1]
        if len(seen[toappend])>2:
            seen[toappend].pop(0)
    return nums[-1]

def solve2(lines):
    nums = list(map(int,lines[0].split(",")))
    asdf = len(nums)
    toappend = 0
    seen = {nums[i]:[i] for i in range(len(nums))}
    for i in range(30000000-asdf):
        if len(seen[nums[-1]]) == 1:
            toappend = 0
            seen[toappend].append(len(nums))
            nums.append(toappend)
        else:
            toappend = seen[nums[-1]][1] - seen[nums[-1]][0]
            nums.append(toappend)
            try:
                seen[toappend].append(len(nums)-1)
            except KeyError:
                seen[toappend] = [len(nums)-1]
        if len(seen[toappend])>2:
            seen[toappend].pop(0)
    return nums[-1]

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")