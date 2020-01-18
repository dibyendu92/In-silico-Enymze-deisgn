#!/usr/bin/env python
import os
from shutil import copyfile
import subprocess
current_dir = os.path.abspath('.') + '/'
store_line = []
with open('serial_num.txt', 'r') as read_file:
     for lines in read_file:
         line = lines.strip().split()
         store_line.append(line)
for i in range(0, len(store_line), 6):
    tmp = []
    for j in range(i, i+5):
        tmp.append(store_line[j][2])
    tmp.append(store_line[j+1][0]) 
    if os.path.isdir(tmp[5].split('.pdb')[0]):
#       print('coming')
       os.chdir(tmp[5].split('.pdb')[0])
#       print(os.getcwd())
       copyfile(current_dir+'kemp_evb.inp', current_dir+tmp[5].split('.pdb')[0]+'/kemp_evb.inp')
       copyfile(current_dir+'steep.inp', current_dir+tmp[5].split('.pdb')[0]+'/steep.inp')
       copyfile(current_dir+tmp[5], current_dir+tmp[5].split('.pdb')[0]+'/'+tmp[5])
       copyfile(current_dir+'mod_evb_inp.py', os.getcwd()+'/'+'mod_evb_inp.py')
       copyfile(current_dir+'mod_steep_inp.py', os.getcwd()+'/'+'mod_steep_inp.py')
       subprocess.call(['python', 'mod_evb_inp.py', tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]])
       subprocess.call(['python', 'mod_steep_inp.py', tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]])
#       os.system('molaris_hpc9.15  kemp_evb_run.inp > kemp_evb_run.out 2>&1 &')
    else:
       os.mkdir(tmp[5].split('.pdb')[0])
       os.chdir(tmp[5].split('.pdb')[0])
       copyfile(current_dir+'kemp_evb.inp', current_dir+tmp[5].split('.pdb')[0]+'/kemp_evb.inp')
       copyfile(current_dir+'steep.inp', current_dir+tmp[5].split('.pdb')[0]+'/steep.inp')
       copyfile(current_dir+tmp[5], current_dir+tmp[5].split('.pdb')[0]+'/'+tmp[5])
       copyfile(current_dir+'mod_evb_inp.py', os.getcwd()+'/'+'mod_evb_inp.py')
       copyfile(current_dir+'mod_steep_inp.py', os.getcwd()+'/'+'mod_steep_inp.py')
       subprocess.call(['python', 'mod_steep_inp.py', tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]])
       subprocess.call(['python', 'mod_evb_inp.py', tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]])
#       os.system('molaris_hpc9.15  kemp_evb_run.inp > kemp_evb_run.out 2>&1 &')
    os.chdir(current_dir)
