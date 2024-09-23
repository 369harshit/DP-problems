def scs(str1, str2):
    def scs_helper(i, j):                                 # Helper function to calculate the SCS
        if i == len(str1):                                # If we reach the end of str1, return the remaining part of str2
            return str2[j:]
        if j == len(str2):                                # If we reach the end of str2, return the remaining part of str1
            return str1[i:]
        
        if str1[i] == str2[j]:                            # If characters in str1 and str2 at current positions match
            return str1[i] + scs_helper(i + 1, j + 1)     # Include this character and move both pointers forward
        
        else:                                             # If characters do not match
            option1 = str1[i] + scs_helper(i + 1, j)      # Option 1: Include character from str1 and move its pointer forward
            option2 = str2[j] + scs_helper(i, j + 1)      # Option 2: Include character from str2 and move its pointer forward
            
            if len(option1) < len(option2):               # Compare lengths of option1 and option2 and return the shorter one
                return option1
            else:
                return option2

    return scs_helper(0, 0)                               # Start the helper function with both pointers at the beginning


str1 = "abac"
str2 = "cab"
print(scs(str1, str2))  # Output: "cabac"
