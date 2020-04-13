import os
import numpy as np
import sys
import operator

'''
 following script runs over nr database 
 it takes Def Lines and calculates frequency of taxonomic assignmets
 input sample:
   >WP_000332037.1 MULTISPECIES: ribonucleoside-diphosphate reductase 1 subunit beta [Proteobacteria]^ANP_311145.1 ribonucleoside-diphosphate reductase 1 beta subunit ferritin-like protein [Escherichia coli O

 Output:
    SeqID, tax_stat{'taxid':tax_freq}
'''
tax_stat={}
with open(sys.argv[1], "r") as nr:
    for line in nr:
        tax_stat.clear()
        deflines = line.split("\x01")
        seq_id = line[1:line.index(" ")]
        for item in deflines:
            try:
                tax_name = item[item.index("[")+1:-1]
                if tax_name in tax_stat:
                    tax_stat[tax_name] += 1
                else:
                    tax_stat[tax_name] = 1

            except:
                print("Error in tax name")


    print(seq_id)
    print(tax_stat)

    #TODO: sort the tax dictionary by value to find the top 3 taxa for each seq id
    sorted_d = sorted(tax_stat.items(), key=operator.itemgetter(1))
    #get the top 3 and print in the file



'''
 Boa equivalent query:
 
    s: Sequence = input;
    tax_stat : output count [string][string] of int;
	foreach(i:int; def(s.annotation[i]))
	   tax_stat[s.seqid] [s.annotation[i].tax_name]<<1;
	   
	   

'''
