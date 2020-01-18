#!/usr/bin/env python
import sys

CG_ASP =   sys.argv[1]
OD1_ASP =  sys.argv[2]
OD2_ASP =  sys.argv[3]
SG_CYI_1 = sys.argv[4]
SG_CYI_2 = sys.argv[5]


f_obj = open('steep_run.inp', 'w')

with open('steep.inp', 'r') as input_file:
     for lines in input_file:
         line = lines.split(' ')
         if line[0] == './mutated_fast_evb.pdb\n':
            line[0] = sys.argv[6] + '\n'
            f_obj.writelines(' '.join(line))
         elif 'addbond' in line and '3846' in line:
            line[line.index('addbond')+2] = SG_CYI_1
            line[line.index('addbond')+3] = SG_CYI_2 +'\n'
            f_obj.writelines(' '.join(line))
         elif 'file_nm' in line:
            line[line.index('mutated_fast_evb.pdb\n')] = sys.argv[6] + '\n'
            f_obj.writelines(' '.join(line))
	 else:
            f_obj.writelines(' '.join(line))

f_obj.close()

