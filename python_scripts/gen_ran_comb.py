#!/usr/bin/env python3

# generate random combinations of a list of mutation
import random

a = ['G81', 'R88', 'T104', 'N124', 'T141', 'T207', 'T278', 'D299']
store_list = []
while len(store_list) < 50:
     a_list = random.choices(a, k =6)
     if len(a_list) == len(set(a_list)):
         store_list.append(a_list)

print(store_list)
