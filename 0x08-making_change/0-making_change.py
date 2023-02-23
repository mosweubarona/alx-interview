#!/usr/bin/python3
"""Give fewest number of coins to meet given total amont"""

def makeChange(coins, total):
    if total < 1:
        return 0
    
    # Initialize a list to keep track of the minimum number of coins needed for each amount up to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    
    # Iterate through each coin in coins
    for coin in coins:
        # Iterate through each amount from coin value up to total
        for amt in range(coin, total + 1):
            # Calculate the minimum number of coins needed for the current amount
            min_coins_needed = min_coins[amt - coin] + 1
            # Update min_coins if the current coin leads to a smaller number of coins needed
            if min_coins_needed < min_coins[amt]:
                min_coins[amt] = min_coins_needed
    
    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]

