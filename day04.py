import fileinput

data = [ line.strip() for line in fileinput.input() ]

h = len(data)
w = len(data[0])


def search(x, y, dx, dy, target):
    if not target: return 1
    if x == w: return 0
    if x < 0: return 0
    if y == h: return 0
    if y < 0: return 0

    if data[y][x] == target[0]:
        return search(x+dx, y+dy, dx, dy, target[1:])

    return 0

def find(target):

    res = 0
    for x in range(w):
        for y in range(h):
            for dx in (-1,0,1):
                for dy in (-1, 0, 1):
                    if dx or dy:
                        res += search(x,y,dx,dy,target)

    return res


print(find('XMAS'))
