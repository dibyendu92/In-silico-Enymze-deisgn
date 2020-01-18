#!/usr/bin/env python

import re
import subprocess
import os
import sys

pdb_file_name = sys.argv[1]
already_mutated = pdb_file_name.split('_')[0]

file_path= os.path.abspath(".")+"/"

amino_dic = {'G': 'GLY', 'A': 'ALA', 'S': 'SER', 'T': 'THR', 'C': 'CYS', 'V': 'VAL', 'L': 'LEU', 'I': 'ILE', 'M': 'MET', 'P': 'PRO', 'F': 'PHE', 'Y': 'TYR', 'W': 'TRP', 'D': 'ASP', 'E': 'GLU', 'N': 'ASN', 'Q': 'GLN', 'H': 'HIS', 'K': 'LYS', 'R': 'ARG'}

mutation_list = ['G81A'] 

def mysplit(string):
    match = re.match(r"([A-Z]+)([0-9]+)([A-Z]+)", string)
    if match:
       items = match.groups()
    return items

for i in mutation_list:
    if already_mutated == '0':
        formatted_resnum = mysplit(i)[1].zfill(4)
        mutation_res = amino_dic[mysplit(i)[2]]
        new_file_name = mysplit(i)[0]+mysplit(i)[1].zfill(4)+mysplit(i)[2]+'.inp'
        subprocess.call(['cp', file_path + 'X_XXX_X.inp', file_path + new_file_name])
        subprocess.call([file_path + 'make_input.bash', new_file_name, formatted_resnum, mutation_res, '0'])
    elif already_mutated == mysplit(i)[0]+mysplit(i)[1].zfill(4)+mysplit(i)[2]:
       pass
    else:
        formatted_resnum = mysplit(i)[1].zfill(4)
        mutation_res = amino_dic[mysplit(i)[2]]
        new_file_prefix = sys.argv[1].split('.')[0]+'_'+mysplit(i)[0]+mysplit(i)[1].zfill(4)+mysplit(i)[2]
        new_file_name = new_file_prefix+'.inp'
        subprocess.call(['cp', file_path + 'X_XXX_X.inp', file_path + new_file_name])
        subprocess.call(['cp', file_path + 'X_XXX_X.inp', file_path + new_file_name])
        subprocess.call([file_path + 'replace_pdb_name.bash', pdb_file_name, file_path + new_file_name])
        print(new_file_prefix) 
        subprocess.call([file_path + 'make_input.bash', new_file_name, formatted_resnum, mutation_res, new_file_prefix])      
