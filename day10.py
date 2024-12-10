import fileinput

data = [ [ int(x) for x in line.strip() ] for line in fileinput.input() ]

h = len(data)
w = len(data[0])

trail_heads = [ (y,x) for x in range(w) for y in range(h) if data[y][x] == 0 ]

def explore(y,x,n=0):
    if x < 0 or x >= w or y < 0 or y >= h:
        return []
    if data[y][x] != n: return []

    #print(x,y,n,data[y][x])
    if n == 9: return [(x,y)]

    return explore( y+1, x, n+1) + explore(y-1, x, n+1) + explore(y, x+1, n+1) + explore(y, x-1, n+1)

res = [ len(set(explore(*t))) for t in trail_heads ]
print(sum(res))

res = [ len(explore(*t)) for t in trail_heads ]
print(sum(res))
