#!/bin/bash

demo_file_name=$1  #molaris DEMO input file for mutating a residue e.g. X_XXX_X.inp
pdb_to_mod=$2      #molaris generated pdb where new residue is placed at the end e.g. mutate_center2.pdb
resnum=$3          #residue number to be mutated e.g. 45
resname=$4         #amino acid name to be mutated e.g. ASN
already_mutated=$5 #echo $already_mutated e.g. E0045N
old_pdb=$6         #pdb used to start mutation e.g. E0045N_conf2.pdb 
new_pdb=$7         #pdb generated after mutation (modified) e.g. A0273W_conf2.pdb
current_dir=`pwd`'/'
file_name=`basename $new_pdb .pdb`'.inp'

cp $current_dir$demo_file_name $current_dir$file_name

sed -i "1s/.*/$old_pdb/" $file_name
sed -i "s/NN/$resnum/g" $file_name
sed -i "s/SS/$resname/g" $file_name

out_file=`basename $file_name .inp`'.out'

#echo $current_dir

molaris_hpc9.15_rms2 $file_name > $out_file &  # use new molaris version, old version does not work

sleep 1

cd ./output/`basename $file_name .inp`

echo `pwd`

if [ -e $pdb_to_mod ]
then
   $current_dir/mod_molaris_pdb.py $pdb_to_mod $resnum '302' $already_mutated $current_dir # number is last residue number + 1
   if [ -e 'NEW_'$pdb_to_mod ]
   then
     cp 'NEW_'$pdb_to_mod $current_dir$new_pdb
   else
    exit 1
   fi
else
   exit 1
fi
cd $current_dir
