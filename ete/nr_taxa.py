
import random

from ete3 import NCBITaxa
ncbi = NCBITaxa()
# ncbi.update_taxonomy_database()



# todo: first get all protein deflines from nr (start with >)
# example one line from nr:
# >WP_000332037.1 MULTISPECIES: ribonucleoside-diphosphate reductase 1 subunit beta [Proteobacteria]^ANP_311145.1 ribonucleoside-diphosphate reductase 1 beta subunit ferritin-like protein [Escherichia coli O

distinct_taxa = set()

with open("nr_deflines_top10",'r') as nr:
    for line in nr:
        deflines = line.split("\x01")
        for item in deflines:
            # print(item)
            try:
                tax_name = item[item.index("[")+1:-1]
                # print(tax_name)
                distinct_taxa.add(tax_name)

            except:
                print("Error")
                # print(item)

print(len(distinct_taxa))

with open("nr_taxlist", "w") as nr_taxlist:
    for item in distinct_taxa:
        nr_taxlist.write(item+"\n")
        #
        # # print(distinct_taxa)
        # for item in distinct_taxa:
        #     name2taxid = ncbi.get_name_translator([item])
        #     print(name2taxid)
        #
        #     if len(name2taxid) > 0:
        #         tax_id = name2taxid[item][0]
        #         print(tax_id)
        #         lineage = ncbi.get_lineage(tax_id)
        #         print(lineage)
        #         lineage2ranks = ncbi.get_rank(lineage)
        #         print(lineage2ranks)
        #
        #         ranks2lineage = dict((rank, taxid) for (taxid, rank) in lineage2ranks.items())
        #         try:
        #             phyl =ranks2lineage['phylum']
        #             print(phyl)
        #         except:
        #             print("no phylum")
        #
        #         #TODO: now how to find a tax id that its phylum is not phyl
        #         # get all taxa from nr and put it in the txt file
        #         # read to a list and take random from the list
        #             # check its phylum by getting lineage and ...
        #


def get_ranks(taxid, desired_rank):
    lineage = ncbi.get_lineage(taxid)
    lineage2ranks = ncbi.get_rank(lineage)

    ranks2lineage = dict((rank, taxid) for (taxid, rank) in lineage2ranks.items())

    return (ranks2lineage[desired_rank])

def get_taxid(tax_name):
    name2taxid = ncbi.get_name_translator([tax_name])
    if len(name2taxid) > 0:
        tax_id = name2taxid[tax_name][0]

    return (tax_id)


def get_nr_taxlist(nr_file):
    with open(nr_file, "r") as f:
        nr_taxlist = f.read().splitlines()
        print("nr tax list size:")
        print(len(nr_taxlist))

    rand_items = random.sample(nr_taxlist, 2)
    print(rand_items)

    #TODO: now write a function that gets phylum of each of these randomly selected.


    # convert tax name to tax id
    name2taxid = ncbi.get_name_translator([rand_items[0]])
    tax_id = get_taxid(rand_items[0])

    current_rank_id=''
    # get desired rank for  taxid
    current_rank_id = get_ranks(tax_id, 'phylum')
    print("current_rank_id: ", current_rank_id)

    # take another sample from nr taxa list and check if its phyla is different then misaanotate it
    while True:
        random_tax = random.sample(nr_taxlist,1)
        if current_rank_id != get_ranks(get_taxid(random_tax[0]), 'phylum'):
            print("find random misann")
            print(" random rank: ",get_ranks(get_taxid(random_tax[0]), 'phylum'))
            print(random_tax)
            break



get_nr_taxlist("nr_taxlist")
