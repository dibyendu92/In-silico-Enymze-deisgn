#!/usr/bin/bash

pdb_file=$1

total_line=`wc -l $pdb_file| awk '{print $1}'`

tail_line=`expr $total_line - 102`

tail -$tail_line $pdb_file | head -1

tail -$tail_line $pdb_file > dum.pdb
cat add.pdb dum.pdb >> new.pdb

mv new.pdb $pdb_file

rm dum.pdb 



