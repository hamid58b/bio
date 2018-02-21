#!/usr/bin/python


import pprint
# from BCBio import GFF

from BCBio.GFF import GFFExaminer
import os
import subprocess
import sys
import numpy as np
import operator

exon_no=0
def parse_gff(in_file):
    examiner = GFFExaminer()
    in_handle = open(in_file)

    gff = examiner.available_limits(in_handle)
    gff_features = gff['gff_type']
    print(gff_features)
    for feature in gff_features:
        if 'exon' in feature:
            # print(feature.sub_features)
            return (gff_features[feature])
    in_handle.close()

assembly_stats={}
def get_assembly(file):
    assembly_program=None
    with open(path+file, 'r') as f:
        for line in f:
            if line.startswith('# Assembly method:'):
                data=line.split(':')
                assembly_program = data[1].strip()

                print(data[1].strip())
    return assembly_program

# list all gff files
files_list=[f for f in os.listdir(".") if f.endswith('.gff')]
# print(files_list)

for f in files_list:
    exon_no = parse_gff(f)

    print(exon_no)
