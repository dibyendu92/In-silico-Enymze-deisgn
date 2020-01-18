#!/usr/bin/env python

import os

abs_path = os.path.abspath('.')

#folder_name = os.path.split(os.path.dirname(abs_path))[1]
folder_name = os.path.split(abs_path)[1]
#print(folder_name)

act_ene = None
LRA = None
LRA_Total = None
search1 = False
search2 = False
with open('map_kemp_evb_run.out', 'r') as input_file:
     for lines in input_file:
         line = lines.strip().split(':')
         line_equal = lines.split('=')[0].strip()
         line_pattern = lines.strip()
         if line_pattern == 'EVB Electrostatic LRA Breakdown:':
            search1 = True
         if search1:
            if len(line_equal)> 0 and line_equal == 'Total':
               LRA = line[0].split()[5] 
               search1 = False 

         if line_pattern == 'EVB total LRA Breakdown:':
            search2 = True
         if search2:
#            print(line_equal)
            if len(line_equal)> 0 and line_equal == 'Total':
               LRA_Total= line[0].split()[3]
               search2 = False
               
#            print(line_pattern)
         if line[0] == 'The dG#':
            act_ene = float(line[1].strip()) 
print folder_name, act_ene, LRA_Total
