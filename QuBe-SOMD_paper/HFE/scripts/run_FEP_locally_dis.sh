#!/bin/bash
  
for i in $(seq 0.00 0.10 1.00)
do
mkdir lambda-$i
cd lambda-$i
~/sire.app/bin/somd-freenrg -C  ../../input/sim_dis.cfg -d 0 -l $i -p OpenCL
cd ../
done

~/sire.app/bin/analyse_freenrg mbar -i lambda-*/simfile.dat -o out.dat -p 90
