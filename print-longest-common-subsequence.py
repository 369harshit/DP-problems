def longestCommonSubsequence(str1, str2):
    def lcs(i, j):                                   # Define a helper function for recursion
        if i == len(str1) or j == len(str2):         # If we've reached the end of either string, return 0 length and empty subsequence
            return 0, ""
 
        if str1[i] == str2[j]:                       # If the characters at the current positions are the same
            length, subseq = lcs(i + 1, j + 1)       # Recur for the next characters in both strings
            return 1 + length, str1[i] + subseq      # Return 1 plus the result, and add the current character to the subsequence

    
        length1, subseq1 = lcs(i + 1, j)             # If the characters are not the same, find the LCS by skipping one character from either string
        length2, subseq2 = lcs(i, j + 1)

       
        if length1 > length2:                        # Return the longer subsequence
            return length1, subseq1
        else:
            return length2, subseq2

    length, subseq = lcs(0, 0)                        # Start the recursion from the beginning of both strings
    return length, subseq


str1 = "abcde"
str2 = "bdgek"
length, subseq = longestCommonSubsequence(str1, str2)

print(f"Length of LCS: {length}")  
print(f"LCS: {subseq}")            # Output should be "bde"
