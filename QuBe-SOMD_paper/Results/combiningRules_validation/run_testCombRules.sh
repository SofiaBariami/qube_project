#!/usr/bin/env bash

molecules=("acetic_acid"  "methylacetate" "dimethylacetamide" "acetaldehyde" "N-methylaniline" "acetophenone" "propane" "bromobenzene" "benzene" "benzonitrile")

for mol in ${molecules[*]}; 
do
cd $mol
echo "$mol"

cp "../test_combRules.py" .

/home/sofia/sire-paper.app/bin/ipython test_combRules.py
rm "test_combRules.py"
cd ..

done

