def count_distinct_subsequences(s, t):
    m, n = len(s), len(t)
    
    # Create a 2D DP array with (m+1) x (n+1) dimensions inside the loop
    dp = []
    for i in range(m + 1):
        dp.append([0] * (n + 1))
    
    # Initialize dp[i][0] to 1 for all i, as an empty t can always be formed by any prefix of s
    for i in range(m + 1):
        dp[i][0] = 1
    
    # Fill the DP array using nested loops
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    # The bottom-right cell contains the count of distinct subsequences
    return dp[m][n]

# Example usage
s = "rabbbit"
t = "rabbit"
print("Number of distinct subsequences:", count_distinct_subsequences(s, t))

