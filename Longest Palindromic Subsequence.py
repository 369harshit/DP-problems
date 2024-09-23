def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_subsequence(s):
    def helper(subseq, index):
        if index == len(s):
            if is_palindrome(subseq):
                return len(subseq)
            else:
                return 0
        # Exclude the current character and move to the next one
        exclude = helper(subseq, index + 1)
        # Include the current character and move to the next one
        include = helper(subseq + s[index], index + 1)
        # Return the maximum length found
        return max(exclude, include)
    
    return helper("", 0)


s1 = "bbbab"
s2 = "cbbd"
print(longest_palindromic_subsequence(s1))  # Output: 4
print(longest_palindromic_subsequence(s2))  # Output: 2
