def longest_string_chain(words):
    # Sort words by their lengths
    words.sort(key=len)
    
    # Create a dictionary to store the longest chain ending at each word
    longest_chain = {}
    
    # Initialize the longest chain for each word to 1
    for word in words:
        longest_chain[word] = 1
    
    # Iterate through each word
    for word in words:
        # Try removing one character from the word to form a predecessor
        for i in range(len(word)):
            predecessor = word[:i] + word[i+1:]  # Remove one character
            
            # If the predecessor exists in the dictionary, update the chain length
            if predecessor in longest_chain:
                longest_chain[word] = max(longest_chain[word], longest_chain[predecessor] + 1)
    
    # Return the longest chain found
    return max(longest_chain.values())

# Test the function with examples
print(longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]))  # Output: 4
print(longest_string_chain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))  # Output: 5
print(longest_string_chain(["abcd", "dbqca"]))  # Output: 1
