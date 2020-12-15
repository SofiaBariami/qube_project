Here are the instructions to run automated Hydration Free Energy calculations using the QuBe FF.

- For the vacuum simulations: 
1. Starting with the pdb/xml files of the ligands, generate the corresponding amber files (prm7/rst7) using [qube_to_prmRst.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/FEP_preparation/qube_to_prmRst.py)
2. Rename the amber files to SYSTEM.top and SYSTEM.crd
3. Generate the. MORPH.pert files using the scripts [morph_step1.py] and [morph_step2.py]. These scripts read the parameters of the molecules and return the pert files for the discharge and the vanish legs.
4. Create the folder architecture and submit the simulations. This is done automatically using [this script]().

- For the solvated simulations: 
1. Starting with the pdb/xml files of the ligands, generate the corresponding amber files (prm7/rst7) using [qube_to_prmRst.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/FEP_preparation/qube_to_prmRst.py)
2. Use the BioSimSpace.app python (e.g. ~/biosimspace.app/bin/ipython) to solvate the molecule with [solvate.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/FEP_preparation/solvate.py):
```
run ./solvate.py --input FILE.prm7 FILE.rst7 --output FILE_sol --water tip3p --box_dim X
```
The dimension of the side of the box is in A.
3. Equilibrate the system with [amberequilibration.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/FEP_preparation/amberequilibration.py)
From this point on, the process is the same as the one for the molecules in vacuum:
4. Rename the amber files to SYSTEM.top and SYSTEM.crd
5. Generate the. MORPH.pert files using the scripts [morph_step1.py] and [morph_step2.py]. 
6. Create the folder architecture and submit the simulations. This is done automatically using [this script](scripts/prepare_HFE_files.sh). This script needs some adjustments (file paths etc) to work on your workstation. 
