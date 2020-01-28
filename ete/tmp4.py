import operator
import os
import sys


x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

print(x)
print(sorted_x)
top1 = sorted_x[1]
print(sorted_x[1])
print(type(top1))
print(top1[1])

str1 = '123'
str2='123'
if str1 != str2:
    print("conflict")


# with open(sys.argv[1], "r") as rna_file:
#     for line in rna_file:
#         print(line.rstrip().replace("-", ''))

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        print(a_set.intersection(b_set))
    return (0)


a = [1, 2, 3, 4, 5,6]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_member(a, b))


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

compare_taxa_set([('300852', 4), ('10090', 3), ('146786', 2)], [('300852', 4), ('10090', 3), ('146786', 2)])