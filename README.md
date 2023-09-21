#### This repository contains prerequisite files + more to be used while modelling proteins with Modeller

- `pdb2fasta.pl`
  - a perl script to obtain a FASTA sequence for a desired protein.
  - usage: `perl pdb2fasta.pl protein.pdb`
  > This FASTA sequence is to be used in the 'structure' part of `model.ali` whereas the 'sequence' part refers to the full sequence of that protein which can be obtained from Uniprot.
  - This perl script was created by Ranjit Vijayan in March 2006
  > (a former member of SBCB, Dept of Biochem, Uni of Oxford, and a Professor in the Dept of Biology, UAE Univ, as of Sep 2023)
  
- `model.ali`
  - an example alignment file (model.ali) to be used by Modeller

- `model.py`
  - an example python script (model.py) to be used to run Modeller
  - usage: `mod9.16 model.py` # check modeller version 

- `dope_scores.py` + `dope_scores_least.sh`
  - scripts to be used in conjunction to obtain DOPE scores of all protein models generated and determine the protein model number with least DOPE score
  - Instructions to run are provided at the end of the `model.py` script
