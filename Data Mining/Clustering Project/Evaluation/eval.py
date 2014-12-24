from __future__ import print_function
from sklearn import metrics
import sys

label_dict = {}
with open('cluster.tsv') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        id, cno = line.split('\t')
        label_dict[int(id)] = int(cno)

expected_labels = []
actual_labels   = []

clusters = set()
num_lines = 0
with open(sys.argv[1]) as f:
    for line in f:
        data = line.strip().split()
        if not data or not data[0]: continue
        if data[0] == 'jobID:':
            id, cno = int(data[1]), int(data[3])
        elif data[0].count('.') == 1:
            id, cno = int(float(data[0])), int(data[1])
        elif not data[0].isdigit():
            #print(num_lines, line)
            continue
        else:
            if len(data) < 2:
                #print('WARNING: SH', data)
                continue
            elif not data[1].isdigit():
                if data[1][:8] == 'cluster-':
                    data[1] = data[1][8:]
                elif data[1][0] == 'C':
                    data[1] = data[1][1:]
                else:
                    print('ERROR', data)
                    exit(0)
            
            id, cno = map(int, data[:2])
        if id not in label_dict:
            #print('WARNING: NE', line)
            continue
        num_lines += 1
        if num_lines >= 16801:
            break
        clusters.add(cno)
        expected_labels.append(label_dict[id])
        actual_labels.append(cno)
        
        del label_dict[id]

print('%s %.3f %5d %5d' % (sys.argv[1], metrics.adjusted_rand_score(expected_labels, actual_labels), len(clusters), num_lines))