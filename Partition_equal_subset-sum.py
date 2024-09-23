def can_partition(nums):
    total_sum = sum(nums)
    
    # If total sum is odd, it cannot be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False

    # We need to find a subset with sum equal to half of total sum
    target = total_sum // 2

    def subset_sum(arr, n, sum):
        # Base Cases
        if sum == 0:
            return True
        if n == 0:
            return False

        # If last element is greater than sum, then ignore it
        if arr[n-1] > sum:
            return subset_sum(arr, n-1, sum)

        # Check if sum can be obtained by including or excluding the last element
        return subset_sum(arr, n-1, sum) or subset_sum(arr, n-1, sum - arr[n-1])

    return subset_sum(nums, len(nums), target)

# Example usage
nums1 = [1, 5, 11, 5]
nums2 = [1, 2, 3, 5]

print(can_partition(nums1))  # Output: True
print(can_partition(nums2))  # Output: False
