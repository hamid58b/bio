
#!/usr/bin/python

import os
import subprocess


my_dic={}


def dl_from_ncbi(assembly_summary):
    # download fna and gff files from ftp
    with open (assembly_summary) as f:
        next(f)
        for line in f:
            info=line.split('\t')
            fna_url=info[19]+'/'+info[19].split('/')[-1]+'_genomic.fna.gz'
            fnafileName=info[19].split('/')[-1]+'_genomic.fna.gz'
            
            assembly_url=info[19]+'/'+info[19].split('/')[-1]+'_assembly_stats.txt'
            assembly_stat= info[19].split('/')[-1]+'_assembly_stats.txt'
        
            gff_url=info[19]+'/'+info[19].split('/')[-1]+'_genomic.gff.gz'
            gfffileName=info[19].split('/')[-1]+'_genomic.gff.gz'
            
            print(gfffileName)
            if not os.path.isfile(fnafileName):
                #os.system('curl -o ' + fnafileName + ' '  + fna_url)
                #os.system('curl -o ' + gfffileName + ' '  + gff_url)
                os.system('curl ' + assembly_url + '>>' + assembly_stat )
                print (" ################### "+ gfffileName)



data=subprocess.check_output("curl ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/", shell=True)
with open("data.txt", 'w') as f:
    f.write(data)

directory_list=[]
with open("data.txt") as f:
    for line in f:
        folders = line.split()
        if "." not in folders[8]:
            directory_list.append(folders[8])


for directory in directory_list:
    if not os.path.exists(directory):
        os.makedirs(directory)
        os.chdir(directory)
        try:
            assembly_summary = subprocess.check_output(
            "curl ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/"+ directory + "/assembly_summary.txt", shell=True)
            with open("assembly_summary.txt", 'w') as outf:
                outf.write(assembly_summary)
            dl_from_ncbi("assembly_summary.txt")

        except subprocess.CalledProcessError:
            print ("############## No Assembly_summary file ")

        os.chdir("..")