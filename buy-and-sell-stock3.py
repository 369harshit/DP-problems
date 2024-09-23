def maxProfit(prices):
    max_profit = 0
    n = len(prices)
    
    first_transaction_profit = 0
    for i in range(n):
        for j in range(i):
            first_transaction_profit = max(first_transaction_profit, prices[i] - prices[j])
        
        
        second_transaction_profit = 0
        for k in range(i + 1, n):
            for l in range(i + 1, k):
                second_transaction_profit = max(second_transaction_profit, prices[k] - prices[l])
        
        max_profit = max(max_profit, first_transaction_profit + second_transaction_profit)
    
    return max_profit

# Test cases
print(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))  # Output: 6
print(maxProfit([1, 2, 3, 4, 5]))           # Output: 4
print(maxProfit([7, 6, 4, 3, 1]))           # Output: 0
