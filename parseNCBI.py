#!/usr/bin/python

def searchNCBI():	
	from Bio.Blast import NCBIWWW	
	result_handle=NCBIWWW.qblast("blastn", "nt", "8332116")
	from Bio.Blast import NCBIXML
	blast_record= NCBIXML.read(result_handle)

	E_VALUE_THRESH = 0.01
	
	for alignment in blast_record.alignments:
		for hsp in alignment.hsps:
			if hsp.expect < E_VALUE_THRESH:
				print('****Alignment****')
				print('sequence:', alignment.title)
				print('length:', alignment.length)
				print('e value:', hsp.expect)
	

searchNCBI()
	

	
