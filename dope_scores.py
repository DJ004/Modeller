from modeller import *
from modeller.scripts import complete_pdb

env = environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

# Number of MODELLER-generated PDBs
npdb = 10                             # CHANGE NUMBER OF MODELLER-GENERATED PDBs HERE

for i in range(1, npdb + 1):
    pdb_file = f"stach_7TM_mod.B999900{i:02d}.pdb"   # CHANGE NAME OF MODELLER-GENERATED PDBs HERE

    mdl = complete_pdb(env, pdb_file)

    # Select all atoms in the first chain
    atmsel = selection(mdl.chains[0])
    score = atmsel.assess_dope()

    print(f"{pdb_file}: DOPE = {score}")

# run: $ python3 dope_scores.py > dope_scores.log && grep -e 'DOPE score' dope_scores.log > dope_scores.csv && bash dope_scores_least.sh
