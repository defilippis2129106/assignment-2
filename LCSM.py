"""Given: A collection of k
 (k≤100
) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
Sample Output
AC
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


def LCSM(sequences):
    seq1 = sequences[0]  # we take the first sequence as a reference
    max_substr = "" 
    
    # now we take all the substrings in the first sequence with a for loop
    for length in range(1, len(seq1) + 1): # this is to get substrings of all possible lengths
        for i in range(len(seq1) - length + 1):
            # we put as a variable the substring that starts from i, which is the starting point we defined in the for loop
            substr = seq1[i:i+length]
            
            # now we need to check if this substring is present in all other sequences
            common = all(substr in seq for seq in sequences)
            
            # lastly, if the substring is common and longer than the current one, we need to update the result
            if common and len(substr) > len(max_substr):
                max_substr = substr
    
    return max_substr
    
sample_input = """
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

sequences = parser(sample_input)

result = LCSM(sequences)
print(result)