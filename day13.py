import fileinput
import re

data = [ line.strip() for line in fileinput.input() ]

puzzles = [ data[i*4:i*4+3] for i in range(1+len(data)//4) ]

def parse(p):
    return [ list(map(int, re.findall('(?:X|Y).(\d+)', part))) for part in p ]

def solve(p):
    [[x1,y1],[x2,y2],[xt,yt]] = p

    b = (yt*x1-xt*y1)//(y2*x1-x2*y1)
    a = (xt-b*x2)//x1

    if a*x1 + b*x2 == xt and a*y1 + b*y2 == yt:
        return a,b


res = [solve(parse(p)) for p in puzzles]
res = [r for r in res if r ]
print(sum(a*3+b for a,b in res))

def add(p):
    p[2][0]+=10000000000000
    p[2][1]+=10000000000000
    return p

res = [solve(add(parse(p))) for p in puzzles]
res = [r for r in res if r ]
print(sum(a*3+b for a,b in res))
