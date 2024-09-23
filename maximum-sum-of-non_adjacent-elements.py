def max_sum_non_adjacent(nums):
    
    n = len(nums)                                            # Get the number of elements  
    if n == 0:                                               # If the list is empty, the maximum sum is 0
        return 0 
    if n == 1:                                               # If the list has only one element, the maximum sum is that element
        return nums[0]
    
    
    dp = [0] * n                                             # Initialize the dp array to store the maximum sum up to each index
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
   
    for i in range(2, n):                                     # Iterate through each element from the third element to the end        
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])           # Calculate the maximum sum by either including or excluding the current element
       
    return dp[n - 1]                                          # Return the maximum sum, which is the last element in the dp array


nums = [3, 2, 5, 10, 7]
print(max_sum_non_adjacent(nums))  # Output: 15
