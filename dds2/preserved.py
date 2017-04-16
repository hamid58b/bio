#!/usr/bin/python

import numpy as np
import sys
import os
import subprocess

def getAvg(strfile):
	lines= np.loadtxt(strfile,  usecols=[2])
	avg=sum(lines)/len(lines)
        return(avg)

def main():
  linesQ=np.loadtxt("grepQ.txt", usecols={1,2})
  linesS=np.loadtxt("grepS.txt", usecols={1,2})
  
  for chain in linesQ[:,0]:
    QStart=linesS[:,0]
    rng=QStart[(QStart>chain-200) & (QStart< chain+200)]
    print(" Qstart {} size= {}, subject Qstart {}".format(line,len(rng), rng) )
  
  #print (linesQ[:,0])
  #a=np.array([1,20,30, 24,15,23,30,45])
  #rng=a[(a>5) & (a<25)]
  
  

if __name__=="__main__":
   #main(sys.argv[1:])
   main()
