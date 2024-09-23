def min_energy(height):
   
    N = len(height)                                                # Get the number of stairs  
    if N == 0:                                                      # If there are no stairs, no energy is needed
        return 0   
    if N == 1:                                                      # If there's only one stair, no energy is needed to stay on it
        return 0


    dp = [0] * N                                                     # Initialize the dp array to store the minimum energy required to reach each stair 
    dp[0] = 0                                                        # Starting point, no energy required to be on the first stair

    
    for i in range(1, N):                                            # Iterate through each stair from 1 to N-1     
        if i == 1:                                                   # If at the first stair, the only possible jump is from stair 0 to stair 1
            dp[i] = abs(height[i] - height[i - 1])
        else:            
            jump_one = dp[i - 1] + abs(height[i] - height[i - 1])    # Calculate the energy required to jump from the previous stair (i-1)            
            jump_two = dp[i - 2] + abs(height[i] - height[i - 2])    # Calculate the energy required to jump from the stair before the previous (i-2)           
            dp[i] = min(jump_one, jump_two)                          # Choose the minimum energy required to reach the current stair
  
    return dp[N - 1]                                                 # Return the minimum energy required to reach the last stair


height = [10, 20, 30, 10]
print(min_energy(height))  # Output: 20
