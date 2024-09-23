def isMatch(s, p):
    def matchHelper(s, p, s_index, p_index):                                         # Helper function for recursion
        
        if s_index >= len(s) and p_index >= len(p):                                  # Base case: if we've reached the end of both the string and the pattern, it's a match
            return True
        
        if p_index >= len(p):                                                        # If we've reached the end of the pattern but not the string, it's not a match
            return False
        
        if p[p_index] == '*':                                                        # If the current pattern character is '*', it can match zero or more characters
            return matchHelper(s, p, s_index, p_index + 1) or (s_index < len(s) and matchHelper(s, p, s_index + 1, p_index))
        
        if s_index < len(s) and (p[p_index] == '?' or p[p_index] == s[s_index]):     # If the current pattern character is '?' or it matches the current string character                             
            return matchHelper(s, p, s_index + 1, p_index + 1)
        
        return False                                                                 # If none of the above conditions are met, it's not a match
    
    return matchHelper(s, p, 0, 0)

# Test cases
print(isMatch("aa", "a"))    
print(isMatch("aa", "*"))   
print(isMatch("cb", "?a"))   
print(isMatch("adceb", "*a*b"))
print(isMatch("acdcb", "a*c?b")) 
