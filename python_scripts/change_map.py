#!/usr/bin/env python

with open('kemp_evb_run.inp', 'r') as file_obj1:
     for line in file_obj1:
         line = line.split()
         if len(line)> 7 and line[0] == 'Hr':
#            print('from kemp_evb_run.inp')
#            print(line)
            n1 = line[3]
            n2 = line[4]
            n3 = line[5]
#            print(n1, n2, n3)

collect_line = []

with open('../map_kemp_evb_run.inp', 'r') as file_obj2:
     for line in file_obj2:
         line = line.split()
#         print(line)
         if len(line)> 7 and line[0] == 'Hr':
#            print(line)
            line[3] = n1
            line[4] = n2
            line[5] = n3
#            print(line)
            collect_line.append(line)
         else: 
            collect_line.append(line)

file_write = open('map_kemp_evb_run.inp', 'w')

for f in range(len(collect_line)):
    file_write.write(' '.join(collect_line[f])+'\n')

file_write.close()
