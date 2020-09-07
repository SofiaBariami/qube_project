- amberFF_files: Contains the pdb files of the proteins' fragments (for ligand groups 1 and 2) that can be parameterised with ff14SB
- qube_files: Contains the xml/pdb files of the proteins' fragments (for ligand groups 1 and 2) that are paremetrised with QuBe along with instructions 
on how to get the correstonding amber-type files for further processing with SOMD. 


###XML generation

**Chris, plese upload the onetep and pdb files needed as input to qubekit-pro. Also include parmed scripts described below, ie everything needed to run the calculations performed in the paper**

Practically, creating the files via QUBEKit is done simply through the command line interface. Navigating to a directory containing the ONETEP output file and the relevant pdb files, the command ```QUBEKit-pro -build <name of pdb>``` will perform the necessary steps.

Using the files

A combination of OpenMM and ParmEd is used to analyse the files. This is done by creating an OpenMM system in the usual way for the first fragment, then each successive fragment is loaded into this same system. Since QUBEKit uses geometric combination rules for the Lennard-Jones parameters (rather than Amber’s arithmetic combination rules), a small change is made to the OpenMM system object to allow for this. Having built the system with OpenMM, the energetics are calculated for the whole system, then using ParmEd, a full breakdown of each contributor is obtained (energy from bonds, angles, torsions and non-bonded). These energy results can then be compared with the energies computed using our SOMD interface as a check.
