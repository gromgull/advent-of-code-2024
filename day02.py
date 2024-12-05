import fileinput

data = [ [int(x) for x in row.split()] for row in fileinput.input() ]

def sign(i):
    if i>0: return 1
    if i<0: return -1
    return 0

def safe(row):
    dir = None
    prev = row[0]

    for x in row[1:]:
        r = prev - x
        if r == 0 or abs(r) > 3 :
            return False
        r = sign(r)
        if dir is not None:
            if dir != r:
                return False
        else:
            dir = r
        prev = x

    return True

def safe2(row):

    if safe(row): return True

    for i in range(len(row)):
        if safe(row[:i]+row[i+1:]): return True

    return False


print(len([row for row in data if safe(row)]))
print(len([row for row in data if safe2(row)]))
