import fileinput
from dataclasses import dataclass
from itertools import groupby

@dataclass
class vec:
    area: int
    perimeter: int

    def __add__(self, other):
        return vec(self.area+other.area, self.perimeter+other.perimeter)

    def price(self): return self.area * self.perimeter

data = [ list(line.strip()) for line in fileinput.input() ]

h = len(data)
w = len(data[0])

visited = [[ 0 for _ in range(w) ] for _ in range(h) ]

def explore(x,y,c):

    if x<0 or x>=w or y<0 or y>=h: return vec(0,1)

    if data[y][x] != c: return vec(0,1)

    if visited[y][x]: return vec(0,0)

    visited[y][x] = 1

    return vec(1,0) + explore(x+1, y, c) + explore(x-1, y, c) + explore(x, y-1, c) + explore(x, y+1, c)



res = [ explore(x,y,data[y][x]) for x in range(w) for y in range(h) if not visited[y][x] ]

print(sum(x.price() for x in res ))

@dataclass
class vec2:
    area: int
    perimeter: list

    def __add__(self, other):
        return vec2(self.area+other.area, self.perimeter+other.perimeter)

    def edges(self):
        # sort by direction, and then by x,y or y,x depending on direction
        p = sorted(self.perimeter, key=lambda x: x[2:] + ( (x[1],x[0]) if x[3] else (x[0],x[1])))
        res = 0
        for k, g in groupby(p, key=lambda x: x[2:]):
            g = list(g)
            dist = [ abs(g[i-1][0]-g[i][0])+abs(g[i-1][1]-g[i][1]) for i in range(1,len(g)) ]
            res += 1 + len([ 1 for d in dist if d>1 ])
        return res

    def price(self): return self.area * self.edges()

visited = [[ 0 for _ in range(w) ] for _ in range(h) ]

def explore2(x,y,c,dx=0,dy=0):
    x += dx
    y += dy

    if x<0 or x>=w or y<0 or y>=h: return vec2(0,[(x,y,dx,dy)])

    if data[y][x] != c: return vec2(0,[(x,y,dx,dy)])

    if visited[y][x]: return vec2(0,[])

    visited[y][x] = 1

    return vec2(1,[]) + explore2(x, y, c, 1) + explore2(x, y, c, -1) + explore2(x, y, c, 0, -1) + explore2(x, y, c, 0, 1)

res = [ explore2(x,y,data[y][x]) for y in range(h) for x in range(w) if not visited[y][x] ]

#print([r.edges() for r in res])

print(sum(x.price() for x in res ))
