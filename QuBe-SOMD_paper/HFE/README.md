Here are the instructions to run automated Hydration Free Energy calculations using the QuBe FF.
The following steps are done automatically using [prepare_HFE_files.sh](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/HFE/scripts/prepare_HFE_files.sh). This script needs some adjustments (file paths etc) to work on your workstation. 

- For the vacuum simulations: 
1. Starting with the pdb/xml files of the ligands, generate the corresponding amber files (prm7/rst7) using [qube_to_prmRst.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/FEP_preparation/qube_to_prmRst.py)
2. Remove the SOLTY flag and rename the amber files to SYSTEM.top and SYSTEM.crd
3. Generate the. MORPH.pert files using the scripts [morph_step1.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/HFE/scripts/morph_step1.py) and [morph_step2.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/HFE/scripts/morph_step2.py). These scripts read the parameters of the molecules and return the pert files for the discharge and the vanish steps.
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
5. Generate the. MORPH.pert files using the scripts [morph_step1.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/HFE/scripts/morph_step1.py) and [morph_step2.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/HFE/scripts/morph_step2.py).
6. Create the folder architecture and submit the simulations.

Analysis: 

`~/sire.app/bin/analyse_freenrg mbar` generates a dat file with the free energies for each step (discharge, vanish) for both legs. 

Corrections: 
- `FUNC.py`: Evaluates the electrostatic correction for the free energy change: FUNC_corr. This is run for lambda= 0 at the discharge leg.
- `~/sire.app/bin/lj-tailcorrection` Evaluates the end-point correction for the truncated vdW potentials. This is run for lambda= 0 and lambda= 1 of the vanish leg. 
DG_LJCOR = (LJ correction at lambda 1.0 ) - (LJ correction at lambda 0.0) )

To derive the hydration free energy, we use the following formula: 
**DDG_hyd = (DG_Vac_Discharge + DG_Vac_vanish) - (DG_Solv_Discharge + DG_Solv_vanish) + FUNC_corr + DG_LJCOR **
