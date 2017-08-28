#!/usr/bin/python

geneCounts={}
exonCounts={}
mRNACounts={}
CDSCounts={}
geneMean={}
exonMean={}
mRNAMean={}
CDSMean={}
assemblers={}
taxlist=set()

with open("boa_output_all.txt") as f, open("assemblerdata_8_17.csv", "w") as assemblerfile:
    for line in f:
        #print (line)
        taxid= line[line.index('[')+1:line.index(']')]
        taxlist.add(taxid)
        value= line[line.index('=')+1:].rstrip()
        
        if line.startswith('geneCounts'):
            geneCounts[taxid]=value
        elif line.startswith('exonCounts'):
            exonCounts[taxid]=value
        elif line.startswith('mRNACounts'):
            mRNACounts[taxid]=value    
        elif line.startswith('CDSCounts'):
            CDSCounts[taxid]=value    
        elif line.startswith('geneMean'):
            geneMean[taxid]=value
        elif line.startswith('exonMean'):
            exonMean[taxid]=value
        elif line.startswith('mRNAMean'):
            mRNAMean[taxid]=value    
        elif line.startswith('CDSMean'):
            CDSMean[taxid]=value        
        elif line.startswith('Assembler'): # FIXME for one genome we may have different assembler, it is not unique.
            # assemblers[taxid]=value
            value = line[line.index('][') + 2:line.index('] =')]
            assemblerfile.write(str(taxid)+ ","+str(value)+"\n")
          
        
print(len(taxlist),len(assemblers),len(geneCounts),len(geneMean), len(exonCounts),len(exonMean),len(mRNACounts),len(mRNAMean),len(CDSCounts),len(CDSMean))

with open("boacsv_8_17.csv",'w') as out:
    for taxid in taxlist:
        if taxid not in geneCounts:
            geneCounts[taxid]=0
            geneMean[taxid]=0
        if taxid not in exonCounts:
            exonCounts[taxid]=0
            exonMean[taxid]=0
        if taxid not in mRNACounts:
            mRNACounts[taxid]=0    
            mRNAMean[taxid]=0    
        if taxid not in CDSCounts:
            CDSCounts[taxid]=0
            CDSMean[taxid]=0


        out.write(str(taxid) + ","+ str(geneCounts[taxid])+ ","+ str(geneMean[taxid])+ ","+ str(exonCounts[taxid])+ ","+ str(exonMean[taxid])+ ","+ str(mRNACounts[taxid])+ ","+ str(mRNAMean[taxid])+ ","+ str(CDSCounts[taxid])+ ","+ str(CDSMean[taxid])+"\n")
        #assemblerfile.write(str(taxid) + ","+ str(geneCounts[taxid])+ ","+ str(geneMean[taxid])+ ","+ str(exonCounts[taxid])+ ","+ str(exonMean[taxid])+ ","+ str(mRNACounts[taxid])+ ","+ str(mRNAMean[taxid])+ ","+ str(CDSCounts[taxid])+ ","+ str(CDSMean[taxid])+"\n")


        