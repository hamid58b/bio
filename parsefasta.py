#! /usr/bin/python 


from Bio import SeqIO

def seq_parse(fastafile):	
	for seq_record in SeqIO.parse(fastafile, "fasta"):
		print(seq_record.id)
		print(repr(seq_record.seq))
		print(len(seq_record))


seq_parse("ls_orchid.fasta")
