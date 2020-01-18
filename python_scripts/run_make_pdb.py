#!/usr/bin/env python

import subprocess

with open('mutation_options.txt', 'r') as read_file:
     for lines in read_file:
         line = lines.strip().split(' ')[0]
         print(line)
         subprocess.call(['./make_pdb.py', line, 'three_mutation_14_19.pdb']) # last string f_r name of the pdb file from which mutation would begin



