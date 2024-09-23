def min_coins(X, coins):
    # Create a list to store the minimum coins needed for each amount up to X
    dp = [float('inf')] * (X + 1)
    dp[0] = 0  # No coins are needed to make a sum of 0

    # Loop through all sums from 1 to X
    for i in range(1, X + 1):
        for coin in coins:
            if i - coin >= 0:  # Check if it's possible to use the coin
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[X] is still infinity, it means we cannot reach the sum X
    return dp[X] if dp[X] != float('inf') else -1

# Example usage:
X = 7
coins = [1,3,4]
print("Minimum coins required:", min_coins(X, coins))
