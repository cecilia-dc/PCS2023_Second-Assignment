'''
Rosalind LONG exercise by Di Cicco Cecilia
'''
# 	Genome Assembly as Shortest Superstring

from Bio import SeqIO

from Bio import SeqIO

with open("rosalind_long.txt", "r") as input_file:
    list,l = [],0
    for record in SeqIO.parse(input_file, "fasta"):
        list.append(str(record.seq))
        l += len(str(record.seq))

mid = int(l/len(list)//2)
for a in range(len(list)):
    for sub in list:
        for s in list:
            if sub != s:
                for i in reversed(range(len(sub))):
                    if sub[:i] == s[-i:] and i >= mid-1:
                        list.append(s+sub[i:])
                        if sub in list:
                            list.remove(sub)
                        if s in list:
                            list.remove(s)


shortest_superstrig = max(list,key=len)
print(shortest_superstrig)