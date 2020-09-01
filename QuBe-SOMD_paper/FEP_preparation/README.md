BioSimSpace protocols and scripts used to generate the input files for FEP calculations. 


**File Setup for Free Energy Calculations**

NB. For the example ligands provided you will need to use the protein files found in Protein/force_field/Group2.

*For use with **AMBER**:*
1) Protein setup: 
  - Given the four fragments of the protein in pdb format, we are going to use the [parameterise.py](https://github.com/michellab/BioSimSpace/blob/devel/nodes/playground/parameterise.py) script of BioSimSpace to parameterise them with the ff14SB amber forcefield.
  - Use the BioSimSpace python to run the following command: **run ./parameterise.py --input FILE.pdb --forcefield ff14SB --output FILE**
  - This will produce AMBER parameterised .rst7 and .prm7 files for each protein fragment.
  - Combine the protein fragments to get the whole protein:
  (e.g. biosimspace.app/bin/ipython)
  - Use the BioSimSpace python to run the following command: **run ./combine.py --system1 FILE_1.prm7 FILE_1.rst7 --system2 FILE_2.prm7 FILE_2.rst7 --output FILE_12**
  - The combining process is done three times to combine the four fragments together. 
  

2) Create AMBER ligand files for Sire:
  - Make a "Ligands" folder in which you will have the pdb files for each ligand and the parameterise.py script.
  - Navigate to ipython where you saved BioSimSpace.app (e.g. biosimspace.app/bin/ipython)
  - Run the following command: **run ./parameterise.py --input FILE.pdb --forcefield gaff2 --output FILE**
  - This will produce AMBER parameterised .rst7 and .prm7 files for each ligand.


*For use with **QUBE**:*
1) Fragmented protein combination
  - Given the four fragments of the protein in xml and pdb format, we are going to use the [qube_to_prmRst.py](https://github.com/cole-group/qube_project/blob/master/QuBe-SOMD_paper/FEP_preparation/qube_to_prmRst.py) to read the xml/pdb files and generate the corresponding amber files for each fragment:
  - Use the Sire python to run the following command: **~/sire.app/bin/ipython qube_to_prmRst.py -x fragX.xml -p fragX.pdb**
  - This will produce AMBER parameterised .rst7 and .prm7 files for each protein fragment.
  - The combining process to get the whole protein is the same as the one we did for the amber parameterisation:
  (e.g. biosimspace.app/bin/ipython)
  - Use the BioSimSpace python to run the following command: **run ./combine.py --system1 FILE_1.prm7 FILE_1.rst7 --system2 FILE_2.prm7 FILE_2.rst7 --output FILE_12**
  - The combining process is done three times to combine the four fragments together. 


2) Create QUBE ligand files to run with Sire:
  - Make a "Ligands" folder in which you will have the QUBE parameterised pdb and xml files for each ligand and the qube_to_prmRst.py script. Example ligands can be found in the "Ligands" folder above.
  - Navigate to ipython where you saved Sire.app (e.g. ~/sire.app/bin/ipython)
  - Run the following command in ipython: **run ./qube_to_prmRst.py -p FILE.pdb -x FILE.xml**
  - This will produce .rst7 and .prm7 files for each ligand.
  
*From here the setup is the same for either force field.* 
  
3) Solvate the ligands:
  - In the "Ligands" folder you should now copy in the solvate.py script.
  - Navigate to ipython where you saved BioSimSpace.app (e.g. biosimspace.app/bin/ipython)
  - Run the following command: **run ./solvate.py --input FILE.prm7 FILE.rst7 --output FILE_sol --water tip3p --extent 26**
  - This will create solvated, unbound ligand files (e.g. FILE_sol.prm7). The above is the box size used for our system.
  
4) Combine the ligands and protein:
  - Make a "Complex" folder in which you will need the (unsolvated) ligand and protein prm7 and rst7 files, and the combine.py script.
  - Nativage to the ipython in BioSimSpace.app (e.g. biosimspace.app/bin/ipython)
  - Run the following command in ipython: **run ./combine.py --system1 LigFILE.prm7 LigFILE.rst7 --system2 PROTEIN.prm7 PROTEIN.rst7 --output PROT_LigFILE**
  - This will create unsolvated prm7 and rst7 files for the ligand in complex with the protein.
  
5) Solvate the complex:
  - Still within the "Complex" folder you will now also need the solvate.py script.
  - Nativage to the ipython in BioSimSpace.app (e.g. biosimspace.app/bin/ipython)
  - Run the following command in ipython: **run ./solvate.py --input PROT_LigFILE.prm7 PROT_LigFILE.rst7 --output Complex_sol --water tip3p --box_dim 88**
  - This will create solvated prm7 and rst7 files of the ligand in complex with the protein. The above is the box size used for our system.
  
6) Equilibrate the solvated systems:
  - Both the solvated complexes and ligands need to equilibrated, this will be conducted in both the "Complex" and "Ligands" folders respectively. You will now also need the amberequilibration.py script in both of these folders.
  - Nativage to the ipython in BioSimSpace.app (e.g. biosimspace.app/bin/ipython)
  - Run the following command for both bound and unbound ligand systems: **run ./amberequilibration.py --input FILE_sol.prm7 FILE_sol.rst7 --output FILE_sol_eq**
  - This will create equilibrated rst7 files for the bound and unbound systems (e.g. Lig_sol_eq.rst7 or Complex_sol_eq.rst7)
  
7) Generate the files for free energy calculations:
  - Make a "Perturbations" folder in which you will need the final prm7 and equilibrated rst7 files for both environments (e.g. ligands in complex with the protein, and ligands unbound in solution). You will also need the prepareFEP.py script.
  - Nativage to the ipython in BioSimSpace.app (e.g. biosimspace.app/bin/ipython)
  - Run the following command for both bound and unbound environments: **run ./prepareFEP.py --input1 FILE1_sol.prm7 FILE1_sol_eq.rst7 --input2 FILE2_sol.prm7 FILE2_sol_eq.rst7 --output FILE1_to_FILE2**
  - This will create the perturbation files for your free energy calculations (e.g. for a transition of Lig1 to Lig2 the above command will create .mapping, .mergeat0.pdb. .pert, .prm7 and .rst7 files for this pertubration, both bound and unbound). 
