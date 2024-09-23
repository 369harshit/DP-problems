def lcs(X, Y):
    m = len(X)
    k = len(Y)
    
    # Creating a 2D array to store lengths of LCS
    dp = []
    for i in range(m + 1):
        dp.append([0] * (k + 1))
    
    # Loop through each character in X (0 to m) and Y (0 to k)
    for i in range(m + 1):
        for j in range(k + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][k]

def min_insert_delete(X, Y):
    lcs_length = lcs(X, Y)
    
    deletions = len(X) - lcs_length
    insertions = len(Y) - lcs_length
    
    return deletions, insertions

# Example usage
X = "heap"
Y = "pea"
deletions, insertions = min_insert_delete(X, Y)
print(f"Minimum deletions: {deletions}")
print(f"Minimum insertions: {insertions}")
