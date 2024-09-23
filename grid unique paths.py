def unique_paths(m, n):
  
    dp = []                                    # Create a 2D DP array with all elements initialized to 0
    for _ in range(m):
        row = [0] * n
        dp.append(row)
          
       
    for i in range(m):                          # Initialize the first row to 1, because there's only one way to reach each cell in the first row
        dp[i][0] = 1

    for j in range(n):                          # Initialize the first column to 1, because there's only one way to reach each cell in the first column
        dp[0][j] = 1
    
    
    for i in range(1, m):                       # Fill the rest of the DP array
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  # The number of ways to reach dp[i][j] is the sum of the ways to reach dp[i-1][j] and dp[i][j-1]
    
    return dp[m-1][n-1]                         # The bottom-right corner contains the number of unique paths


m = 3
n = 2
print(unique_paths(m, n))  # Output: 3
