#!/usr/bin/env python
import sys
import re
import os.path
import subprocess
import shutil

def mod_pdb(old_pdb, new_pdb): # old_pdb = E0045N_conf1.pdb
    if new_pdb == pdb_list[0]:
       print('old_pdb should be', old_pdb)
       already_mutated = '0'
    else:
       already_mutated = old_pdb
    jst_list = new_pdb.split('.')[0].split('_') 
    res_info = mysplit(jst_list[0])
    resnum = res_info[1]
    resname = amino_dic[res_info[2]]
    conf_name = type_confor[jst_list[1]]
    print(conf_name)
    if os.path.isfile('X_XXX_X.inp'):
       mutation_demo_file = 'X_XXX_X.inp'
    else:
       print('X_XXX_X.inp does not exist in the current folder')
       sys.exit(1)
    subprocess.call([file_path + 'multi_mutated_pdb.bash', 'X_XXX_X.inp', conf_name, resnum, resname, already_mutated, old_pdb, new_pdb])

a = sys.argv[1]

#a = 'E0045N_conf2_N0087S_conf2_F0088H_conf2_M0265F_conf2_A0273W_conf2_F0274R_conf3'

if len(sys.argv) < 2:
   print("GIVE E0045N_conf2_N0087S_conf2_F0088H_conf2... like pdb name")
if len(sys.argv) == 2:
   print("GIVE initial pdb file name to start first mutation")
   print("Can't generate the 'first_pdb'")

initial_pdb = sys.argv[2]

file_path= os.path.abspath(".")+"/"

amino_dic = {'G': 'GLY', 'A': 'ALA', 'S': 'SER', 'T': 'THR', 'C': 'CYS', 'V': 'VAL', 'L': 'LEU', 'I': 'ILE', 'M': 'MET', 'P': 'PRO', 'F': 'PHE', 'Y': 'TYR', 'W': 'TRP', 'D': 'ASP', 'E': 'GLU', 'N': 'ASN', 'Q': 'GLN', 'H': 'HIS', 'K': 'LYS', 'R': 'ARG'}

type_confor = {'conf1': 'mutate_center1.pdb', 'conf2': 'mutate_center2.pdb', 'conf3': 'mutate_closest_center.pdb'}

def mysplit(string):
    match = re.match(r"([A-Z]+)([0-9]+)([A-Z]+)", string)
    if match:
       items = match.groups()
    return items
#print(mysplit('E0045N'))

list_a = a.split('_')

if len(list_a) != 6:
    print('check the input string')
else:
    first_pdb = '_'.join(list_a[:2])+'.pdb'
    second_pdb = '_'.join(list_a[2:4])+'.pdb'
    third_pdb = '_'.join(list_a[4:6])+'.pdb'
#    forth_pdb = '_'.join(list_a[6:8])+'.pdb'
#    fifth_pdb = '_'.join(list_a[8:10])+'.pdb'
#    sixth_pdb = '_'.join(list_a[10:12])+'.pdb'
    pdb_list = [first_pdb, second_pdb, third_pdb]

print(pdb_list)

for f in range(len(pdb_list)):
    if f == 0:
       mod_pdb(initial_pdb, pdb_list[f])
    else:
       mod_pdb(pdb_list[f-1], pdb_list[f])

shrt_conf = {'conf1': 'c1', 'conf2': 'c2', 'conf3': 'c3'}
final_name = []
for i in range(len(pdb_list)):
    current_str = pdb_list[i].split('.')[0].split('_')
    shrt = shrt_conf[current_str[1]]
    shrt_tuple = mysplit(current_str[0])
    shrt_str = shrt_tuple[0]+shrt_tuple[1].lstrip('0')+shrt_tuple[2]+shrt 
    final_name.append(shrt_str)
final_pdb = '_'.join(final_name)+'.pdb'
print('final modified pdb is', pdb_list[f])
shutil.copy2(file_path+pdb_list[f], file_path+final_pdb)


