import fileinput
from collections import Counter

data = [ l.strip().split() for l in fileinput.input() ]
X = sorted([ int(row[0]) for row in data ])
Y = sorted([ int(row[1]) for row in data ])

print(sum(abs(x-y) for x,y in zip(X,Y)))

Y = Counter(Y)

print(sum(x * Y[x] for x in X))
