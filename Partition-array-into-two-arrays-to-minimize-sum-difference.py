def find_min_difference(nums):
    n = len(nums) // 2

    def find_partitions(index, subset1, subset2):
        # Base case: if we've used all elements
        if index == len(nums):
            if len(subset1) == n and len(subset2) == n:
                sum1, sum2 = sum(subset1), sum(subset2)
                return abs(sum1 - sum2)
            else:
                return float('inf')

        # If either subset is too large, return inf
        if len(subset1) > n or len(subset2) > n:
            return float('inf')

        # Include the current element in subset1 or subset2
        diff1 = find_partitions(index + 1, subset1 + [nums[index]], subset2)
        diff2 = find_partitions(index + 1, subset1, subset2 + [nums[index]])

        # Return the minimum of both options
        return min(diff1, diff2)

    return find_partitions(0, [], [])


nums1 = [3, 9, 7, 3]
nums2 = [-36, 36]
nums3 = [1,2,3,4]

print(find_min_difference(nums1))  # Output: 2
print(find_min_difference(nums2))  # Output: 72
print(find_min_difference(nums3))  # Output: 0
