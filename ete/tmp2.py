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

# todo: randomly select 100k protein; then get list of all tax names for each protein
# TODO: then, convert name to tax id: name2taxid = ncbi.get_name_translator(['Homo sapiens', 'primates'])
# tax_list (p)= list of all tax ids of selected protein
# steps: get lineage for a protein p
# phyl_set= set of phylum(p)

# TODO: list of all tax ids from nr database

# assign a random tax id to p s.t phylum(tax) != phyl




# tree = ncbi.get_topology([984896])
# print (tree.get_ascii(attributes=["sci_name", "rank"]))

print(get_desired_ranks(984896))

print(get_desired_ranks(214092))

print(get_desired_ranks(5741))

print("--------")
print(ncbi.get_name_translator(['Campylobacter','Vibrio']))

# lineage = ncbi.get_lineage(9606)
# print (lineage)
#
#
#
# names = ncbi.get_taxid_translator(lineage)
# print ([names[taxid] for taxid in lineage])

