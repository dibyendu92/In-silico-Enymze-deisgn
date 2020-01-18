#!/usr/bin/env python

import sys

def find_serial(pdb_file, text_pattern):
    with open(pdb_file, "r") as input_file:
         for line in input_file:
#             print(line[13:26].split(' '))
#             print(text_pattern.split(' '))
             if line[13:26] == text_pattern:
#                print(text_pattern)
                serial_number = line[6:11]
                return serial_number

pdb_file_name = sys.argv[1]

text_pattern_1 = "CG  ASP   126" # note the extra whitesapce after residue number
text_pattern_2 = "OD1 ASP   126"
text_pattern_3 = "OD2 ASP   126"
text_pattern_4 = "SG  CYI   254"
text_pattern_5 = "SG  CYI   260"

CG_ASP = find_serial(pdb_file_name, text_pattern_1)
OD1_ASP = find_serial(pdb_file_name, text_pattern_2)
OD2_ASP = find_serial(pdb_file_name, text_pattern_3)
SG_CYI_1 = find_serial(pdb_file_name, text_pattern_4)
SG_CYI_2 = find_serial(pdb_file_name, text_pattern_5)

print "CG_ASP = ", CG_ASP
print "OD1_ASP = ", OD1_ASP
print "OD2_ASP = ", OD2_ASP
print "SG_CYI_1 = ", SG_CYI_1
print "SG_CYI_2 = ", SG_CYI_2

