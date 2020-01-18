#!/usr/bin/env python

def search_replace(angle_header, angle_pattern, angle_change):
    for i in range(len(file_loader)):
        if file_loader[i] == angle_header:
           print(file_loader[i])
           for j in range(i+1, len(file_loader)):
#              print file_loader[j]
               if file_loader[j] == angle_pattern:
                  print(file_loader[j])
                  file_loader[j+1] = angle_change

def add_angle(add_angle_header, add_angle_change, add_angle_pattern, add_angle):
    for i in range(len(file_loader)):
        if file_loader[i] == add_angle_header:
           file_loader[i] = add_angle_change 
        if file_loader[i] == add_angle_pattern:
           file_loader.insert(i+1, add_angle)
            

old_dat_file = "evb.dat"
file_loader = []
angle_header = "   30                   angles(atoms,types,exist)\n"

angle_header_new ="   35          angle parameters(angle0(radian),force,gausD,gausig,type)\n"


first_angle_pattern = "     9    11    12\n"

second_angle_pattern = "    10     9    11\n"
third_angle_pattern = "     6     7     8\n"
forth_angle_pattern = "     8     7     9\n"
fifth_angle_pattern = "   1.911  50.000   0.000   1.000    32\n"
sixth_angle_pattern = "   2.210  50.000   0.000   1.000    37 ! C7  C7a O1 state 1\n"

first_angle_change = "    36    33 #\n"
second_angle_change = "    37     5 #\n"
third_angle_change = "    38     5 #\n"
forth_angle_change = "    36     5 #\n"
fifth_angle_change = "   2.800  50.000   0.000   1.000    33\n"
#sixth_angle_change = "   0.000   0.000   0.000   1.000    38\n"

add_angle_header ="   35          angle parameters(angle0(radian),force,gausD,gausig,type)\n"
add_angle_change ="   38          angle parameters(angle0(radian),force,gausD,gausig,type)\n"

add_angle_pattern = "   0.000   0.000   0.000   1.000    35\n"

add_angle_1 ="   1.911  50.000   0.000   1.000    36 ! C3a C3/C7a  N2/O state 1\n" 
add_angle_2 ="   2.360  50.000   0.000   1.000    37 ! C4  C3  C3 state 1\n"
add_angle_3 ="   2.210  50.000   0.000   1.000    38 ! C7  C7a O1 state 1\n"
write_file = open("evb_mod.dat", "w")

start_serach = False
start_replace = True
with open(old_dat_file, "r") as input_file:
     for line in input_file:
         file_loader.append(line)

search_replace(angle_header, first_angle_pattern, first_angle_change)
search_replace(angle_header, second_angle_pattern, second_angle_change)
search_replace(angle_header, third_angle_pattern, third_angle_change)
search_replace(angle_header, forth_angle_pattern, forth_angle_change)
search_replace(angle_header_new, fifth_angle_pattern, fifth_angle_change)

#add_angle(add_angle_header, add_angle_change, add_angle_pattern, add_angle_4)
add_angle(add_angle_header, add_angle_change, add_angle_pattern, add_angle_3)
add_angle(add_angle_header, add_angle_change, add_angle_pattern, add_angle_2)
add_angle(add_angle_header, add_angle_change, add_angle_pattern, add_angle_1)

#search_replace(angle_header_new, sixth_angle_pattern, sixth_angle_change)
#for i in range(len(file_loader)):
#    if file_loader[i] == angle_header:
#       print file_loader[i]    
#       for j in range(i+1, len(file_loader)):
#           print file_loader[j]
#           if file_loader[j] == first_angle_pattern:
#              print file_loader[j]
#              file_loader[j+1] = first_angle_change

for i in range(len(file_loader)):
    write_file.write(file_loader[i])

write_file.close()                  
