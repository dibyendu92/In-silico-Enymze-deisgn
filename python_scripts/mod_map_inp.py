#!/usr/bin/env python
import sys

CG_ASP =   sys.argv[1]
OD1_ASP =  sys.argv[2]
OD2_ASP =  sys.argv[3]
SG_CYI_1 = sys.argv[4]
SG_CYI_2 = sys.argv[5]


f_obj = open('map_kemp_evb_run.inp', 'w')

with open('map_kemp_evb.inp', 'r') as input_file:
     for lines in input_file:
         line = lines.split(' ')
         if 'Hr' in line and 'OD2' in line:
            line[line.index('OD2')] = OD2_ASP
            f_obj.writelines(' '.join(line))
         else:
            f_obj.writelines(' '.join(line))

f_obj.close()

