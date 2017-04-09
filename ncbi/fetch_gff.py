#!/usr/bin/python

import os


my_dic={}

# download fna and gff files from ftp
with open ('assembly_summary.txt') as f:
    i=0
    for line in f:
        info=line.split('\t')
        fna_url=info[19]+'/'+info[19].split('/')[-1]+'_genomic.fna.gz'
        fnafileName=info[19].split('/')[-1]+'_genomic.fna.gz'
        gff_url=info[19]+'/'+info[19].split('/')[-1]+'_genomic.gff.gz'
        gfffileName=info[19].split('/')[-1]+'_genomic.gff.gz'
        print(gfffileName)
        if not os.path.isfile(fnafileName):
            os.system('curl -o ' + fnafileName + ' '  + fna_url)
            os.system('curl -o ' + gfffileName + ' '  + gff_url)
            i+=1
        if i==10000:
            break







