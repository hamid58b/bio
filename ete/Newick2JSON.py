#!/usr/bin/python

'''
 Convert nwk format to json
 the tree has annotated with list of leaves 
'''

import sys
from ete3 import Tree, NCBITaxa
import random
import pandas as pd
import numpy as np


ncbi = NCBITaxa()
df=pd.read_csv("stats(OLD).csv", names=['taxid','CDS','CDS_length','exon','exon_length','gene','gene_length','mRNA','mRNA_length'])
taxid_list=df['taxid']

  # call get_leaves_taxid
  #  nodeset=set()
  #   nodeset.add(int(node.name))
  #   taxid_list=get_leaves_taxid(nodeset)

def get_leaves_taxid(nodeset):

    gff_set = set()

    for nodeid in nodeset:
        for taxid in taxid_list:
            try:
                if nodeid in ncbi.get_lineage(taxid):
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

    nodes=[node.name]
    if node.name != "" and node.children:
        node_Name= ncbi.translate_to_names([int(node.name)])
        print("node name ------" + str(node_Name))

    nodeset=set()
    leaves_list=[]
    leaves_frame=pd.DataFrame();
    if node.name!="" and node.children:
        print("node name:" + node.name)
        taxid=int(node.name)
        nodeset.add(taxid)
        leaves_list=get_leaves_taxid(nodeset)
        print(leaves_list)
        print(df.loc[df['taxid'].isin(leaves_list)])
        leaves_frame=df.loc[df['taxid'].isin(leaves_list)]
        for index,row in leaves_frame.iterrows():
            print (row['taxid'], row['gene'])

    json = { "name": node.name, 
#             "display_label": node.name,
#             "duplication": dup,
#             "branch_length": str(node.dist),
#             "common_name": node.name,
#             "seq_length": 0,
             "leave":[ {"taxid":str(int(row['taxid'])),
                        "gene":str(row['gene']),
                        "gene_length":str(row['gene_length'])
                        } for index, row in leaves_frame.iterrows()], #  this format "leaves": ["L1", "L2", "L3"]
             "type": "node" if node.children else "leaf",
#             "uniprot_name": "Unknown",
             }
    print (json)
    if node.children:
        json["children"] = []
        for ch in node.children:
            json["children"].append(get_json(ch))
    return json


if __name__ == '__main__':
    if len(sys.argv) > 1:
        t = Tree(sys.argv[1], format=1)
        print (t)

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
    with open ('convertedJson.json', 'w') as f:
        f.write(json)

