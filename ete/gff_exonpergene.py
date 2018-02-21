import os
import sys

# Uncomment following line for actual analysis
# sys.stdout=open("exonpergene2018.txt", "w+")

# with open('exonpergene.txt',"w") as outf:


files_list=list()
for path, subdirs, files in os.walk("/Users/hbagheri/Documents/MyGithub/bio/ete"):
    for name in files:
        if name.endswith('.gff'):
            # print (name, os.path.join(path, name))
            files_list.append(os.path.join(path, name))


# list all gff files
# files_list=[f for f in os.listdir(".") if f.endswith('.gff')]
print(len(files_list))


for f in files_list:
    with open(f, "r") as in_file:
        print(f)
        taxtid = ""
        refseq_id = ""
        exon_list = list()

        for line in in_file:
            fields= line.split()
            if (len(fields)>10 and fields[2]=="exon"):
                sub_features=fields[8].split(";")
                exon_list.append(sub_features[1][7:])
                #print(fields[2] ,sub_features[1][7:])
            if line.startswith("##species"):
                taxid=line[line.index("=")+1:]
                # print(taxtid)
            if line.startswith("#!genome-build-accession"):
                refseq_id=line[line.index(":")+1:]
                # print(refseq_id, taxtid)


    avglist=list()
    #print(list1)
    exon_set=set(exon_list)
    for parent in exon_set:
        #print (parent, list1.count(parent))
        avglist.append(exon_list.count(parent))
    if len(avglist) > 0:
        print(refseq_id.rstrip("\n")+ "," + taxid.rstrip("\n") + "," +str("%0.2f" %(sum(avglist) / float(len(avglist)))))
    else:
        print(refseq_id.rstrip("\n")+ "," + taxid.rstrip("\n")+","+ "0")


