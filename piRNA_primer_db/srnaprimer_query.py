import sqlite3, sys

# example:
# for method A-F: 
# 	python srnaprimer_query.py A2F "RNA_id=='mmu_piR_029704' and Experient_Method=='A'"
# for method G:
#	python srnaprimer_query.py G "RNA_id=='mmu_piR_029704' and Experient_Method=='G'"
# for method H:
#	python srnaprimer_query.py H "RNA_id=='mmu_piR_029704' and Experient_Method=='H'"
# for method I:
#	python srnaprimer_query.py I "RNA_id=='mmu_piR_029704' and Experient_Method=='I'"
#	

conn = sqlite3.connect('srnaprimer_piRNA_results.db')
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



print ("------------------------------------------------------------------------------")
print (query)
print ("------------------------------------------------------------------------------")
print ()


curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print ('%s: %s' % pair)
    print()

curs.close()
conn.commit()
conn.close()