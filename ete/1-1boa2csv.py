#!/usr/bin/python

import  csv
'''
 This script gets Boa output and genrates the 2 csv files:
 one for features stats and another csv file for assembly programs
 ID is Refseq not taxid, bacause taxid is not unique
'''
geneCounts={}
exonCounts={}
mRNACounts={}
CDSCounts={}
geneMean={}
exonMean={}
mRNAMean={}
CDSMean={}
assemblers={}
refseqlist=set()
taxlist={}

with open("boa_output1") as f, open("assemblerdata2018.csv", "w") as assemblerfile:
    for line in f:


        if line.startswith('Assembler'):  # FIXME for one genome we may have different assembler, it is not unique.
            # assemblers[taxid]=value
            taxid = line[line.index('[') + 1:line.index(']')]
            value = line[line.index('][') + 2:line.index('] =')]
            assemblerfile.write(str(taxid) + "," + str(value) + "\n")
        else:
            refseq = line[line.index('[') + 1:line.index(']')]
            taxid = line[line.index('][') + 2:line.index('] =')]
            refseqlist.add(refseq)
            taxlist[refseq] = taxid
            value = line[line.index('=') + 1:].rstrip()

            if line.startswith('geneCounts'):
                geneCounts[refseq]=value
            elif line.startswith('exonCounts'):
                exonCounts[refseq]=value
            elif line.startswith('mRNACounts'):
                mRNACounts[refseq]=value
            elif line.startswith('CDSCounts'):
                CDSCounts[refseq]=value
            elif line.startswith('geneMean'):
                geneMean[refseq]=value
            elif line.startswith('exonMean'):
                exonMean[refseq]=value
            elif line.startswith('mRNAMean'):
                mRNAMean[refseq]=value
            elif line.startswith('CDSMean'):
                CDSMean[refseq]=value

        
print(len(refseqlist), len(assemblers), len(geneCounts), len(geneMean),
      len(exonCounts), len(exonMean), len(mRNACounts), len(mRNAMean), len(CDSCounts), len(CDSMean))

reader = csv.reader(open('exonGene2018.csv', 'r'))
exon_per_gene = {}
for row in reader:
    k, v = row
    exon_per_gene[k] = v

with open("boacsv_12_17.csv",'w') as out:
    for refseq in refseqlist:
        if refseq not in geneCounts:
            geneCounts[refseq]=0
            geneMean[refseq]=0
        if refseq not in exonCounts:
            exonCounts[refseq]=0
            exonMean[refseq]=0
        if refseq not in mRNACounts:
            mRNACounts[refseq]=0
            mRNAMean[refseq]=0
        if refseq not in CDSCounts:
            CDSCounts[refseq]=0
            CDSMean[refseq]=0

        exonPerGene=0
        if refseq in exon_per_gene:
            exonPerGene=exon_per_gene[refseq]
            print("###refseq, exon per gene")
            print (refseq, exonPerGene)


        out.write(str(refseq) + ","+ str(taxlist[refseq]) + "," + str(geneCounts[refseq]) + "," +
                  str(geneMean[refseq]) + "," + str(exonCounts[refseq]) + "," + str(exonMean[refseq]) +
                  "," + str(mRNACounts[refseq]) + "," + str(mRNAMean[refseq]) + "," + str(CDSCounts[refseq]) +
                  "," + str(CDSMean[refseq]) + "," + str(exonPerGene) + "\n")
        #assemblerfile.write(str(taxid) + ","+ str(geneCounts[taxid])+ ","+ str(geneMean[taxid])+ ","+ str(exonCounts[taxid])+ ","+ str(exonMean[taxid])+ ","+ str(mRNACounts[taxid])+ ","+ str(mRNAMean[taxid])+ ","+ str(CDSCounts[taxid])+ ","+ str(CDSMean[taxid])+"\n")


        