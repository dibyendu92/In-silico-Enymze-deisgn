#!/usr/bin/env python
import itertools
from itertools import combinations
import numpy as np
import pprint
import pandas
import math
import sys
np.set_printoptions(threshold = np.inf)

alpha = sys.argv[1]
m =sys.argv[2]
beta = sys.argv[3]

#----------------------------------------------------#
#----------------------------------------------------#
#---------------DEFINE NEW FUNCTIONS-----------------#
#----------------------------------------------------#
#----------------------------------------------------#

def boltz_avg(a_list):
    RT = 0.593
    sorted_list = sorted(a_list)
    exp_sorted = []
    for i in range(len(sorted_list)):
        exp_sorted.append((math.exp(-(float(sorted_list[i])-float(sorted_list[0]))/RT)))
    exp_sum = 0.0
    for i in range(len(sorted_list)):
        exp_sum += exp_sorted[i]
    abs_pro = []
    ene_pro = []
    for j in range(len(exp_sorted)):
        ene_pro.append((float(sorted_list[j])*exp_sorted[j])/exp_sum)
        abs_pro.append(exp_sorted[j]/exp_sum)

    return sum(x for x in ene_pro)

def calc_energy(single_list, double_list, single_bind_dic, bind_dic, bind_fast_TS):
    total_energy = 0.0
    single_energy_dic = {}
    double_energy_dic = {}
    min_single_dic = {}
    min_double_dic = {}
#    print(alist)
#    print(single_list)
    for i in single_list:
#        print i
        if i in single_bind_dic:
 #           print(i.split("c"))
            if i.split("c")[0] not in single_energy_dic.keys():
#                 print(single_bind_dic[i])
                 single_energy_dic[i.split("c")[0]] = [float(single_bind_dic[i])]
            else:
                single_energy_dic[i.split("c")[0]].append(float(single_bind_dic[i]))
        else:
            total_energy += 0.0
    for key in single_energy_dic:

#       min_single_dic[key] = min(single_energy_dic[key])
#        min_single_dic[key] = np.array(single_energy_dic[key]).mean()
        min_single_dic[key] = boltz_avg(single_energy_dic[key])
#        print min(list(map(lambda x : round(x -bind_fast_TS, 2), single_energy_dic[key]))), key
    for min_ene in min_single_dic:
        diff_sin = float(min_single_dic[min_ene]) - bind_fast_TS
        print min_ene, round(diff_sin, 2)
#        if abs(diff_sin):
        total_energy = total_energy + float(alpha)*diff_sin  - float(beta)*float(m)*diff_sin

#    print(double_list)
    for j in double_list:
#        print j
        split_list = j.split('_')    
        if split_list[0]+"_"+split_list[1] in bind_dic:
            if split_list[0].split("c")[0]+split_list[1].split("c")[0] not in double_energy_dic.keys():
               double_energy_dic[split_list[0].split("c")[0]+split_list[1].split("c")[0]] = [float(bind_dic[j])]
#               print(split_list[0].split("c")[0]+split_list[1].split("c")[0])
            else:
               double_energy_dic[split_list[0].split("c")[0]+split_list[1].split("c")[0]].append(float(bind_dic[j]))
        elif split_list[1]+"_"+split_list[0] in bind_dic:
            if split_list[1].split("c")[0]+split_list[0].split("c")[0] not in double_energy_dic:
               double_energy_dic[split_list[1].split("c")[0]+split_list[0].split("c")[0]] = [float(bind_dic[split_list[1]+"_"+split_list[0]])]
#               print(split_list[0].split("c")[0]+split_list[1].split("c")[0])
            else:
               double_energy_dic[split_list[1].split("c")[0]+split_list[0].split("c")[0]].append(float(bind_dic[split_list[1]+"_"+split_list[0]]))

        else:
            total_energy += 0.0
#    print(len(double_energy_dic))
    for key in double_energy_dic:
#        min_double_dic[key] = min(double_energy_dic[key])
#        min_double_dic[key] = np.array(double_energy_dic[key]).mean()
        min_double_dic[key] = boltz_avg(double_energy_dic[key])
#        print min(list(map(lambda x : round(x -bind_fast_TS, 2), double_energy_dic[key]))), key
    for min_ene in min_double_dic:
        diff = float(min_double_dic[min_ene]) - bind_fast_TS
        print min_ene, round(diff, 2)
#        if abs(diff) > 0.5:
#            total_energy = total_energy + diff 
        total_energy = total_energy + float(beta)*diff 
#    print total_energy   
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
def gen_sin_doub_states(mutation_list):
    small_list = []
    twoD_list = []
    for i in range(len(mutation_list)):
        for j in rotamer_list:
            if 'A' not in mutation_list[i]:
                small_list.append(mutation_list[i]+j)
            else:
                if j == 'c1':
                    if mutation_list[i]+j not in small_list:
                       small_list.append(mutation_list[i]+j)
                else:
                    pass
            for k in range(i+1, len(mutation_list)):
                for l in rotamer_list:
                    if 'A' not in mutation_list[i] and 'A' not in mutation_list[k]:
                        if mutation_list[i] !=mutation_list[k]:
                           if mutation_list[i]+j+'_'+mutation_list[k]+l not in twoD_list:
                               twoD_list.append(mutation_list[i]+j+'_'+mutation_list[k]+l)
                    else:
                        if mutation_list[i] !=mutation_list[k]:
                           if 'A' in mutation_list[i]:
                                j = "c1" 
                                if 'A' in mutation_list[k]:
                                   l = "c1"
                                   if mutation_list[i]+j+'_'+mutation_list[k]+l not in twoD_list:
                                      twoD_list.append(mutation_list[i]+j+'_'+mutation_list[k]+l)
                                else:
#                                   j = "c1"
                                   if mutation_list[i]+j+'_'+mutation_list[k]+l not in twoD_list:
                                       twoD_list.append(mutation_list[i]+j+'_'+mutation_list[k]+l)
                           else:
                               l = "c1"
                               if mutation_list[i]+j+'_'+mutation_list[k]+l not in twoD_list:
                                   twoD_list.append(mutation_list[i]+j+'_'+mutation_list[k]+l)
                        else:
                            pass
#   print(small_list)
    
#   print('double_state', twoD_list)
    return small_list, twoD_list

res_interest = ['G81', 'R88', 'T104', 'N124', 'T141', 'T207', 'T278', 'D299']
#res_interest = ['T104', 'N124', 'D299', 'T141', 'T278', 'G81']
mutation_dic = {'G81': ['A'], 'R88': ['S'], 'T104': ['I'], 'N124': ['T'], 'T141': ['N'], 'T207': ['M'], 'T278': ['S'], 'D299': ['N']}
#mutation_dic = {'G81': ['A'], 'T104': ['I'], 'N124': ['T'], 'T141': ['N'], 'T207': ['M'], 'T278': ['S']}
#conf = ['c1', 'c2', 'c3']
newdata = []
for f in res_interest:
    raw_data = []
    for j in mutation_dic[f]:
#        for k in conf:
        raw_data.append(f+j)
    newdata.append(raw_data)


result = list(itertools.product(*newdata))

#print(list(result))

a_list = []

for f in result:
    mutation_list =  list(f) #[ 'Q36K', 'H49Q', 'D89H']
    rotamer_list = [ 'c1', 'c2', 'c3' ]
    single_activation_file = "single_ene_pre_new.txt"
    double_activation_file = "double_ene_pre_new.txt"
    bind_fast_TS = 14.4
    single_state_list, double_state_list = gen_sin_doub_states(mutation_list)
    single_bind_dic, bind_dic = single_double_act(single_activation_file, double_activation_file)
    energy = calc_energy(single_state_list, double_state_list, single_bind_dic, bind_dic, bind_fast_TS)
    a_list.append([mutation_list, energy])
#    print(mutation_list, energy)
a_list.sort(key=lambda x: x[1])
dat_frme = pandas.DataFrame(a_list)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
pprint.pprint(dat_frme)
#pprint.pprint(a_list)
#==================================================#
