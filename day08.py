from collections import defaultdict
import fileinput
from itertools import combinations

data = [ list(line.strip()) for line in fileinput.input() ]

h = len(data)
w = len(data[0])

antennas = defaultdict(list)

for y,line in enumerate(data):
    for x,c in enumerate(line):
        if c == '.': continue
        antennas[c].append((x,y))

anodes = defaultdict(list)

for c in antennas:
    for (ax,ay),(bx,by) in combinations(antennas[c], 2):
        dx = ax-bx
        dy = ay-by

        anodes[c] += [ (ax+dx, ay+dy),
                       (bx-dx, by-dy) ]


# for c in anodes:
#     for x,y in anodes[c]:
#         if x<0 or y<0 or x>=w or y>=h: continue
#         data[y][x] = '#'


# for line in data:
#     print(''.join(line))

all_anodes = set((x,y) for c in anodes for (x,y) in anodes[c]  )
print(len([1 for x,y in all_anodes if not (x<0 or y<0 or x>=w or y>=h) ]))

anodes = []
for c in antennas:
    for (ax,ay),(bx,by) in combinations(antennas[c], 2):
        dx = ax-bx
        dy = ay-by

        anodes.append((ax,dx,ay,dy))

res = set()
for x in range(w):
    for y in range(h):
        for ax,dx,ay,dy in anodes:
            if ((x-ax) % dx) == 0 and ay + ((x-ax) // dx) * dy == y:
                res.add((x,y))
                break

print(len(res))
