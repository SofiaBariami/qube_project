BioSimSpace protocols and scripts used to generate the input files for FEP calculations. 


**File Setup for Free Energy Calculations**

*For use with **AMBER**:*
1) Protein setup - Sofia

2) Create AMBER ligand files for Sire:
  - Make a "Ligands" folder in which you will have the pdb files for each ligand and the parameterise.py script.
  - Navigate to ipython where you saved BioSimSpace.app (e.g. biosimspace.app/bin/ipython)
  - Run the followin command: **run ./parameterise.py --input FILE.pdb --forcefield gaff2 --output FILE**
  - This will produce AMBER parameterised .rst7 and .prm7 files for each ligand.


*For use with **QUBE**:*
1) Fragmented protein combination - Sofia

2) Create QUBE ligand files to run with Sire:
  - Make a "Ligands" folder in which you will have the QUBE parameterised pdb and xml files for each ligand and the qube_to_prmRst.py script.
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
  - This will create unsovated prm7 and rst7 files for the ligand in complex with the protein.
  
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
