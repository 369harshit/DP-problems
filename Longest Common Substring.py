def longestCommonSubstring(str1, str2):
    max_length = 0
    max_substring = ""

    # Loop through each character in str1
    for i in range(len(str1)):
        # Loop through each character in str2
        for j in range(len(str2)):
            # Initialize the length of the common substring
            length = 0
            # Initialize the common substring itself
            substring = ""
            # Check characters while they match and within the bounds of both strings
            while i + length < len(str1) and j + length < len(str2) and str1[i + length] == str2[j + length]:
                substring += str1[i + length]
                length += 1
            # If we found a longer common substring, update max_length and max_substring
            if length > max_length:
                max_length = length
                max_substring = substring

    return max_length, max_substring


str1 = "abcjklp"
str2 = "acjkp"
length, substring = longestCommonSubstring(str1, str2)
print(f"Length of Longest Common Substring: {length}")  
print(f"Longest Common Substring: {substring}")         
