def longestBitonicSubsequence(arr):
    n = len(arr)
    
    # Step 1: Calculate LIS for each element
    dp1 = [1] * n  # Initialize dp1 with 1
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp1[i] = max(dp1[i], dp1[j] + 1)
    
    # Step 2: Calculate LDS for each element
    dp2 = [1] * n  # Initialize dp2 with 1
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
    
    # Step 3: Find the maximum value of ans[i]
    max_bitonic = 0
    for i in range(n):
        ans_i = dp1[i] + dp2[i] - 1
        max_bitonic = max(max_bitonic, ans_i)
    
    return max_bitonic

arr = [1, 11, 2, 10, 4, 5, 2, 1]
result = longestBitonicSubsequence(arr)
print(result)
