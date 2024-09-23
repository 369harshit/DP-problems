def minimumTotal(triangle):
    if not triangle:
        return 0
  
    dp = triangle[-1]                                                 # Copy the last row of the triangle as the initial state of our DP array
 
    for row in range(len(triangle) - 2, -1, -1):                      # Start from the second to last row and move upwards
        for col in range(len(triangle[row])):           
            dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])  # Update the DP array with the minimum path sum to reach each element

    return dp[0]                                                      # The top element now contains the minimum path sum


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

print(minimumTotal(triangle))  # Output: 11
