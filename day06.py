import fileinput
from copy import deepcopy

data = [ list(line.strip()) for line in fileinput.input() ]

w = len(data[0])
h = len(data)

for y in range(h):
    for x in range(w):
        if data[y][x] == '^':
            break
    else:
        continue
    break

ix = x
iy = y
themap = deepcopy(data)

d = 0

delta = [ (0,-1), (1,0), (0,1), (-1,0) ]

dx,dy = delta[d]

while True:
    themap[y][x] = 'X'

    if x+dx>=w or y+dy>=h or x+dx<0 or y+dy<0: break

    while themap[y+dy][x+dx] == '#':
        d = (d+1) % 4
        dx, dy = delta[d]

    x += dx
    y += dy

#for line in data:
#    print(''.join(line))

print(sum(len([x for x in line if x == 'X']) for line in themap))

dir = [ 1,2,4,8 ]

data[iy][ix] = '.'

for y in range(h):
    for x in range(w):
        if data[y][x] == '.': data[y][x] = 0


def test(ox,oy):
    themap = deepcopy(data)
    themap[oy][ox] = '#'

    x = ix
    y = iy

    d = 0
    dx,dy = delta[d]

    while True:

        if themap[y][x] & dir[d]:
            return 1

        themap[y][x] |= dir[d]

        if x+dx>=w or y+dy>=h or x+dx<0 or y+dy<0:
            return 0

        while themap[y+dy][x+dx] == '#':
            d = (d+1) % 4
            dx, dy = delta[d]

        x += dx
        y += dy


print(sum( test(x,y) for x in range(w) for y in range(h) if not (x == ix and y == iy) and data[y][x] == 0 ))
