
# coding: utf-8

import sys,os

iname=("MOL.prm7")
with open(iname) as infile:
    
    with open("SYSTEM.top", "w") as o:
    
        while True:
            line=infile.readline()
            if line=="":
                break
            elif "%FLAG SOLTY" not in line:
                o.write(line)
            else:
                o.write(line)
                line=infile.readline()
                o.write(line)
                while "%FLAG LENNARD_JONES" not in line:
                    line=infile.readline()
                o.write(line)





