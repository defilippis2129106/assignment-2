"""Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
MA
Sample Output
12
"""

codon_table = {
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    
    'UAU': 'Y', 'UAC': 'Y',
    'CAU': 'H', 'CAC': 'H',
    'AAU': 'N', 'AAC': 'N',
    'GAU': 'D', 'GAC': 'D',
    
    'UAA': '', 'UAG': '', 'UGA': '',
    'CAA': 'Q', 'CAG': 'Q',
    'AAA': 'K', 'AAG': 'K',
    'GAA': 'E', 'GAG': 'E',
    
    'UGU': 'C', 'UGC': 'C',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    
    'UGG': 'W', 'AGA': 'R', 'AGG': 'R'
}

# I used this dictionary for the exercise PROT in which I had to translate a mrna sequence to protein
# so in this exercise I reverse it and then I define a function to count the occurrences 
# of a specific amino acid in the dictionary

reverse_codons = {}
for codon, amino in codon_table.items():
    if amino:  # I want to skip the stop codons
        if amino not in reverse_codons:
            reverse_codons[amino] = []
        reverse_codons[amino].append(codon) # I grouped the codons by amino acids


def MRNA(protein):
    sequences = 3 # I put 3 cause I want to multiply by the 3 possible stop codons, so I obtain the correct amount of possible seuqences
    for amino in protein:
        # I want to get the possible codons for this amino acid
        if amino in reverse_codons:
            codons = len(reverse_codons[amino])
            sequences *= codons

    return sequences % 1000000 # this is to give the modulo rosalind asked for

protein = 'MA'
result = MRNA(protein)
print(result)
