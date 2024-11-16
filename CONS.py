"""Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

def parser(fasta_data):
    sequences = []
    sequence = []
    
    for line in fasta_data.strip().splitlines():
        line = line.strip()
        if line.startswith('>'):
            if sequence:
                sequences.append(''.join(sequence))
                sequence = []
        else:
            sequence.append(line) 

    if sequence:
        sequences.append(''.join(sequence))
    
    return sequences

def ProfMatrix(sequences):
    # first I need to initialize a profile matrix with zeros for each nucleotide and each position
    # basically a profile matrix is a dictionary with keys 'A', 'C', 'G', 'T' (nucleotides)
    n = len(sequences[0])
    profile = {element: [0] * n for element in "ACGT"} # I initialize each list with 0 cause no nucleotides have been counted yet
    
    # now we count each nucleotide at each position
    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1
    
    return profile

def consensus(profile):
    consensus = []
    length = len(profile['A'])  # here we get the length of one of the sequences, whatever sequence is fine
    
    for i in range(length):
        # now we get the nucleotide with the maximum count at position i
        counts = {nuc: profile[nuc][i] for nuc in "ACGT"} # I created a dictionary (counts) where each nucleotide ('A', 'C', 'G', 'T') 
                                                          # maps to the count of that nucleotide at position i in the profile matrix

        max_nucleotide = max(counts, key=counts.get)  # max() finds the nucleotide that has the highest count at position i
        consensus.append(max_nucleotide) # and we add it to the consensus sequence
    
    return ''.join(consensus) # the last step is to turn the list into a string


sample_input = """
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

sequences = parser(sample_input)

profile = ProfMatrix(sequences)
cons_string = consensus(profile)


# this is our output, the consensus sequence and below the profile matrix
print(cons_string)
for element in "ACGT":
    print(f"{element}: {' '.join(map(str, profile[element]))}")