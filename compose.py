#!/c/Python27/python
import sys
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

ft = {}
for item in f['TRANS']:
    sp = item.split(',')
    ft[sp[0]+">"+sp[1]] = sp[2]

gt = {}
for item in g['TRANS']:
    sp = item.split(',')
    gt[sp[0]+">"+sp[1]] = sp[2]


g['ACT'] = g['IN'].union(g['INT']).union(g['OUT']) - set([None])

#validation before composition
if not f['INT'].isdisjoint(g['ACT']) or not f['OUT'].isdisjoint(g['OUT']):
    print 'Automatons are not composable'
    exit()

h = {}
h['OUT'] = f['OUT'].union(g['OUT'])
h['INT'] = f['INT'].union(g['INT'])
h['IN'] = f['IN'].union(g['IN']) - h['OUT']
h['STATES'] = {(X,Y) for X in f['STATES'] for Y in g['STATES']}
h['START'] = {(X,Y) for X in f['START'] for Y in g['START']}
h['TRANS'] = set()
h['ACT'] = h['IN'].union(h['INT']).union(h['OUT']) - set([None])

for act in h['ACT']:
    for state in h['STATES']:
        result = re.sub(r'\W',"",str(state))+","+act+","
        push = False
        change = re.sub(r'\W',"",str(state))
        if re.sub(r'\W',"",str(state))[:-2]+">"+act in ft:
            change = change.replace(change[:-2],ft[re.sub(r'\W',"",str(state))[:-2]+">"+act])
            push = True
        if re.sub(r'\W',"",str(state))[-2:]+">"+act in gt:
            change = change.replace(change[-2:],gt[re.sub(r'\W',"",str(state))[-2:]+">"+act])
            push = True
        if push == True:
            result += change
            h['TRANS'].add(result)

for key, val in h.iteritems():
    print key
    for item in val:
        if key == 'STATES' or key == 'START':
            print re.sub(r'\W', "", str(item)),
        else:
            print item,
    print
