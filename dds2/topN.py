#!/usr/bin/python

import numpy as np
import sys
import os
import subprocess

def getAvg(strfile):
	lines= np.loadtxt(strfile,  usecols=[2])
	avg=sum(lines)/len(lines)
        return(avg)

def main(argv):
        # list of all files with dds extension in the current directory
	files_list=[f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]
	fileAvg={}
	
	for f in files_list:
	    # run grep command to the selected file and
	    #write the result of the grep to a greps.txt file
	    #
	    greps=subprocess.check_output("grep Chain " + f, shell=True)
	    with open("greps.txt", 'w') as outf:
		outf.write(greps)
            
	    fileAvg[f]=getAvg("greps.txt")

	#print(max(fileAvg, key=fileAvg.get))	
        #print top N  which N is given as argument argv[0]
	print(sorted(fileAvg, key=fileAvg.get, reverse=True)[:int(argv[0])])

if __name__=="__main__":
   print(sys.argv[1:])
   main(sys.argv[1:])

