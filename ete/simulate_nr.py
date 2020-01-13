from ete3 import NCBITaxa
ncbi = NCBITaxa()
# ncbi.update_taxonomy_database()


def get_desired_ranks(taxid):
    lineage = ncbi.get_lineage(taxid)
    print("lineage to rank: ")
    lineage2ranks = ncbi.get_rank(lineage)

    print(lineage2ranks)
    print()

    ranks2lineage = dict((rank, taxid) for (taxid, rank) in lineage2ranks.items())
    print(ranks2lineage['phylum'])

    return (ranks2lineage)

# todo: first get all protein deflines from nr (start with >)
# example one line from nr:
# >WP_000332037.1 MULTISPECIES: ribonucleoside-diphosphate reductase 1 subunit beta [Proteobacteria]^ANP_311145.1 ribonucleoside-diphosphate reductase 1 beta subunit ferritin-like protein [Escherichia coli O

def get_nr_taxlist(nr_file):
    with open(nr_file, "r") as f:
        nr_taxlist = f.readlines()
        print("nr tax list size:")
        print(len(nr_taxlist))


get_nr_taxlist("nr_taxlist")


distinct_taxa = set()
print("nr")
with open("nr_deflines_top10",'r') as nr:
    for line in nr:
        # print(line)
        distinct_taxa.clear()
        deflines = line.split("\x01")
        print(len(deflines))
        for item in deflines:
            # print(item)
            try:
                tax_name = item[item.index("[")+1:-1]
                # print(tax_name)
                distinct_taxa.add(tax_name)
            except:
                print("Error")
                # print(item)

        # print(distinct_taxa)
        for item in distinct_taxa:
            name2taxid = ncbi.get_name_translator([item])
            print(name2taxid)

            if len(name2taxid) > 0:
                tax_id = name2taxid[item][0]
                print(tax_id)
                lineage = ncbi.get_lineage(tax_id)
                print(lineage)
                lineage2ranks = ncbi.get_rank(lineage)
                print(lineage2ranks)

                ranks2lineage = dict((rank, taxid) for (taxid, rank) in lineage2ranks.items())
                try:
                    phyl =ranks2lineage['phylum']
                    print(phyl)
                except:
                    print("no phylum")

                #TODO: now how to find a tax id that its phylum is not phyl
                # get all taxa from nr and put it in the txt file
                # read to a list and take random from the list
                    # check its phylum by getting lineage and ...


# todo: randomly select 100k protein; then get list of all tax names for each protein
# TODO: then, convert name to tax id: name2taxid = ncbi.get_name_translator(['Homo sapiens', 'primates'])
# tax_list (p)= list of all tax ids of selected protein
# steps: get lineage for a protein p
# phyl_set= set of phylum(p)

# TODO: list of all tax ids from nr database

# assign a random tax id to p s.t phylum(tax) != phyl




# tree = ncbi.get_topology([984896])
# print (tree.get_ascii(attributes=["sci_name", "rank"]))

# print(get_desired_ranks(984896))
#
# print(get_desired_ranks(214092))
#
# print(get_desired_ranks(5741))
#
# print("--------")
# print(ncbi.get_name_translator(['Campylobacter','Vibrio']))

# lineage = ncbi.get_lineage(9606)
# print (lineage)
#
#
#
# names = ncbi.get_taxid_translator(lineage)
# print ([names[taxid] for taxid in lineage])

