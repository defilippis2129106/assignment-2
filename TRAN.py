"""For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2)
is the ratio of the total number of transitions to the total number of transversions,
where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance.

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2)

"""


def parser(fasta_data):
    sequences = []
    sequence_list = []

    for line in fasta_data.strip().splitlines():
        line = line.strip()
        if line.startswith('>'):  
            if sequence_list:  
                sequences.append(''.join(sequence_list))
            sequence_list = [] 
        else:
            sequence_list.append(line) 

    if sequence_list:
        sequences.append(''.join(sequence_list))

    return sequences  


sample_input = """>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
"""
sequences = parser(sample_input)
# I stored the first and second sequences to compare them later
dna1 = sequences[0]
dna2 = sequences[1]


def Tran(dna1, dna2):
    transition = 0
    transversion = 0
    purines = ['A', 'G']
    pyrimidines = ['C', 'T']

    for element1, element2 in zip(dna1, dna2):
        if element1 != element2:
            if element1 in purines and element2 in purines:
                transition += 1
            if element1 in pyrimidines and element2 in pyrimidines:
                transition += 1
            if element1 in purines and element2 in pyrimidines:
                transversion += 1
            if element1 in pyrimidines and element2 in purines:
                transversion += 1
    return ('%0.11f' % (transition / transversion))

result = Tran(dna1, dna2)
print(result)
