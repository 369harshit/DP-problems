def min_energy_k_jump(height, k):
    
    N = len(height)                                                              # Get the number of stairs   
    if N == 0:                                                                   # If there are no stairs, no energy is needed
        return 0
       
    dp = [float('inf')] * N                                                      # Initialize the dp array to store the minimum energy required to reach each stair
    dp[0] = 0                                                                    # Starting point, no energy required to be on the first stair

    
    for i in range(1, N):                                                        # Iterate through each stair from 1 to N-1       
        for j in range(1, k + 1):                                                # Check jumps from all possible previous stairs within distance k
            if i - j >= 0:                                                       # Ensure the jump does not go out of bounds
                dp[i] = min(dp[i], dp[i - j] + abs(height[i] - height[i - j]))   # Calculate the minimum energy required to reach stair i

    return dp[N - 1]                                                             # Return the minimum energy required to reach the last stair

height = [10, 30, 40, 50, 20]
k = 3
print(min_energy_k_jump(height, k))  # Output: 30
