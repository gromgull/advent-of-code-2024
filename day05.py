import fileinput
from collections import defaultdict
from functools import cmp_to_key

data = list(fileinput.input())

split = data.index('\n')
part1 = [ line.strip().split('|') for line in data[:split] ]
orderings = defaultdict(list)
for p1,p2 in part1:
    orderings[p1].append(p2)

pages = [ line.strip().split(',') for line in data[split+1:] ]

def ok(ps):

    for i,p1 in enumerate(ps):
        for p2 in ps[i:]:
            if p1 in orderings.get(p2, []):

                print(i,p1,p2)
                return False
    return True

print(sum([ int(p[len(p)//2]) for p in pages if ok(p) ]))


def cmp(p1,p2):

    if p1 in orderings[p2]: return 1
    if p2 in orderings[p1]: return -1
    return 0


not_ok = [ sorted(p, key=cmp_to_key(cmp)) for p in pages if not ok(p) ]
print(sum(int(p[len(p)//2]) for p in not_ok))
