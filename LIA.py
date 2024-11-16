"""Given: Two positive integers k(k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
Tom has two children in the 1st generation, each of whom has two children, and so on. 
Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N
Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). 
Assume that Mendel's second law holds for the factors.

Sample Dataset
2 1
Sample Output
0.684
"""

# no matter what organism mates with AaBb the probability that the offspring is AaBb is always 0.25, 1/4
# if we check the punnett square
# now that we know this we need to solving using binary distribution (to obtain the probability of success over n trials)

import math

def Successes(k, n):
    tot  = 2**k # organisms in the kth generation knowing that 2 offspring have two offspring and so on
    prob_AaBb =  0.25
    probability = 0 # I initialize a counter for the cumulative probability

    for i in range (n, tot+1):
        binom_coeff = math.comb(tot, i)
        probability += binom_coeff * (prob_AaBb ** i) * ((1-prob_AaBb) ** (tot - i)) # this is simply the binomial distribution formula
    return round(probability, 3) # I round to 3 decimals to get the exact same result as the output

k = 2
n = 1
result = Successes(k, n)
print(result)