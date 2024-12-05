import sys
import re

with open(sys.argv[1]) as f:
    data = f.read()

print(sum([ int(a)*int(b) for a,b in re.findall(r'mul\((\d+),(\d+)\)', data) ]))


on = True
res = 0
for a,b,dont,do in re.findall(r'mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\))', data):

    if do: on = True
    elif dont: on = False
    elif on:
        res += int(a) * int(b)

print(res)
