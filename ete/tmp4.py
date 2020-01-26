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


with open(sys.argv[1], "r") as rna_file:
    for line in rna_file:
        print(line.rstrip().replace("-", ''))