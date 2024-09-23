def rob(nums):
    
    n = len(nums)                                      # Get the number of houses
    if n == 0:                                         # If there are no houses, the maximum amount of money is 0
        return 0  
    if n == 1:                                         # If there is only one house, the maximum amount of money is the value of that house
        return nums[0]
    
  
    dp = [0] * n                                       # Initialize the dp array to store the maximum amount of money that can be robbed up to each house
    dp[0] = nums[0]                                    # The maximum amount of money robbed from the first house is the value of the first house
    dp[1] = max(nums[0], nums[1])                      # The maximum amount of money robbed from the first two houses is the max of the two values
    
    
    for i in range(2, n):                              # Iterate through each house from the third house to the last house     
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])    # Calculate the maximum amount of money by either including or excluding the current house
    
    return dp[n - 1]                                   # Return the maximum amount of money that can be robbed up to the last house


nums = [1, 2, 3, 1]
print(rob(nums))  # Output: 4
 