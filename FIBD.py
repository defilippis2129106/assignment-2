"""
Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100
 and m≤20
.

Return: The total number of pairs of rabbits that will remain after the n
-th month if all rabbits live for m
 months.

Sample Dataset
6 3
Sample Output
4
"""


def FibdRabbits(months, death):
    rab = [0] * death # this is a list with rabbits in age groups, those that are newborn, those that are 1 month old, and those that are 2 month old
    rab[0] = 1  # first month, base case there's only the first pair of rabbits that reaches reproduction age
    tot_rab = [] # I created this list to keep track of the n of rabbits each month
    tot_rab.append(sum(rab))

    for i in range(1, months): # range(1, months) cause we know that in the first month there's only 1 pair
        born = sum(rab[1:])  # only those that are of reproduction age
        rab = [born] + rab[:-1] # I used the indexing [:-1] because I want to keep the rabbits 
        # except the last ones that have reached 3 months and so have died
        # we're basically shifting along the list 'rab'
        tot_rab.append(sum(rab))

    return tot_rab[-1] # here I used the -1 index to get only the last element of the list, which is the rabbits at the last month
     
    
months = 6
death = 3

result = FibdRabbits(months, death)

print(result)


