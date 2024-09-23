def count_subsets_with_sum(arr, n, K):
    # Base Cases
    if K == 0:
        return 1
    if n == 0:
        return 0

    # If the last element is greater than the sum, ignore it
    if arr[n - 1] > K:
        return count_subsets_with_sum(arr, n - 1, K)

    # Number of subsets including the last element + excluding the last element
    return count_subsets_with_sum(arr, n - 1, K - arr[n - 1]) + count_subsets_with_sum(arr, n - 1, K)


arr = [1, 2, 2, 3]
K = 3
n = len(arr)

print("Number of subsets with sum", K, ":", count_subsets_with_sum(arr, n, K))
