def knapsack(profit, weight, capacity):
    n = len(profit)
    
    # Function to explore all possible combinations
    def find_max_profit(current_weight, current_profit, max_profit):
        # If the current weight is more than the capacity, stop
        if current_weight > capacity:
            return max_profit
        
        # Update the maximum profit if current profit is higher
        max_profit = max(max_profit, current_profit)
        
        # Try adding each item to the knapsack
        for i in range(n):
            new_weight = current_weight + weight[i]
            new_profit = current_profit + profit[i]
            max_profit = find_max_profit(new_weight, new_profit, max_profit)
        
        return max_profit
    
    # Start checking from zero weight and zero profit
    return find_max_profit(0, 0, 0)

n = 3
capacity = 10
profit = [5, 11, 13]
weight = [2, 4, 6]

max_profit = knapsack(profit, weight, capacity)
print("Maximum Profit:", max_profit)
