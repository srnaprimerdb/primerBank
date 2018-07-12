import sqlite3, sys

# example:
# for method A-F: 
# 	python srnaprimer_query.py A2F "RNA_id=='esi-miR3464-5p' and Experient_Method=='A'"
# for method G:
#	python srnaprimer_query.py G "RNA_id=='esi-miR3464-5p' and Experient_Method=='G'"
# for method H:
#	python srnaprimer_query.py H "RNA_id=='esi-miR3464-5p' and Experient_Method=='H'"
# for method I:
#	python srnaprimer_query.py I "RNA_id=='sv40-miR-S1-3p' and Experient_Method=='I'"
#	

conn = sqlite3.connect('srnaprimer_miRNA_results.db')
curs = conn.cursor()

if sys.argv[1] == "A2F":
	method=""
if sys.argv[1] == "G":
	method="G"	
if sys.argv[1] == "H":
	method="H"
if sys.argv[1] == "I":
	method="I"
	
query = "SELECT * FROM "+method+"results WHERE %s" % sys.argv[2]


print ("-"*len(query))
print (query)
print ("-"*len(query))
print ("\n")


curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print ('%s: %s' % pair)
    print ("\n")

curs.close()
conn.commit()
conn.close()
