import csv
import pandas as pd
from ete3 import NCBITaxa

ncbi = NCBITaxa()

def get_desired_ranks(taxid, desired_ranks):
    lineage = ncbi.get_lineage(taxid)
    lineage2ranks = ncbi.get_rank(lineage)
    ranks2lineage = dict((rank, taxid) for (taxid, rank) in lineage2ranks.items())

    # return {'{}_id'.format(rank): ranks2lineage.get(rank, '<not present>') for rank in desired_ranks}
    return { ranks2lineage.get(rank, '<not present>') for rank in desired_ranks}

def main(taxids, desired_ranks, path):
    with open(path, 'w') as csvfile:
        fieldnames = ['{}_id'.format(rank) for rank in desired_ranks]
        writer = csv.DictWriter(csvfile, delimiter='\t', fieldnames=fieldnames)
        writer.writeheader()

        taxlist=set()

        for taxid in taxids:

            # print( ncbi.get_lineage(taxid))
            # print(get_desired_ranks(taxid, desired_ranks))
            rank1=dict()
            # print(taxid)
            try:
                rank1=get_desired_ranks(int(taxid), desired_ranks)
            except:
                pass

            for item in rank1:
                taxlist.add(str(item))
        # print(taxlist)
        # print(len(taxlist))
        return (list(taxlist))

if __name__ == '__main__':

    df = pd.read_csv("taxList2_9_17.txt", names=['name', 'taxid'])
    taxid_list = df['taxid']
    # print(df)

    #desired_ranks = ['kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species']
    desired_ranks = ['kingdom', 'phylum', 'class', 'order','family', 'genus']
    path = 'taxids.csv'
    taxids=taxid_list.values.tolist()
    # print(taxids)

    resolved=main(taxids, desired_ranks, path)
    print(type(resolved))

    df_selected = df.loc[df['taxid'].isin(resolved)]
    print(df_selected)
    df_selected.to_csv(r'out_taxids.txt', header=None, index=None, sep=',', mode='a')

    # with open("resolved.txt","w") as outf:


