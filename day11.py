import fileinput
from functools import cache

data = [ int(x) for x in list(fileinput.input())[0].strip().split(' ') ]

@cache
def expand(x, n):
    if n == 0: return 1
    if x == 0: return expand(1, n-1)
    s = str(x)
    if len(s) % 2 == 0: return expand(int(s[:len(s)//2]), n-1) + expand(int(s[len(s)//2:]), n-1)
    return expand(x*2024, n-1)

res = [ expand(x, 25) for x in data ]

print(sum(res))

res = [ expand(x, 75) for x in data ]

print(sum(res))
