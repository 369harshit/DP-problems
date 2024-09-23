def is_palindrome(s):
    return s == s[::-1]                       # Check if the string s is the same when reversed

def min_insertions_to_make_palindrome(s):
    def helper(s, l, r):
        if l >= r:                             # If the left index is greater than or equal to the right index, no insertions needed
            return 0
        if s[l] == s[r]:                       # If the characters at the left and right indices are the same, move inward
            return helper(s, l + 1, r - 1)
        else:
            # If characters are different, find the minimum insertions needed by considering
            # two possibilities: insert at the left or insert at the right
            return 1 + min(helper(s, l + 1, r), helper(s, l, r - 1))

    return helper(s, 0, len(s) - 1)             # Start the helper function with the full string


s1 = "zzazz"
print(min_insertions_to_make_palindrome(s1))  # Output: 0

s2 = "mbadm"
print(min_insertions_to_make_palindrome(s2))  # Output: 2
