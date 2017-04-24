#!/usr/bin/python

import os
import subprocess
import numpy as np

'''
filter grep files;
1.length> 2k base pair
2.sp=1 single ungapped alignment
3.similarity btw 70% to 80%

TODO:
filter Query and subject with length first then run analysis

OUTPUT:
         QStart      QEnd     Score  SPs  DStart    DEnd  QAccession  DAccession
name of the Subject file and 
return the DStart and DEnd from the chain line NOT QStart and QEnd

'''
# verify if specific chain is preserved in all subject dds files?
# check +v and -v as a range
def check_chain(Qstart,v):
  files_list=[f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]
  #remove the query which is GCA_900079805.1_Fusarium_fujikuroi_IMI58289_V2_genomic.fna.dds.txt
  files_list.remove('GCA_900079805.1_Fusarium_fujikuroi_IMI58289_V2_genomic.fna.dds.txt')
  for subject in files_list:
    chains=np.loadtxt(subject, usecols=[1])
    rng=chains[(chains>Qstart-v) & (chains<Qstart+v)]
    print (rng)
    if len(rng)==0:
      return False
  return True

 
# get list of all dds files in the current directory and
# put it in a files_list
def filter_dds():
     files_list=[f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.dds')]
     for fileName in files_list:
	  greps=subprocess.check_output("grep 'Chain\|Similarity' " + fileName, shell=True)
	  with open("outgreps.txt", 'w') as outf:
	    outf.write(greps)

	  with open("outgreps.txt", "r") as f, open(fileName+".txt", 'w') as of:
	    for line in f:
	     chainLine= line.split()
	     if int(chainLine[4])==1:
	       simLine=f.next()
	       # check if the lenght is >2k
	       # and the similarity btw 70% and 90%
	       simLine=simLine.split()
	       simValue=simLine[6]
	       if int(chainLine[2])-int(chainLine[1])>2000 and int(simValue[0:2])>70 and int(simValue[0:2])<80:
		 of.write(line)
		 print(chainLine)
		 print(simLine)
	     else:
	       for i in range(int(chainLine[4])):
		 f.next()



def main():
  #call filter the dds diles
  #filter_dds()
  #call check chain to find the presereved chains
  lineQ=np.loadtxt('GCA_900079805.1_Fusarium_fujikuroi_IMI58289_V2_genomic.fna.dds.txt', usecols={1,2,5,6})
  #print lineQ
  for x in lineQ: 
    if check_chain(x[0],200):
      print (x)
  #for chain in lineQ[:,0]:
    #if check_chain(chain,200):
    #  print("DStart= {} and DEnd={}" %())
    #print(chain)
    




main()
 
