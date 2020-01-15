from ete3 import NCBITaxa
ncbi = NCBITaxa()

# parse all nr deflines and get all the distinct taxa
# example one line from nr defline:
# >WP_000332037.1 MULTISPECIES: ribonucleoside-diphosphate reductase 1 subunit beta [Proteobacteria]^ANP_311145.1 ribonucleoside-diphosphate reductase 1 beta subunit ferritin-like protein [Escherichia coli O

distinct_taxa = set()

def get_taxid(tax_name):
    name2taxid = ncbi.get_name_translator([tax_name])
    if len(name2taxid) > 0:
        tax_id = name2taxid[tax_name][0]

    return (tax_id)


# this finds all taxa from the nr database deflines
def main():
    try:

        with open("/Users/hbagheri/Downloads/tmp/nr_deflines",'r') as nr:
            for line in nr:
                deflines = line.split("\x01")
                for item in deflines:
                    # print(item)
                    try:
                        tax_name = item[item.rfind("[")+1:item.rfind("]")]
                        distinct_taxa.add(get_taxid(tax_name))

                    except:
                        print(item)
                        # print(item)

        print(len(distinct_taxa))

        with open("nr_taxa_list", "w") as nr_taxlist:
            for item in distinct_taxa:
                nr_taxlist.write(item+"\n")

    except:
        print("error in the process")

'''
One Boa query:

1APH:9606=2;9798=1;9823=50;9913=104;9940=5
1AR1:10090=2;266=6
1AS5:32630=1;41690=1
1ATI:10090=3;146786=2;300852=4;4932=1;4952=1;559292=1;562=2;9606=1;9823=2
1AU1:32630=5;9606=3
1AVZ:11676=1;9606=5
1AWI:4212=1;9606=1
1AXC:3702=10;9606=5
1AY1:10090=2;271=2
1AY7:1390=2;1894=1
1AYN:169066=8;31708=25;9606=2

'''

def get_all_taxa(boa_output):
    distinct_taxa.clear()
    with open(boa_output,'r') as f:
        for line in f:
            line_tax = line[line.index(":")+1:]
            tax_array = line_tax.split(";")
            for item in tax_array: #10090=3
                distinct_taxa.add(item[:item.index("=")])

    with open("nr_taxa_list_from_Boa", "w") as nr_taxlist:
        for item in distinct_taxa:
            nr_taxlist.write(item + "\n")

get_all_taxa("part-r-00000_converted")
print(len(distinct_taxa))