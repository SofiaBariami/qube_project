We use *qube_to_prmRst.py* to read the xml/pdb files of the protein fragments and save the amber files. 
Then we combine the fragments to get the whole protein.
Single Point Energy calculations both for the fragments and for the whole protein calculated with SOMD and OpenMM prove that the file conversion works fine.
Folders "Group1" and "Group2" contain the qube files (pdb/xml) of the protein fragments and the amber files (prm7/rst7) of the whole proteins that were used 
with the respective set of ligands. 
