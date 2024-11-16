"""A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""

def parser(fasta_data):
    sequence_list = []
    
    for line in fasta_data.strip().splitlines():
        line = line.strip()
        if line.startswith('>'): 
            continue
        else:
            sequence_list.append(line)  

    return ''.join(sequence_list)

def RevCompl(dna):
    complements = {"A": "T", "C": "G", "G": "C", "T": "A"}

    return ''.join(complements[base] for base in dna[::-1]) # now I simply reverse the string and then get its complement

def RevPal(dna):
    result = []
    for length in range(4, 13):  # the lengths of the reverse palindromes we are asked to find go from 4 to 12
        for i in range(len(dna) - length + 1):  # now we iterate over all possible start positions
            substr = dna[i:i + length]
            if substr == RevCompl(substr):

                result.append((i + 1, length)) # we want to report the correct position in the sequence, but in dna sequence they start from 1, so we write i+1
    for position, length in result:
        print(position, length)


sample_input = """
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
"""

dna_sequence = parser(sample_input)
RevPal(dna_sequence)
