def maxPathSum(matrix):
    if not matrix or not matrix[0]:
        return 0

    N = len(matrix)
    M = len(matrix[0])

    dp = []                                                                     # Create a DP array initialized with the values of the first row
    for row in matrix:
        dp.append(row[:])


    for row in range(1, N):                                                     # Fill the DP array
        for col in range(M):
            max_from_above = dp[row - 1][col]                                   # Check the value from the cell directly above

            if col > 0:                                                         # Check the value from the top-left cell, if it exists
                max_from_above = max(max_from_above, dp[row - 1][col - 1])

            if col < M - 1:                                                     # Check the value from the top-right cell, if it exists
                max_from_above = max(max_from_above, dp[row - 1][col + 1])

            dp[row][col] += max_from_above                                      # Update the current cell in dp with the max value from above plus the current cell's value

    return max(dp[N - 1])                                                       # The maximum path sum will be the maximum value in the last row of the DP array


matrix = [
    [2, 2, 1],
    [3, 4, 5],
    [6, 5, 7],
    [4, 1, 8]
]
    
print(maxPathSum(matrix))  # Output: 22