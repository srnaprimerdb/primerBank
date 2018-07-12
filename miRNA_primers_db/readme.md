## The current directory includes:
	1. srnaprimer_miRNA_results.db is a databases file contains miRNA primers results.
 	2. srnaprimer_query.py is a program for querying the priemr results from srnaprimer_miRNA_results.db.

## Use of help for queries:
	because different primer design method produces different output formats result, here we have four query

## commands for method A to I. 

if design method is A-F: 
```
	python srnaprimer_query.py A2F "RNA_id=='esi-miR3464-5p' and Experient_Method=='A'" > query_result.txt
``` 
else if design method is G: 
```
	python srnaprimer_query.py G "RNA_id=='esi-miR3464-5p' and Experient_Method=='G'" > query_result.txt
```
else if design method is H:
```
	python srnaprimer_query.py H "RNA_id=='esi-miR3464-5p' and Experient_Method=='H'" > query_result.txt
```
else design method is I:
```
	python srnaprimer_query.py I "RNA_id=='sv40-miR-S1-3p' and Experient_Method=='I'" > query_result.txt
```

# for more details result, please try online tools:  http://www.srnaprimerdb.com/ or http://123.57.239.141/.
