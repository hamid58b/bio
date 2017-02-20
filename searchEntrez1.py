#!/usr/bin/python

def searchEntrez1():
	from Bio import Entrez, SeqIO
	handle = Entrez.efetch(db="nucleotide", id="186972394", rettype="gb", retmode="text")
	record = SeqIO.read(handle, "genbank")
	handle.close()
	print(record)


searchEntrez1()
