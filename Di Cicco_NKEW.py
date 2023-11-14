'''
Rosalind NKEW exercise by Di Cicco Cecilia
'''
# Newick Format with Edge Weights


# Biopython package working with Phylogenetic trees
import sys
from Bio import Phylo
import io

input_file = 'rosalind_nkew.txt'
output_file = 'result_NKEW.txt'

with open(input_file, 'r') as file:
    pairs = [i.split('\n') for i in file.read().strip().split('\n\n')]

with open(output_file, 'w') as output:
    for i, line in pairs:
        X, Y = line.split()
        tree = Phylo.read(io.StringIO(i), 'newick')
        distance = round(tree.distance(X, Y))
        output.write(f'{distance} ')

print(output_file)