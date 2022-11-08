from Bio import SeqIO
sequences = []
for seq_record in SeqIO.parse('Data\sequence.fasta', 'fasta'):
    sequences.append(seq_record.seq)

from Functions import bases
pos= {}
i = 0
for seq in sequences:
    for n in  ['R', 'S', 'K', 'N', 'M', 'Y', 'W', 'V']:
        # print(seq)
        if pos.get(i):
            pos[i] = str(seq).count(n) + pos.get(i)
        else:
            pos[i] = str(seq).count(n)
    i += 1
rel = {}
for x, y in zip(pos.keys(), pos.values()):
    if y != 0 :
        rel[x] = y

print(sequences[12908])
print(len(rel))

from matplotlib import pyplot as plt
plt.hist(rel.values(), bins=20)
plt.show()
a = [x for x in rel.values()]
a.sort()
print(a)
print(pos)
