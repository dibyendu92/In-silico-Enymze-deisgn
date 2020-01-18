#!/usr/bin/env python
#==================================================#
#    THIS NEXT PART CAN DO RANDOM SELECTION        #
#   BUT WE WANT DO GUIDED MUTATIONS SELECTION      #
#   WE CAN DO BY READING ACTIVATION ENERGIES FROM  #
#           SINGLE MUTATION CALCULATIONS           #
#==================================================#

import random
from operator import itemgetter
import itertools

mutation_list = []
conform_list = ['conf1', 'conf2', 'conf3']
new_list = []
with open('mutations.txt', 'r') as input_file: 
     for line in input_file:
         line = line.strip()
         mutation_list.append(line)
constant = (len(mutation_list))
while len(new_list) < constant*2:
      pick = random.choice(mutation_list)
      con_pick = random.choice(conform_list)
      new_list.append(pick)
      new_list.append(con_pick)
      if len(mutation_list) > 0:
         mutation_list.remove(pick)
      if len(mutation_list) == 0:
         pdb_string = '_'.join(new_list)
         print(pdb_string)
   

#=================================================#
#     GUIDED SLECTION PART STARTS FROM HERE       #
#     WE MIGHT NEED SOME VARIABLES FROM THE       #
#            ABOVE PART OF THE CODE               #
#=================================================#
activation_list = []
lst_list = []

def get_index(string, list_name):
    get_index = list_name.index(string)
    return get_index
    
with open('mut_activation.txt', 'r') as read_file:  # mut_activation.txt contains mutation information
     for content in read_file:
         entry = content.strip().split(' ')
         activation_list.append(entry)
         var = 'XXXXXX'
         counter = 1
     for f in range(len(activation_list)):
         if activation_list[f][0].split('_')[0]!= var:
            var = activation_list[f][0].split('_')[0]
            list_name = 'list_'+'%03d' % counter
            list_name = []
            lst_list.append(list_name)
            list_name.append([activation_list[f][0], float(activation_list[f][1])])
            counter += 1
         else:
            list_name.append([activation_list[f][0], float(activation_list[f][1])])

new_list_lst = []
for i in lst_list:
    counter = 1
    new_list = 'newlist_'+'%03d' % counter
    counter += 1
    new_list = sorted(i, key=itemgetter(1)) 
    new_list = [item[0] for item in new_list]
    new_list_lst.append(new_list)
    all_comb = list(itertools.product(*new_list_lst))
#    all_comb_enu = list(itertools.product(enumerate(*new_list_lst)))
#print(all_comb_emu)
  
#=======================================================================================================#
#            IF WE HAVE TO SELECT COMBINATIONS WITH ONE MUTATION AS AN OPTION (like M0084C_conf3)
#=======================================================================================================#
#selected_comb = []
#for j in range(len(all_comb)):
#    if 'M0084C_conf3' in all_comb[j]:
#       selected_comb.append(all_comb[j]) # automatically ordered with lowest activation energy combinations
#print(len(selected_comb))    
#selected_pdbstring_lst = list('_'.join(a) for a in selected_comb)  
#=======================================================================================================#
#=======================================================================================================#

selected_comb = all_comb # comment it, if the section above is not commented
selected_pdbstring_lst = list('_'.join(a) for a in selected_comb) # comment it, if the section above is not commented
map_list = []
for k in selected_comb:
    a = []
    for m in range(len(k)):
        a.append(get_index(k[m], new_list_lst[m]))
    map_list.append(a)
print(map_list)

write_obj = open('mutation_options.txt', 'w')

unsorted_lst = []

if len(selected_pdbstring_lst) == len(map_list):
   for m in range(len(map_list)):
       tmp_str = ''.join(map(str, map_list[m]))
       sum_total = str(sum(map_list[m])) 
       tmp_lst = [selected_pdbstring_lst[m], tmp_str, sum_total]
       unsorted_lst.append(tmp_lst)     
#       write_obj.write(selected_pdbstring_lst[m] + ' '+ tmp_str+ ' '+ sum_total+'\n')
       
#print(unsorted_lst)
sorted_lst = sorted(unsorted_lst, key=lambda x:int(x[2]))
for n in range(len(sorted_lst)):
    write_obj.write(' '.join(sorted_lst[n])+ '\n')
#    write_obj.write('\n')
print(sorted_lst)
write_obj.close()
