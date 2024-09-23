def ninja_training(points):
    
    n = len(points)                                         # Number of days
    
    dp = []                                                 # Initialize an empty list to store the DP table
    for i in range(n):                                      # Loop through each day
        dp.append([0, 0, 0])                                # Append a list with three zeros for the three activities
    
    dp[0][0] = points[0][0]                                 # Initialize the first day with the same points as given
    dp[0][1] = points[0][1]
    dp[0][2] = points[0][2]
    
   
    for i in range(1, n):                                      # Fill the dp table
        dp[i][0] = points[i][0] + max(dp[i-1][1], dp[i-1][2])  # Activity 0 today, choose max from previous day excluding activity 0
        dp[i][1] = points[i][1] + max(dp[i-1][0], dp[i-1][2])  # Activity 1 today, choose max from previous day excluding activity 1
        dp[i][2] = points[i][2] + max(dp[i-1][0], dp[i-1][1])  # Activity 2 today, choose max from previous day excluding activity 2
    
    return max(dp[n-1][0], dp[n-1][1], dp[n-1][2])             # Return the maximum points from the last day for any activity


points = [
    [1, 2, 5],  # Day 1 points for activities 0, 1, 2
    [3, 1, 1],  # Day 2 points for activities 0, 1, 2
    [3, 3, 3]   # Day 3 points for activities 0, 1, 2
]
print(ninja_training(points))  # Output: 11
