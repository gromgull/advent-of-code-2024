import fileinput
from collections import namedtuple

data = list(fileinput.input())[0].strip()
data += '0'

compressed = [ (int(data[i]), int(data[i+1]) ) for i in range(0,len(data),2) ]

data = []
for i, (f,e) in enumerate(compressed):
    data += [i]*f
    data += ['.']*e

# print(''.join(str(c) for c in data))

free = [ i for i,c in enumerate(data) if c == '.' ]

for i in reversed(range(len(data))):
    if not free: break
    if free[0]>len(data): break
    if i == free[0]: break
    if data[i] != '.':
        data[free.pop(0)] = data.pop(i)

# print(''.join(str(c) for c in data))

print(sum(i*c for i,c in enumerate(data) if c!='.'))

File = namedtuple('File', ['index', 'len', 'id'])
Free = namedtuple('Free', ['index', 'len'])
frees = []
files = []
data = []
n = 0
for i, (f,e) in enumerate(compressed):
    files.append(File(n, f, i))
    n += f
    frees.append(Free(n, e))
    n += e
    data += [i]*f
    data += ['.']*e

print(''.join(str(c) for c in data))

for i, file in reversed(list(enumerate(files))):
    for j, free in enumerate(frees):
        if free.len >= file.len and free.index<file.index:
            #print(f'moving {file.id} to {free.index}', file, free)
            files[i] = File(free.index, file.len, file.id)
            frees[j] = Free(free.index+file.len, free.len-file.len)
            frees.append(Free(file.index, file.len))

            break

print('-'*20)
data = []
for t in sorted(files+frees, key=lambda x: x.index):
    data += ['.' if isinstance(t, Free) else t.id]*t.len

print(''.join(str(c) for c in data))

print(sum(i*c for i,c in enumerate(data) if c!='.'))
