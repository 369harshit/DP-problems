def largestDivisibleSubset(nums):
    # Sort the numbers in ascending order
    nums.sort()
    
    # Create a dp array where dp[i] will store the largest subset ending with nums[i]
    dp = []  # Initialize an empty list for dp
    for num in nums:
        dp.append([num])  # Append a list containing just num to dp
    
    # Iterate through the nums array
    for i in range(len(nums)):
        for j in range(i):
            # Check if nums[i] is divisible by nums[j]
            if nums[i] % nums[j] == 0:
                # If the subset with nums[j] can be extended, do it
                if len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
    
    # Return the largest subset found
    return max(dp, key=len)

# Example 1
nums1 = [1, 2, 3]
print(largestDivisibleSubset(nums1))  # Output: [1, 2] or [1, 3]

# Example 2
nums2 = [1, 2, 4, 8]
print(largestDivisibleSubset(nums2))  # Output: [1, 2, 4, 8]
