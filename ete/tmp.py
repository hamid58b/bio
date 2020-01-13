from ete3 import Tree

'''
 reference for ete tree : http://etetoolkit.org/docs/latest/tutorial/tutorial_ncbitaxonomy.html
 
'''
def test1():
    t = Tree()
    # We create a random tree topology
    t.populate(15)
    print (t)
    # print (t.children)
    # print (t.get_children())
    # print(t.up)
    # print (t.name)
    print (t.dist)
    # print (t.is_leaf())
    # print (t.get_tree_root())
    # print (t.children[0].get_tree_root())
    # print (t.children[0].children[0].get_tree_root())
    # # You can also iterate over tree leaves using a simple syntax
    # for leaf in t:
    #   print (leaf.name)

def compare_trees():
    from ete3 import Tree
    t1 = Tree('(((a,b),c), ((e, f), g));')
    t2 = Tree('(((a,c),b), ((e, f), g));')
    rf, max_rf, common_leaves, parts_t1, parts_t2 = t1.robinson_foulds(t2)
    print(t1, t2)
    print ("RF distance is %s over a total of %s" % (rf, max_rf))
    print("Partitions in tree2 that were not found in tree1:", parts_t1 - parts_t2)
    print(    "Partitions in tree1 that were not found in tree2:", parts_t2 - parts_t1)

    # We can also compare trees sharing only part of their labels

    t1 = Tree('(((a,b),c), ((e, f), g));')
    t2 = Tree('(((a,c),b), (g, H));')
    rf, max_rf, common_leaves, parts_t1, parts_t2 = t1.robinson_foulds(t2)

    print( t1, t2)
    # print
    # "Same distance holds even for partially overlapping trees"
    # print
    # "RF distance is %s over a total of %s" % (rf, max_rf)
    # print
    # "Partitions in tree2 that were not found in tree1:", parts_t1 - parts_t2
    # print
    # "Partitions in tree1 that were not found in tree2:", parts_t2 - parts_t1

def get_distance():
    # Loads a tree with branch lenght information. Note that if no
    # distance info is provided in the newick, it will be initialized with
    # the default dist value = 1.0
    nw = """(((A:0.1, B:0.01):0.001, C:0.0001):1.0,
    (((((D:0.00001,I:0):0,F:0):0,G:0):0,H:0):0,
    E:0.000001):0.0000001):2.0;"""
    t = Tree(nw)
    print(t)
    #                              /-A
    #                    /--------|
    #          /--------|          \-B
    #         |         |
    #         |          \-C
    #         |
    #         |                                                  /-D
    #         |                                        /--------|
    # ---------|                              /--------|          \-I
    #         |                             |         |
    #         |                    /--------|          \-F
    #         |                   |         |
    #         |          /--------|          \-G
    #         |         |         |
    #          \--------|          \-H
    #                   |
    #                    \-E
    #
    # Locate some nodes
    A = t & "A"
    C = t & "C"
    # Calculate distance from current node
    print("The distance between A and C is", A.get_distance("C"))
    # Calculate distance between two descendants of current node
    print("The distance between A and C is", t.get_distance("A", "C"))
    # Calculate the toplogical distance (number of nodes in between)
    print( "The number of nodes between A and D is ", \
    t.get_distance("A", "D", topology_only=True))


def ncbi_tree():
    from ete3 import NCBITaxa
    ncbi = NCBITaxa()
    # tax_list =[9606, 9598, 10090, 7707, 8782]
    tax_list =[357,3846, 323620,1883,4575,32630]
    tree = ncbi.get_topology(tax_list)
    print(tree.get_ascii(attributes=["sci_name", "rank"]))
    print(tree)
    for tax in tax_list:
        print("distance: %f is %s" %(tax, tree.get_distance(str(tax))))

    name2taxid = ncbi.get_name_translator(['Agrobacterium',      'Expression',      'Glycine',      'Shinella',      'Streptomyces',      'Zea',      'standard',      'synthetic'])
    print(name2taxid) # the tax id is name2taxid['Bacteria']

ncbi_tree()

# compare_trees()

#get_distance()