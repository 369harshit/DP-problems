def min_path_sum(triangle):
    # Base case: if the triangle is empty, return 0
    if not triangle:
        return 0
    
    # Dynamic programming table to store minimum path sums
    dp = []
    for row in triangle:
        dp.append([0] * len(row))

    # Initialize the bottom row of the DP table with the values of the bottom row of the triangle
    dp[-1] = triangle[-1]
    
    # Traverse the triangle from bottom to top, computing the minimum path sum at each cell
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Compute the minimum path sum for each cell based on the adjacent cells below
            dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])

    # The top cell of the DP table contains the minimum path sum
    return dp[0][0]

# Example usage:
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(min_path_sum(triangle))  # Output: 11
