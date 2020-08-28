Here are all the files (scripts and results) with the single point energies of proteins and other molecules.
These are used to validate the correct implementation of new methods/features in SOMD and the correct parsing of input files.
- The "protein-fragments" folder contains files with the single point energies of proteins, and the protein fragments.
- The "molecules" folder contains input files of small molecules to calculate single point energies.
- test_combRules.py: Compares Sire and SOMD SPEs using both the geometric and arithmetic combining rules 
- fragment_energetics.py, protein_energetics.py: Computes the OpenMM energy of the protein fragments and the protein
- sire_nrg_calc.py: Computes single point energies with Sire. Usage: ~/sire.app/bin/ipython sire_nrg_calc.py -x MOL.xml -p MOL.pdb
