#!/bin/bash

## Not currently in use, but this script should be used for binding calculations
current_dir=`pwd`

for f in *_bind.inp
do
  file=`basename $f .inp`
#  if [ $file != 'fast_TS_bind' ]; then
  #echo $file
     cd $current_dir/output/$file
     echo $file >> $current_dir/pdld_bind.txt
     grep 'PDLD/S-LRA estimate  ' bind_pdld_s_lra.out >> $current_dir/pdld_bind.txt
     cd $current_dir
#  fi
done
