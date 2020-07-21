This folder contains the xml files for the proteins.

### Creating the files

An extension to QUBEKit, QUBEKit-pro (meaning protein) is used to generate the xml files from the pdb and ONETEP output files. Using QUBEKit as a base has the advantage that most features can be easily applied to the protein, allowing for charge checking and symmetrisation, for example.

QUBE-pro builds the xml by first reading the pdb file to get the full topology of the protein or fragment. This gives atom types, positions and bonds, as well as some other information such as the amino acids and if the protein is split into subunits. At this stage, certain groups of atoms are picked out for later symmetrisation such as hydrogens on the same methyl or amine groups. 

With the structure stored, a parametrisation step is performed (Allen, 2019). A general protein xml contains bonded parameters for all atoms in the amino acids (and the caps such as NME or ACE). This general xml is used to map parameters to the protein in question, using the now stored structure. Non-bonded data is, for now, ignored since this comes from the ONETEP output file.

The requisite information is extracted from the ONETEP file. For each atom, this is the partial charge and the effective volume. These parameters are then used to calculate the Lennard-Jones parameters via atom-in-molecule electron density partitioning (Cole, 2016). Following this calculation, the atoms previously marked for symmetrisation are symmetrised. These parameters are then stored for use in producing the final xml file.

QUBEKit is then used to write the pdb and xml files; if the protein consists of two or more fragments, these fragments are returned as separate files. Since each atom in the protein is in a unique environment, and therefore has unique charge and Lennard-Jones parameters, each atom in QUBEKit-pro is assigned a unique type. This means the entire protein to be treated as a single molecule rather than a collection of residues with fixed atom types.

Practically, creating the files via QUBEKit is done simply through the command line interface. Navigating to a directory containing the ONETEP output file and the relevant pdb files, the command `QUBEKit-pro -build <name of pdb>` will perform the necessary steps described above.

### Using the files

A combination of OpenMM and ParmEd is used to analyse the files. This is done by creating an OpenMM system in the usual way for the first fragment, then each successive fragment is loaded into this same system. Since QUBEKit uses geometric combination rules for the Lennard-Jones parameters (rather than Amber’s arithmetic combination rules), a small change is made to the OpenMM system object to allow for this. Having built the system with OpenMM, the energetics are calculated for the whole system, then using ParmEd, a full breakdown of each contributor is obtained (energy from bonds, angles, torsions and non-bonded). These energy results can then be compared with the energies computed using our SOMD interface as a check.
