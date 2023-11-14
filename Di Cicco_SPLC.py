'''
Rosalind SPLC exercise by Di Cicco Cecilia
'''
# RNA splicing

# Biopython
from Bio import SeqIO 
from Bio.Seq import Seq

# Reading the FASTA file and extracting the sequences
sequences = []
with open('rosalind_splc.txt', 'r') as DNA_string:
    for record in SeqIO.parse(DNA_string, 'fasta'):
        sequences.append(str(record.seq))

# Removing introns from the s string of DNA
DNA_string = sequences[0]
for intron in sequences[1:]:
    DNA_string = DNA_string.replace(intron, '')

# Translating the string obtained after the removal of introns into a protein string
protein_string = Seq(DNA_string)
protein_string = protein_string.translate()
print(protein_string)