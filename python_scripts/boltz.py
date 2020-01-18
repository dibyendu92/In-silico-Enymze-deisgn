#!/usr/bin/env python

import math
import sys

RT = 0.593
file_name = sys.argv[1]

#RT = 3.974
unsorted_list = []
with open(file_name, 'r') as file_ene:
     for lines in file_ene:
         line = lines.strip().split(' ')
         unsorted_list.append(line)

sorted_list = sorted(unsorted_list, key=lambda x:float(x[1]))
#print sorted_list
exp_sorted = []
exp_lra = []

for i in range(len(sorted_list)):
    exp_sorted.append((math.exp(-(float(sorted_list[i][1])-float(sorted_list[0][1]))/RT)))

#for i in range(len(sorted_list)):
#    if abs(float(sorted_list[i][2])-float(sorted_list[0][2])) <=5.0:
 #      exp_lra.append((math.exp(-(float(sorted_list[i][2])-float(sorted_list[0][2]))/RT)))
 #   else:
 #      exp_lra.append(0.00)


exp_sum= 0.0
for i in range(len(sorted_list)):
    exp_sum += exp_sorted[i] 

abs_pro = []
ene_pro = []
for j in range(len(exp_sorted)):
    ene_pro.append((float(sorted_list[j][1])*exp_sorted[j])/exp_sum)
    abs_pro.append(exp_sorted[j]/exp_sum)

print sum(x for x in ene_pro)
#print exp_lra

#avg_ene = 0.0
#avg_ene = sum(x for x in ene_pro)

#gap_list = []

#for i in range(len(sorted_list)):
#    gap_list.append(abs(float(sorted_list[i][1])-avg_ene))
    
#index=gap_list.index(min(gap_list))
#print index, avg_ene
#print sorted_list
#for i in range(len(sorted_list)):
#    if (float(sorted_list[i][1])-avg_ene) <= 0.0:
#       exp_lra.append((math.exp(-(float(sorted_list[i][2])-float(sorted_list[index][2]))/5.0)))
#    elif (float(sorted_list[i][1])-avg_ene) >0 and (float(sorted_list[i][1])-avg_ene) <=3.0:
#       exp_lra.append(math.exp(-(float(sorted_list[i][2])-float(sorted_list[index][2]))/50.0))
#    else:
#       exp_lra.append(0.00)
#print sum(exp_lra)/len(sorted_list)
#for i in range(len(sorted_list)):
#    print sorted_list[i][0], sorted_list[i][1], (float(sorted_list[0][2]) - float(sorted_list[i][2]))*0.2

#print avg_ene
#print exp_lra
#for i in range(len(sorted_list)):
#    print ' '.join(sorted_list[i]), ene_pro[i]
