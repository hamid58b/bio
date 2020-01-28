import os
import sys
import operator

seq_cluster_Dict = {}
cluster_Dict= {}

def read_seq_cluster(seq_cluster_file):
    with open(seq_cluster_file, "r") as f:
        for line in f:
            seq_id = line[:line.index(":")]   # WP_094632576:10000009
            clstr_id = line[line.index(":") + 1:].rstrip()
            seq_cluster_Dict[seq_id] = clstr_id

def read_clusters(clstr_file):
    cluster_Dict.clear()
    with open(clstr_file, "r") as cluster_file:
        for line in cluster_file:
            clstr_id = line[:line.index(":")]  # 1000003:1359185=1;784=2
            tax_row = line[line.index(":") + 1:].rstrip()
            cluster_Dict[clstr_id] = tax_row

# this returns the top(3) most frequent taxa
def get_top3_tax(line):
    taxDic = dict()
    tax_list = line.split(";")
    taxDic.clear()
    for i in range(len(tax_list)):
        tax_id = tax_list[i][:tax_list[i].index("=")]
        tax_count = int(tax_list[i][tax_list[i].index("=") + 1:])
        taxDic[tax_id] = tax_count

    #Sort the dic and return the top(3)
    sorted_taxDic = sorted(taxDic.items(), key=operator.itemgetter(1), reverse=True)
    return (sorted_taxDic[:3])

    return (taxDic)

def compare_taxa_set(seq_top3, clstr_top3):
    # [('300852', 4), ('10090', 3), ('146786', 2)]
    seq_set=set()
    clstr_set = set()
    for item in seq_top3:
        seq_set.add(item[0])

    for item in clstr_top3:
        clstr_set.add(item[0])
    print(seq_set, clstr_set)
    common_taxa = len (seq_set.intersection(clstr_set))
    return (common_taxa)



def verify_conflicts(sequence_file):
    taxDic = dict()
    with open(sequence_file, "r") as seq_file:
        for line in seq_file:    # 1A43:11676=1;11698=4
            if line.find(":") != -1:
                row_id = line[:line.index(":")]
                row_tax = line[line.index(":") + 1:].rstrip()
                seq_top3= get_top3_tax(row_tax) #

                #get the cluster of this sequence
                if row_id in seq_cluster_Dict:
                    clstr_id = seq_cluster_Dict[row_id]
                    if clstr_id in cluster_Dict:
                        # TODO: important check if all clusters are here
                        row_tax = cluster_Dict[clstr_id]

                        #get the top3 of the cluster
                        clstr_top3 = get_top3_tax(row_tax)
                        # print("row tax for cluster: ")
                        # print(row_tax)
                        # print("clstr-top3: ")
                        # print(clstr_top3)


                    #check top3 of cluster vs sequence
                    #TODO: check top1, top2, top3 if they are the same or not?
                    try:
                        print(row_id, clstr_id)
                        print ("common" + str(compare_taxa_set(seq_top3,clstr_top3)))
                    except:
                        print("error compare 2 sets ")

                    # try:
                    #     if seq_top3[0][0] != clstr_top3[0][0]:
                    #         print("#####conflicts1: ")
                    #         print(seq_top3[0][0],clstr_top3[0][0] )
                    #         print(seq_top3, clstr_top3)
                    #
                    # except:
                    #     print("error compare seq top3 and clstr top3 ")




                else:
                    print("seq id is not in a dictionary file")
read_seq_cluster(sys.argv[1])
read_clusters(sys.argv[2])
verify_conflicts(sys.argv[3])
