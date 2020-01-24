
import  os
import sys

seq_dic= {}
def parse_alignment(fasta_file):
    seq_id =""
    sequence = ""
    with open(fasta_file, "r") as f:
        for line in f:
            if line.startswith(">"):
                seq_id = line[1:line.index(" ")]
                sequence = ""
                seq_dic[seq_id] = ""

            else:
                sequence += line.rstrip()
                seq_dic[seq_id] += line.rstrip()


def chunkstring(string, length):
    seq_string= list(string[0+i:length+i] for i in range(0, len(string), length))

    sequence_line = ""
    for it in seq_string:
        sequence_line += it + " "

    return (sequence_line)


parse_alignment("/Users/hbagheri/Downloads/clustalo-E20200123-200931-0093-83792760-p2m.fasta")
# print(seq_dic)

print("17" + "\t" + "916")

for item in seq_dic:
    seq_line = seq_dic[item][:50]
    print(item + '\t' + chunkstring(seq_line, 10))


line_size =60
seq_start =50
seq_max_len= 916

while seq_max_len > line_size:
    for item in seq_dic:
        seq_line = seq_dic[item][seq_start:seq_start+line_size]
        print(chunkstring(seq_line, 10))
    seq_start = seq_start + line_size
    print()

    seq_max_len -= line_size

for item in seq_dic:
    seq_line = seq_dic[item][seq_start:seq_start+line_size]
    print(chunkstring(seq_line,10))

# for item in seq_dic:
#     seq_size = len(seq_dic[item])
#     seq_start =0
#     print(item + "\t" + seq_dic[item][seq_start:60])
#     seq_start +=60
#     while (seq_size - seq_start) > line_size:
#         print(seq_dic[item][seq_start+1:seq_start+line_size])
#         seq_start += line_size
#     print(seq_dic[item][seq_start+1:])