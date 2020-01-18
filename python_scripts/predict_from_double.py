#!/usr/bin/env python

from itertools import combinations
import numpy as np
np.set_printoptions(threshold = np.inf)

mutation_list = ['G81A', 'R88S', 'T104I', 'N124T', 'T141N', 'T207M', 'T278S', 'D299N']
rotamer_list = [ 'c1', 'c2', 'c3' ]
single_state = []
twoD_list = []
store_line = []
single_store_line = []
bind_dic = {}
single_bind_dic = {}

#----------------------------------------------------#
#----------------------------------------------------#
#---------------DEFINE NEW FUNCTIONS-----------------#
#----------------------------------------------------#
#----------------------------------------------------#

def calc_energy(alist, single_bind_dic, bind_dic, bind_fast_TS):
    total_energy = 0.0
    single_list = []
#    print(alist)
    for i in range(len(alist)):
        if alist[i][0] in single_bind_dic and alist[i][1] in single_bind_dic:
           if alist[i][0] not in single_list:
              total_energy = total_energy + float(single_bind_dic[alist[i][0]]) - bind_fast_TS
              single_list.append(alist[i][0])
#              print(float(single_bind_dic[alist[i][0]]) - bind_fast_TS)
#              print('single_energy', alist[i][0], 'is ', total_energy)
           if alist[i][1] not in single_list:
              total_energy = total_energy + float(single_bind_dic[alist[i][1]]) - bind_fast_TS
              single_list.append(alist[i][1])
#              print(float(single_bind_dic[alist[i][1]]) - bind_fast_TS)
#              print('single_energy', alist[i][1], 'is ', total_energy)
        else:
 #          print('calculate the combination', alist[i][0], 'or', alist[i][1])
           total_energy += 0.0
       
        if alist[i][0]+'_'+alist[i][1] in bind_dic.keys():
            total_energy = total_energy + float(bind_dic[alist[i][0]+'_'+alist[i][1]]) - bind_fast_TS 
#            total_energy = total_energy + float(bind_dic[alist[i][0]+'_'+alist[i][1]])*2 - float(single_bind_dic[alist[i][0]]) - float(single_bind_dic[alist[i][1]])
#            print('energy_of', float(bind_dic[alist[i][0]+'_'+alist[i][1]])*2 - float(single_bind_dic[alist[i][0]]) - float(single_bind_dic[alist[i][1]]))
            pass
        elif alist[i][1]+'_'+alist[i][0] in bind_dic.keys():
            total_energy = total_energy + float(bind_dic[alist[i][1]+'_'+ alist[i][0]]) - bind_fast_TS
#            total_energy = total_energy + float(bind_dic[alist[i][1]+'_'+ alist[i][0]])*2 - float(single_bind_dic[alist[i][1]]) - float(single_bind_dic[alist[i][0]])
#            print('energy_of', float(bind_dic[alist[i][1]+'_'+ alist[i][0]])*2 - float(single_bind_dic[alist[i][1]]) - float(single_bind_dic[alist[i][0]]))
            pass  
        else:
#           print('calculate the combination', alist[i])
           total_energy += 0.0
#    print(single_list)
    return total_energy 

#-----------------------------------------------------------#
#============Reading activation energy data=================#
#===============From activation_ene.txt  ===================#
#-----------------------------------------------------------#

def single_double_act(single_activation_file, double_activation_file):
    store_line = []
    with open(double_activation_file, 'r') as input_file:
         for lines in input_file:
             line = lines.split()
             store_line.append(line)

    single_store_line = []
    with open(single_activation_file, 'r') as file_read:
         for contents in file_read:
             content = contents.split()
             single_store_line.append(content)

#-----------------------------------------------------#
#======Making Dictionary for Self interactions========#
#-----------------------------------------------------#
    single_bind_dic = {}
    for m in range(len(single_store_line)):
         if single_store_line[m][0] !='None':
             single_bind_dic[single_store_line[m][0]] = single_store_line[m][1]
         else:
             pass

#-----------------------------------------------------#
#======Making Dictionary for Pair Interactions========#
#-----------------------------------------------------#
    bind_dic = {}
    for m in range(len(store_line)):
         if store_line[m][0] != 'None':
             bind_dic[store_line[m][0]] = store_line[m][1]
         else:
             pass

    return single_bind_dic, bind_dic


#-----------------------------------------------------#
#============Generate Lists of States=================#
#=================Single states &=====================#
#=================Double_mutation states==============#
#-----------------------------------------------------#

for i in mutation_list:
    small_list = []
    for j in rotamer_list:
        small_list.append(i+'_'+j)
        for k in mutation_list:
            for l in rotamer_list:
                if i !=k:
                   twoD_list.append(i+'_'+j+'_'+k+'_'+l)
    single_state.append(small_list)

#----------------------------------------------------#
#============= 6 states combination =================#
#----------------------------------------------------#

six_states_com = [[]]
for x in single_state:
    temp = []
    for y in x:
       for i in six_states_com:
           temp.append(i+[y])     
    six_states_com = temp

map_1 = {}
for f in six_states_com:
#    print(f)
    map_1['_'.join(f)]=combinations(f, 2)    

#--------------------------------------------------#
#===========Sort wrt minimum energy================#
#--------------------------------------------------#

just_an_array = []
key_list = []

single_activation_file = "single_ene_new.txt"
double_activation_file = "double_ene_new.txt"
single_bind_dic, bind_dic = single_double_act(single_activation_file, double_activation_file)
bind_fast_TS = 14.42
#print map_1
for keys in map_1:
    energy = calc_energy(list(map_1[keys]), single_bind_dic, bind_dic, bind_fast_TS)
    key_list.append(keys)
    just_an_array.append(float(energy))
    nd_a = np.array(just_an_array)
    new_nd_a = np.sort(nd_a, kind = 'heapsort')
    id_sort = np.argsort(nd_a, kind = 'headpsort')

#print(id_sort)
#print("unsorted_list")
#print(nd_a)
print("sorted list")
print(len(new_nd_a))
for i in range(10):
    print(key_list[id_sort[i]])

#print(list(key_list[id_sort[i]] for i in range(len(id_sort))))

#energy_1 = calc_energy(list(combinations(['E0045N_conf3', 'N0087S_conf2', 'F0088H_conf2', 'M0265F_conf2', 'A0273W_conf1', 'F0274R_conf1'], 2)), single_bind_dic, bind_dic, bind_fast_TS) 

#print(energy_1)

#==================================================#
