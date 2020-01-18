#!/usr/bin/env python
import sys
import os

pdb_file_name = sys.argv[1] 
mutated = sys.argv[2].lstrip("0") # residue number
last_residue = sys.argv[3]
already_mutated = sys.argv[4]
path = sys.argv[5]
folder_path = os.path.abspath(path)+'/'

amino_dic = {'GLY': 'G','ALA': 'A', 'SER': 'S', 'THR': 'T', 'CYS': 'C', 'CYI': 'C', 'VAL': 'V', 'LEU': 'L', 'ILE': 'I', 'MET':'M', 'PRO': 'P', 'PHE': 'F', 'TYR': 'Y', 'TRP': 'W', 'ASP': 'D', 'GLU': 'E', 'ASN': 'N', 'GLN': 'Q', 'HIS': 'H', 'HIE': 'H', 'LYS': 'K', 'ARG': 'R'}

def three_to_one(string):
    if string in amino_dic:
       return amino_dic[string]
    else:
       	return string

pdb_array = []
discard_array = []
new_residue_array = []
sequence = {}
with open(pdb_file_name, "r") as input_obj:
     for content in input_obj:
         content = content.strip()
         residue = content[22:26].strip()
#         sequence[residue] = content[17:20]
         if residue != mutated and residue != last_residue:
           pdb_array.append(content[0:54])
         elif residue == mutated:
           discard_array.append(content[0:54])
         else:
           new_residue_array.append(content[0:54])
#print(len(discard_array))   
#print(len(new_residue_array))

number_pointer = int(discard_array[0][6:11])
#print(number_pointer)
f_obj = open("NEW_"+pdb_file_name, "w")

i=1

while i <number_pointer:
      f_obj.write(pdb_array[i-1]+'\n')
      residue = pdb_array[i-1][22:26]
      sequence[residue] = pdb_array[i-1][17:20]
#      print(i)
      i += 1
#print(pdb_array[i])   
for j in range(len(new_residue_array)):
    f_obj.write(new_residue_array[j][0:6]+str(j+number_pointer).rjust(5)+new_residue_array[j][11:22]+mutated.rjust(4)+new_residue_array[j][26:54]+'\n')
    residue = mutated.rjust(4)
    sequence[residue] = new_residue_array[j][17:20]
j_curr = len(new_residue_array)
#print(j_curr)
for k in range(i-1, len(pdb_array)):
    f_obj.write(pdb_array[k][0:6]+str(k+1+j_curr).rjust(5)+pdb_array[k][11:54]+'\n')
    residue = pdb_array[k][22:26]
    sequence[residue] = pdb_array[k][17:20] 

f_obj.close()                       

if os.path.exists(folder_path + 'seq.txt'):
   append_write = 'a'
   print(append_write)
else:
   append_write = 'w'
   print(append_write)

mutation_info = three_to_one(discard_array[0][17:20])+mutated.zfill(4)+three_to_one(new_residue_array[0][17:20])
#print(mutation_info)
write_file = open(folder_path + 'seq.txt', append_write)
write_file.write("============================================"+'\n')
if already_mutated == '0':
   write_file.write(pdb_file_name+" "+mutation_info+'\n')
#   print("COMING")
else:
   write_file.write(pdb_file_name+" "+already_mutated.split('_'+mutation_info)[0]+" "+mutation_info+'\n')
#   print("WHY HERE?")
write_file.write("============================================"+'\n')
for keys in sequence:
    write_file.write(three_to_one(sequence[keys]))
write_file.write('\n')

write_file.close() 
