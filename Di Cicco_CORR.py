'''
Rosalind CORR exercise by Di Cicco Cecilia
'''
# Error Correction in Reads

# Biopython
from Bio import SeqIO

# Defining the function Hamming distance
def hamming_distance(sequence1, sequence2):
    return sum([1 if sequence1[i]!=sequence2[i] else 0 for i in range(len(sequence1))])

# Defining the function error correction
def error_corr(reads):
    corrections = []
    correct_reads, incorrect_reads = [], []
    reverse_pattern={"A": "T", "T": "A", "C": "G", "G": "C"}

    for r in reads:
        reverse_r = "".join([reverse_pattern[i] for i in r[::-1]])
        if reads.count(r) + reads.count(reverse_r) >= 2:
            correct_reads.append(r)
        else:
            incorrect_reads.append(r)

    for ir in incorrect_reads:
        for cr in correct_reads:
            reverse_cr = "".join([reverse_pattern[i] for i in cr[::-1]])
            if hamming_distance(ir, cr) == 1:
                corrections.append((ir, cr))
                break
            if hamming_distance(ir, reverse_cr) == 1:
                corrections.append((ir, reverse_cr))
                break

    return corrections

if __name__ == "__main__":
    # Importing data in fasta format with biopython
    sequence_name, sequence_string = [], []
    with open ("rosalind_corr.txt",'r') as input_file:
        for sequence_record in SeqIO.parse(input_file,'fasta'):
            sequence_name.append(str(sequence_record.name))
            sequence_string.append(str(sequence_record.seq))

    corrections = error_corr(sequence_string)
    for ir, cr in corrections:
        corrections_list = "{}->{}".format(ir, cr)
        print(corrections_list)