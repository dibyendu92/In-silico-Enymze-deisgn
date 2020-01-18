#!/usr/bin/env python

unsorted_list = []
with open('activation_ene.txt', 'r') as file_ene:
     for lines in file_ene:
         line = lines.strip().split(' ')
         unsorted_list.append(line)

sorted_list = sorted(unsorted_list, key=lambda x:float(x[1]))

for i in range(len(sorted_list)): 
    print(' '.join(sorted_list[i]))

