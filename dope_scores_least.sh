npdb=$(grep npdb dope_scores.py | head -n 1 | awk '{ print $3 }')

for i in $(seq $npdb); do echo "$i";done > col1 
paste col1 dope_scores.csv > dope_scores_.csv

n=$(cut -f2 dope_scores_.csv | awk '{print $4}' | sort -n | head -1) 
grep -e $n dope_scores_.csv | awk '{print "\n\n Find all DOPE scores in dope_scores.csv \n\n PDB Model #" $1 " exhibits least DOPE score = " $5 "\n\n"}'

rm col1
mv dope_scores_.csv dope_scores.csv
