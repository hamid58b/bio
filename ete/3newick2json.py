#!/usr/bin/python

'''
     Convert nwk format to json
     the tree has annotated with list of leaves 
     First argument is the Newick file format
     Second Argument will be the generated JSON file (Equivalent to the Newick format)
     It needs boacsv data and assembler data to annotate each node in the tree
'''

import sys
from ete3 import Tree, NCBITaxa
import random
import pandas as pd
import numpy as np

lineage={}

ncbi = NCBITaxa()
df=pd.read_csv("boacsv_8_17.csv", names=['taxid','CDS','CDS_length','exon','exon_length','gene','gene_length','mRNA','mRNA_length'])
taxid_list=df['taxid']
df_assemblers=pd.read_csv("assemblerdata_8_17.csv", names=['taxid','assembler'])

for taxid in taxid_list:
    lineage[taxid]=ncbi.get_lineage(taxid)

  # call get_leaves_taxid
  #  nodeset=set()
  #   nodeset.add(int(node.name))
  #   taxid_list=get_leaves_taxid(nodeset)

def get_leaves_taxid(nodeset):

    gff_set = set()

    for nodeid in nodeset:
        for taxid in taxid_list:
            try:
                if nodeid in lineage[taxid]:
                    gff_set.add(taxid)
            except ValueError:
                print ("error in getting get_lineage()")
    return gff_set



def get_json(node):
    # Read ETE tag for duplication or speciation events
    if not hasattr(node, 'evoltype'):
        dup = random.sample(['N','Y'], 1)[0]
    elif node.evoltype == "S":
        dup = "N"
    elif node.evoltype == "D":
        dup = "Y"

    node.name = node.name.replace("'", '')

    node_Name=""
    if node.name != "" :
        node_Name= ncbi.translate_to_names([int(node.name)])
        node_Name=str(node_Name[0])
        print("node name ------" + str(node_Name))

    nodeset=set()
    leaves_list=[]
    assembler_frame=pd.DataFrame()
    leaves_frame=pd.DataFrame()
    if node.name!="" and node.children:
        taxid=int(node.name)
        nodeset.add(taxid)
        leaves_list=get_leaves_taxid(nodeset)
        leaves_frame=df.loc[df['taxid'].isin(leaves_list)]
        assembler_frame=df_assemblers.loc[df_assemblers['taxid'].isin(leaves_list)]

    json = {"name": node_Name.replace('\n','').replace("'",""),
            "taxid": node.name,
            # "display_label": node.name,
#             "duplication": dup,
#             "branch_length": str(node.dist),
#             "common_name": node.name,
#             "seq_length": 0,
#              "leaves":[ {"taxid":str(int(row['taxid'])),
#                         "gene":str(row['gene']),
#                         "gene_length":str(row['gene_length']),
#                         "exon": str(row['exon']),
#                         "exon_length": str(row['exon_length']),
#                         "mRNA": str(row['mRNA']),
#                         "mRNA_length": str(row['mRNA_length']),
#                         "CDS": str(row['CDS']),
#                         "CDS_length": str(row['CDS_length'])
#                         } for index, row in leaves_frame.iterrows()],  #  this format "leaves": ["L1", "L2", "L3"]
            "leaves": [[str(int(row['taxid'])),
                        str(row['gene']),
                        str(row['gene_length']),
                        str(row['exon']),
                        str(row['exon_length']),
                        str(row['mRNA']),
                        str(row['mRNA_length']),
                        str(row['CDS']),
                        str(row['CDS_length'])
                        ] for index, row in leaves_frame.iterrows()],  # this format "leaves": ["L1", "L2", "L3"]
            "assemblers":[str(row['assembler']) for index, row in assembler_frame.iterrows()],
            #              "leaves": [str(leaf) for leaf in leaves_list],  # this format "leaves": ["L1", "L2", "L3"]
            #              "type": "node" if node.children else "leaf",
            #             "leaves": [str(row) for index,row in leaves_frame.iterrows()],  # this format "leaves": ["L1", "L2", "L3"]
            #             "type": "node" if node.children else "leaf",
            #             "uniprot_name": "Unknown",
            }
    if node.children:
        json["children"] = []
        for ch in node.children:
            json["children"].append(get_json(ch))
    return json


if __name__ == '__main__':
    if len(sys.argv) > 2:
        t = Tree(sys.argv[1], format=1)

    else:
        # create a random example tree
        t = Tree()

        t.populate(100, random_branches=True)

#    t=Tree()
#    t.populate(10000, random_branches=True)
#    print(t)

    # TreeWidget seems to fail with simple quotes

    json=str(get_json(t))
    json=json.replace("'", '"')

    #print (json)
    with open (sys.argv[2], 'w') as f:
        f.write(json)

