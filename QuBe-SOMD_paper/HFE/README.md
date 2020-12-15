Here are the instructions to run automated Hydration Free Energy calculations using the QuBe FF.
The following steps are done automatically using [prepare_HFE_files.sh](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/HFE/scripts/prepare_HFE_files.sh). This script needs some adjustments (file paths etc) to work on your workstation. 

- For the vacuum simulations: 
1. Starting with the pdb/xml files of the ligands, generate the corresponding amber files (prm7/rst7) using [qube_to_prmRst.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/FEP_preparation/qube_to_prmRst.py)
2. Remove the SOLTY flag and rename the amber files to SYSTEM.top and SYSTEM.crd
3. Generate the. MORPH.pert files using the scripts [morph_step1.py] and [morph_step2.py]. These scripts read the parameters of the molecules and return the pert files for the discharge and the vanish legs.
4. Create the folder architecture and submit the simulations. 

- For the solvated simulations: 
1. Starting with the pdb/xml files of the ligands, generate the corresponding amber files (prm7/rst7) using [qube_to_prmRst.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/FEP_preparation/qube_to_prmRst.py)
2. Use the BioSimSpace.app python (e.g. ~/biosimspace.app/bin/ipython) to solvate the molecule with [solvate.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/FEP_preparation/solvate.py):
```
run ./solvate.py --input MOL.prm7 MOL.rst7 --output MOL_sol --water tip3p --box_dim 26
```
The dimension of the side of the box is in A. (This might need to be changed)

3. Equilibrate the system with [amberequilibration.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/FEP_preparation/amberequilibration.py) also with BioSimSpace.
```
run ./amberequilibration.py --input MOL_sol.prm7 MOL_sol.rst7 --output MOL

```
From this point on, the process is the same as the one for the molecules in vacuum:
4. Remove the SOLTY flag and rename the amber files to SYSTEM.top and SYSTEM.crd
5. Generate the. MORPH.pert files using the scripts [morph_step1.py] and [morph_step2.py]. 
6. Create the folder architecture and submit the simulations.
