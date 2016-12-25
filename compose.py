#!/c/Python27/python
import sys
#import itertools
import re

f = {}
g = {}
command = None
mode = 'read';
file1 = open(sys.argv[1])
for line in file1:
    if mode=='read':
        command = str(line.strip())
        mode = 'parse'
    elif mode == 'parse':
        n = line.strip().split()
        if n[0] == 'None':
            f[command] = set([None])
            mode = 'read'
            continue
        f[command] = set(n)
        mode = 'read'

file2 = open(sys.argv[2])
for line in file2:
    if mode=='read':
        command = str(line.strip())
        mode = 'parse'
    elif mode == 'parse':
        n = line.strip().split()
        if n[0] == 'None':
            g[command] = set([None])
            mode = 'read'
            continue
        g[command] = set(n)
        mode = 'read'

g['ACT'] = g['IN'].union(g['INT']).union(g['OUT']) - set([None])

#validation before composition
if not f['INT'].isdisjoint(g['ACT']) or not f['OUT'].isdisjoint(g['OUT']):
    print 'Automatons are not composable'
    exit()

h = {}
h['OUT'] = f['OUT'].union(g['OUT'])
h['INT'] = f['INT'].union(g['INT'])
h['IN'] = f['IN'].union(g['IN']) - h['OUT']
#h['START'] = set(itertools.product(f['START'],g['START']))
#h['STATES'] = set(itertools.product(f['STATES'],g['STATES']))
h['STATES'] = {(X,Y) for X in f['STATES'] for Y in g['STATES']}
h['START'] = {(X,Y) for X in f['START'] for Y in g['START']}

for key, val in h.iteritems():
    print key
    for item in val:
        if key == 'STATES' or key == 'START':
            print re.sub(r'\W', "", str(item)),
        else:
            print item,
    print
