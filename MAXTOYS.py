"""
Sample Input

7 50
1 12 5 111 200 1000 10
Sample Output

4
Explanation

He can buy only  toys at most. These toys have the following prices: 1, 12, 5 ,10
"""

items = 7
budget = 50
prices = '1 12 5 111 200 1000 10'

prices = prices.split()
prices = [int(num) for num in prices]

def MaxToys(prices, k):
    max_amount = 0
    spent = 0
    prices = sorted(prices)

    for element in prices:
        if element <= k:
            max_amount += 1
            spent += element
            k = k - element
    return max_amount

result = MaxToys(prices, budget)
    
print(result)