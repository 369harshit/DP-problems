def uniquePaths(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])

    dp = []                                           # Create a 2D DP array with all elements initialized to 0
    for _ in range(m):
        row = [0] * n
        dp.append(row)
    
                                              
    dp[0][0] = 1                                      # Base case: there's one way to reach the top-left cell
    
   
    for i in range(1, n):                             # Fill the first row (can only move right)
        if grid[0][i] == 0:
            dp[0][i] = dp[0][i-1]
    
   
    for i in range(1, m):                             # Fill the first column (can only move down)
        if grid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
    
   
    for i in range(1, m):                             # Fill the dp array for the rest of the grid
        for j in range(1, n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]                               # The result is stored in the bottom-right corner


grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
print(uniquePaths(grid))  # Output: 2