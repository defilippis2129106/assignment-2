"""
Maximum Perimeter Triangle 

Given an array of stick lengths, use  of them to construct a non-degenerate triangle with the maximum possible perimeter. 
Return an array of the lengths of its sides as  integers in non-decreasing order.

If there are several valid triangles having the maximum perimeter:

Choose the one with the longest maximum side.
If more than one has that maximum, choose from them the one with the longest minimum side.
If more than one has that maximum as well, print any one them.
If no non-degenerate triangle exists, return [-1]"""


def Max_Perimeter(sticks):
    n = len(sticks)
    max_triangle = []
    max_perimeter = 0

    for x in range(n -2):
        for y in range(x + 1, n -1):
            for z in range (y + 1, n):

                stick1 = sticks[x]
                stick2 = sticks[y]
                stick3 = sticks[z]


                sides = sorted([stick1, stick2, stick3])
                a, b, c = sides  # a <= b <= c
                if a < b + c: # the if statement delineates the criteria to have a non-degenarate triangle
                    if b < a + c:
                        if c < a + b:

                            perimeter = a + b + c 
 
                                # criteria for choosing the best triangle
                            if (perimeter > max_perimeter or
                                (perimeter == max_perimeter and c > max_triangle[2]) or # If there are several valid triangles having the maximum perimeter: 1. Choose the one with the longest maximum side.
                                (perimeter == max_perimeter and c == max_triangle[2] and a > max_triangle[0])):
                                # If more than one has that maximum, choose from them the one with the longest minimum side.
                                # If more than one has that maximum as well, print any one them.

                                max_perimeter = perimeter
                                max_triangle = [a, b, c] # cause they asked for the output in ascending order

    return max_triangle if max_triangle else [-1]



# now we try all our sample inputs

sticks1 = '1 1 1 3 3'
sticks1 = sticks1.split()
sticks1 = [int(num) for num in sticks1]

result1 = Max_Perimeter(sticks1)
print(*result1)

sticks2 = '1 2 3'
sticks2 = sticks2.split()
sticks2 = [int(num) for num in sticks2]
                        
result2 = Max_Perimeter(sticks2)
print(*result2)

sticks3 = '1 1 1 2 3 5'
sticks3 = sticks3.split()
sticks3 = [int(num) for num in sticks3]
                        
result3 = Max_Perimeter(sticks3)
print(*result3)