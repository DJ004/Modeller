# Example for: selection.assess_dope()

from modeller import *
from modeller.scripts import complete_pdb

env = environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

# Read a model previously generated by Modeller's automodel class

npdb = 10                                                     # CHANGE NUMBER OF MODELLER-GENERATED PDBs HERE

a=["%02d" % x for x in range(1,npdb+1)]
for i in a:
	mdl = complete_pdb(env, 'protein_final_mod'               # CHANGE NAME OF MODELLER-GENERATED PDBs HERE
                            +'.B999900%s.pdb'%(i))

	# Select all atoms in the first chain
	atmsel = selection(mdl.chains[0])
	score = atmsel.assess_dope()

# run: $ python2 dope_scores.py > dope_scores.log && grep -e 'DOPE score' dope_scores.log > dope_scores.csv && sh dope_scores_least.sh
