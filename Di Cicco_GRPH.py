'''
Rosalind GRPH exercise by Di Cicco Cecilia
'''
# Overlap Graphs

# Biopython
from Bio.Seq import Seq
from Bio import SeqIO

from Bio import SeqIO

# File containing data in fasta format
input_file = "rosalind_grph.txt"
k = 3

# Parse the input file using Biopython
records = list(SeqIO.parse(input_file, "fasta"))

def overlap_graph(dna_records, k):
    adjacency_list = []

    for i, record1 in enumerate(dna_records):
        suffix = record1.seq[-k:]
        for j, record2 in enumerate(dna_records):
            if i != j and record2.seq[:k] == suffix:
                adjacency_list.append((record1.id, record2.id))

    return adjacency_list


result = overlap_graph(records, k)

# Print the result
for pair in result:
    print(" ".join(pair))
