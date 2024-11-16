"""
Given: A DNA string s
 (of length at most 1 kbp) and a collection of substrings of s
 acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s
. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
Sample Output
MVYIADKQHVASREAYGHMFKVCA
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

def Exons(sample_input):
    sequences = parser(sample_input)
    
    seq1 = sequences[0] # we store the first sequence, from which we'll have to remove the introns
    
    # now we remove each subsequence in sequences[1:] from the first sequence
    for subseq in sequences[1:]: 
        seq1 = seq1.replace(subseq, '') # this way we remove the introns
  
    return seq1 # and our sequence has only exons

def Transcription(dna):
    return dna.replace("T", "U") # in mrna all the Ts are replacd by Us

def Translation(rna):
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)] # we need to split the mrna into codons 
    
    # the last step is to translate each codon but stop at '*'
    proteins = []
    for codon in codons:
        amino_acid = codon_table.get(codon, '*')
        if amino_acid == '*':
            break
        proteins.append(amino_acid)
    
    return ''.join(proteins) # we turn our protein list into a string

sample_input = """
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
"""

exons_seq = Exons(sample_input)
mrna = Transcription(exons_seq)
protein = Translation(mrna)
print(protein)