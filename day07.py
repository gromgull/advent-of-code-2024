import fileinput
import operator as op

data = [ line.strip().split(':') for line in fileinput.input() ]
data = [ (int(k), [int(n) for n in v.split()]) for k,v in data ]

ops = [ op.add, op.mul ]

def test(target, ns, val):

    if not ns:
        return int(target == val)

    return sum( test(target, ns[1:], op(val, ns[0])) for op in ops )

def tester(target, ns):
    return bool(test(target, ns[1:], ns[0]))

print(sum(v for v,ns in data if tester(v,ns)))

def combine(a,b):
    return int(str(a)+str(b))

ops.append(combine)

print(sum(v for v,ns in data if tester(v,ns)))
