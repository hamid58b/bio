#!/usr/bin/python


from Bio import SeqIO

def parsegenebank(gbkfile):
	for seq_record in SeqIO.parse(gbkfile, "genbank"):
		print(seq_record.id)
		print(repr(seq_record.seq))
		print(len(seq_record))


parsegenebank("ls_orchid.gbk")
