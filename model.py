from modeller import *
from modeller.automodel import *

log.verbose()    # request verbose output
env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']


class MyModel(automodel):
    def special_restraints(self, aln):
    	rsr = self.restraints
	at = self.atoms
	
	#Residues to be alpha helices
	#rsr.add(secondary_structure.alpha(self.residue_range('82:C','95:C')))	  
	#rsr.add(secondary_structure.alpha(self.residue_range('212:D','227:D')))	   
	#rsr.add(secondary_structure.alpha(self.residue_range('368:E','382:E')))	   
	#rsr.add(secondary_structure.alpha(self.residue_range('1049:H','1064:H')))

    def select_atoms(self):
    	return selection(self) - selection(self.residue_range('1:', '37:'),
                                           self.residue_range('54:', '421:'))
					   
#For position-restraining regions using the above command, use residue numbers of the full-length model, NOT those of the known structures.

a = MyModel(env, 
		alnfile='protein_gmx_resnr.ali', 
		knowns='protein_gmx_resnr', 
		sequence='protein_final_mod')
		
a.starting_model = 1
a.ending_model = 10
a.make()

# After successfully generating model(s) using Modeller, 
# (1) Update the name of the modeller output file in dope_scores.py,
#
# (2) To calculate DOPE scores and select least energy protein model, copy-paste the following line and run it on a bash terminal
# python2 dope_scores.py > dope_scores.log && grep -e 'DOPE score' dope_scores.log > dope_scores.csv && sh dope_scores_least.sh
