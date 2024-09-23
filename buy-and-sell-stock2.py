def maxProfit(prices):
    total_profit = 0
    
    # Loop through prices, and check for profit on each consecutive day
    for i in range(1, len(prices)):
        # If today's price is greater than yesterday's, buy and sell for profit
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]
    
    return total_profit

# Test cases
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 7
print(maxProfit([1, 2, 3, 4, 5]))     # Output: 4
print(maxProfit([7, 6, 4, 3, 1]))     # Output: 0
