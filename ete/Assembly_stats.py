import os
import sys

#sys.stdout=open("assembly_stats01312018.txt", "w+")

# list all assembly statistics files
files_list=list()
for path, subdirs, files in os.walk("/Users/hbagheri/Documents/NCBI/testncbi/fish"):
    for name in files:
        if name.endswith('assembly_stats.txt'):
            #print (name, os.path.join(path, name))
            files_list.append(os.path.join(path, name))

with open("assembly_stats022018(Fish).csv", 'w') as outf:
    for f in files_list:
        taxtid = ""
        genome_name = ""
        total_length = "0"
        total_gap_length = "0"
        scaffold_count = "0"
        scaffold_N50 = "0"
        contig_count = "0"
        contig_N50 = "0"
        with open(f, "r") as in_file:
            for line in in_file:
                row = line.split()
                if line.startswith('# RefSeq assembly accession:'):
                    genome_name=row[4]
                    print(genome_name)
                if line.startswith('# Taxid'):
                    taxtid=row[2]
                if line.startswith('all	all	all'):
                    if row[4]=='total-length':
                        total_length=row[5]
                    if row[4] == 'total-gap-length':
                        total_gap_length = row[5]
                    if row[4] == 'scaffold-count':
                        scaffold_count = row[5]
                    if row[4] == 'scaffold-N50':
                        scaffold_N50 = row[5]
                    if row[4] == 'contig-count':
                        contig_count = row[5]
                    if row[4] == 'contig-N50':
                        contig_N50 = row[5]
        outf.write(genome_name + "," + taxtid + "," + total_length + "," +
                   total_gap_length + "," + scaffold_count + "," + scaffold_N50 + "," +
                   contig_count + "," + contig_N50 + "\n")