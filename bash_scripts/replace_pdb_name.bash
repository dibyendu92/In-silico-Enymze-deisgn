#!/bin/bash
old_pdb='three_mutation_14_19.pdb'
new_pdb=$1
input_file=$2

sed -i "s/$old_pdb/$new_pdb/" $input_file
