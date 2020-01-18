#!/usr/bin/env python

import sys
import re
import os

def find_serial(pdb_file_name, start, residue, string):
    with open(pdb_file_name, 'r') as inputfile:
         for line in inputfile:
             line = line.strip()
             resnum = line[22:26].strip()
             resname = line[17:20]
             if resnum == str(start) and resname == residue:
                if line[12:16].strip() == string:
                    serial = line[6:11]
                    return serial
                else:
                    pass
             else:
                pass
#         return None

def mysplit(string):
    match = re.match(r"([A-Z]+)([0-9]+)([A-Z]+)", string)
    if match:
       items = match.groups()
    return items



pdb_file_name = os.path.basename(sys.argv[1])
seq_file_path = os.path.abspath('.')+'/'
already_mutated = sys.argv[2]
#print("from binding_input", already_mutated)
pdb_list = ['mutate_center1.pdb', 'mutate_center2.pdb', 'mutate_closest_center.pdb']

if already_mutated == '0':
   search_pattern1 = pdb_file_name.split("_")[0]
#   print(1, search_pattern1)
   search_pattern2 = pdb_file_name.split("_")[1]
else:
   search_pattern1 = pdb_file_name.split("_")[0]+'_'+pdb_file_name.split("_")[1]+' '+pdb_file_name.split("_")[2]
   search_pattern2 = pdb_file_name.split("_")[3]
#   print(2, search_pattern2)
if search_pattern2 == 'conf1.pdb':
   search_pattern2 = pdb_list[0]
elif search_pattern2 == 'conf2.pdb':
   search_pattern2 = pdb_list[1]
else:
   search_pattern2 = pdb_list[2]

search_pattern = search_pattern2 + " " + search_pattern1
print(search_pattern)

#print(serach_pattern1)
#print(search_pattern2)

line_list = []

search =  False
with open(seq_file_path + 'seq.txt', 'r') as input_file:
     for line in input_file:
         line_list.append(line.strip())
#print(line_list[0])
for i in range(len(line_list)):
    if line_list[i] == search_pattern:
 #      print(line_list[i+2])
       p=re.compile('WDV')
       for m in p.finditer(line_list[i+2].strip()):
           start = m.start() # NOTE that the fisrt residue is NT6 so m.start() == position of D
 #          print(line_list[i+2].strip()[m.start():m.end()])
       q=re.compile('CLNVQSC')
       for n in q.finditer(line_list[i+2].strip()):
           SG_start = n.start()-1
           SG_end = n.end()-2 
#print(SG_start, SG_end)
serial_dic = {}

serial_dic['CG'] = find_serial(pdb_file_name, start, 'ASP', 'CG')
serial_dic['OD1'] = find_serial(pdb_file_name, start, 'ASP', 'OD1')
serial_dic['OD2'] = find_serial(pdb_file_name, start, 'ASP', 'OD2')
serial_dic['SG1'] = find_serial(pdb_file_name, SG_start, 'CYI', 'SG')
serial_dic['SG2'] = find_serial(pdb_file_name, SG_end, 'CYI', 'SG')

#CG_serial = serial_dic['CG']
#OD1_serial = serial_dic['OD1']
#OD2_serial = serial_dic['OD2']
#SG1_serial = serial_dic['SG1']
#SG2_serial = serial_dic['SG2']

print(serial_dic['SG1'], serial_dic['SG2'])

ionres_check = mysplit(search_pattern1)[1].strip('0')

write_inp = open(pdb_file_name.split('.')[0]+'_bind.inp', 'w')

with open('fast_TS_bind.inp', 'r') as inputfile:
     for lines in inputfile:
         line = lines.split(' ')
#         print(line)
         if 'addbond' in line:
            if line[-1] == '3937\n':
               print(line)
               line[-1] = serial_dic['SG2']+'\n'
               line[-2] = serial_dic['SG1']
               print(line)
         if 'ionres' in line:
            if ionres_check == line[-1].strip():
               line[0] = ''
#               print(line)
         if 'reg1_atm' in line:
#            print(line)
            if '1967' in line:
               line[line.index('1967')] = serial_dic['CG']
               line[line.index('1969\n')] = serial_dic['OD2']+'\n'
#               print(line)
         if ('setcrg' and '1967') in line:
            line[line.index('1967')] = serial_dic['CG']
         if ('setcrg' and '1968') in line:
            line[line.index('1968')] = serial_dic['OD1']
         if ('setcrg' and '1969') in line:
            line[line.index('1969')] = serial_dic['OD2']
#            print(line)
         if 'fast_TS.pdb\n' in line:
            line[line.index('fast_TS.pdb\n')] = pdb_file_name + '\n'
         write_inp.write(' '.join(line))
write_inp.close()
#print(serial_diac)
