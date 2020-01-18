#!/bin/bash

## extract all activation energy results from the runs
working_dir=`pwd`

for f in `ls -d */`
do 
#   echo $f
   cd $f
    cp $working_dir/change_map.py change_map.py
#    python change_map.py
    mapping_hpc9.15 <map_kemp_evb_run.inp> map_kemp_evb_run.out
#    sleep 1   
#   ls
   if [ -f 'map_kemp_evb_run.out' ]
   then 
      cp $working_dir/extract_act_ene.py extract_act_ene.py
#      echo $f 
      ./extract_act_ene.py
      cd $working_dir
   else
      cd $working_dir
   fi
#echo `pwd`
done
