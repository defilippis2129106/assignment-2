"""A permutation of length n is an ordering of the positive integers {1,2,…,n}.
For example, π=(5,3,2,1,4) is a permutation of length 5
Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample Dataset
3
Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""


def Perm(values):

    if len(values) == 0: # I need to initialize a base case where the list of elements is empty
        return []

    if len(values) == 1:
        return [values] # and the case in which only one element is present so only one permutation is possible

    permutations = [] # this list will contain the following possible permutations

    for i in range(len(values)):
        element = values[i]

        other_elements = values[:i] + values[i+1:] # we create a list of all the other elements except the one at that specific index

        for j in Perm(other_elements): # with this we recursively generate all permutations of the remaining elements
            permutations.append([element] + j) # then we append the current element to each of the permutations of the remaining elements

    return permutations


n = 3
values = list(range(1, n+1))

permutations = Perm(values)

print(len(permutations)) # total n of permutations

for element in permutations:
    print(*element)  # prints each permutation in the list
