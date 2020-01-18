#!/bin/bash

file_name=$1 #molaris input file for mutating a residue
resnum=$2    #residue number to be mutated
resname=$3   #amino acid name to be mutated
already_mutated=$4
#echo $already_mutated
current_dir=`pwd`'/'

sed -i "s/NN/$resnum/g" $file_name 
sed -i "s/SS/$resname/g" $file_name

out_file=`basename $file_name .inp`'.out'

echo $current_dir

molaris_hpc9.15 $file_name > $out_file &

sleep 1

cd ./output/`basename $file_name .inp`

if [ -e 'mutate_center1.pdb' ] 
then
   $current_dir/mod_molaris_pdb.py 'mutate_center1.pdb' $resnum '302' $already_mutated $current_dir
   if [ -e 'NEW_mutate_center1.pdb' ] 
   then
     cp 'NEW_mutate_center1.pdb' $current_dir`basename $file_name .inp`'_conf1.pdb'
   else
    exit 1
   fi
else
   exit 1
fi
if [ -e 'mutate_center2.pdb' ] 
then
   $current_dir/mod_molaris_pdb.py 'mutate_center2.pdb' $resnum '302' $already_mutated $current_dir
   if [ -e 'NEW_mutate_center2.pdb' ]
   then
     cp 'NEW_mutate_center2.pdb' $current_dir`basename $file_name .inp`'_conf2.pdb'
   else
     exit 1
   fi
else
  exit 1
fi
if [ -e 'mutate_closest_center.pdb' ] 
then 
   $current_dir/mod_molaris_pdb.py 'mutate_closest_center.pdb' $resnum '302' $already_mutated $current_dir
   if [ -e 'NEW_mutate_closest_center.pdb' ]
   then
      cp 'NEW_mutate_closest_center.pdb' $current_dir`basename $file_name .inp`'_conf3.pdb'
   fi
else
   exit 1
fi
cd $current_dir

#     $current_dir/binding_input.py $current_dir`basename $file_name .inp`'_conf1.pdb' $already_mutated # anything other than zero means double mutation
#     $current_dir/binding_input.py $current_dir`basename $file_name .inp`'_conf2.pdb' $already_mutated 
#     $current_dir/binding_input.py $current_dir`basename $file_name .inp`'_conf3.pdb' $already_mutated
