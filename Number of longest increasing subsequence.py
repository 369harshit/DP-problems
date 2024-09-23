def findNumberOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    lengths = [1] * n  # lengths[i] will be the length of the LIS ending at index i
    counts = [1] * n   # counts[i] will be the number of LIS ending at index i

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]

    max_length = max(lengths)
    total_count = 0

    for i in range(n):
        if lengths[i] == max_length:
            total_count += counts[i]

    return total_count


print(findNumberOfLIS([1, 3, 5, 4, 7]))  # Output: 2
print(findNumberOfLIS([2, 2, 2, 2, 2]))  # Output: 5