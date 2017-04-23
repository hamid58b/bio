#!/usr/bin/python

mport os
import subprocess
import numpy as np

tolerance=500
'''
filter grep files;
1.length> 2k base pair
2.sp=1 single ungapped alignment
3.similarity btw 70% to 80%
'''
# verify if specific chain is preserved in all subject dds files?
# check +v and -v as a range
def check_chain(Qstart):
  filesgrep=[f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt') and f.startswith('GCA')]
  #remove the query which is GCA_900079805.1_Fusarium_fujikuroi_IMI58289_V2_genomic.fna.dds.txt
  filesgrep.remove('GCA_900079805.1_Fusarium_fujikuroi_IMI58289_V2_genomic.fna.dds.txt')
  #print(filesgrep)
  coverage=[]
  for f in filesgrep:
    chains=np.loadtxt(f, usecols=[1])
    #print(chains)
    rng=chains[(chains>Qstart-tolerance) & (chains<Qstart+tolerance)]
    if len(rng)>0:
      coverage.append(f)# if the chain is covered by file f then add to the list of coverage files
  return(len(coverage), coverage)



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
              if int(chainLine[4])==1: # if SP=1 then read the seconf line
                simLine=f.next()
                # check if the lenght is >2k
                # and the similarity btw 70% and 90%
                simLine=simLine.split()
                simValue=simLine[6]
                if int(chainLine[2])-int(chainLine[1])>1000 and int(simValue[0:2])>70 and int(simValue[0:2])<90:
                  of.write(line)
                  print(chainLine)
                  print(simLine)
              else:
               for i in range(int(chainLine[4])):
                 f.next()


def get_Dstart_Dend(subjectFile, Qstart):
    chains=np.loadtxt(subjectFile, usecols={1,2,3,4,5,6})
    for i in range(len(chains)):
      if chains[i][0]>Qstart-tolerance and chains[i][0]<Qstart+tolerance:
           #print (chains[i])
           return(chains[i])


def main():
  #call filter the dds diles
  #filter_dds()
  #call check chain to find the presereved chains
  lineQ=np.loadtxt('GCA_900079805.1_Fusarium_fujikuroi_IMI58289_V2_genomic.fna.dds.txt', usecols={1,2,5,6})
  for x in lineQ:
    if x[0]==796615:  # 55770 or 796615 are covered by 26 files
      (coverNo, coverageFiles)=check_chain(x[0])
      print ("chain"+ str( x))
      print (coverNo)
      print (coverageFiles)
      for f in coverageFiles:
        #dstart, dend=get_Dstart_Dend(f,x[0])
        print("file: " + f)
        chain=get_Dstart_Dend(f,x[0])
        print("Chain {} {} {} {} {} {} \n".format( chain[0], chain[1],chain[2],chain[3],chain[4],chain[5]))

main()

