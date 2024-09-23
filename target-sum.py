def count_ways(ARR, N, target):
    # Helper function to recursively explore each combination
    def find_ways(index, current_sum):
        # If we have placed a sign for all numbers
        if index == N:
            # Check if the current sum equals the target
            return 1 if current_sum == target else 0
        
        # Option 1: Add the current number
        add_way = find_ways(index + 1, current_sum + ARR[index])
        
        # Option 2: Subtract the current number
        subtract_way = find_ways(index + 1, current_sum - ARR[index])
        
        # Return total ways for this index
        return add_way + subtract_way
    
    # Start the recursion from index 0 with an initial sum of 0
    return find_ways(0, 0)

# Example usage
ARR = [1, 2, 3, 1]
target = 3
N = len(ARR)

number_of_ways = count_ways(ARR, N, target)
print("Number of ways to reach the target:", number_of_ways)
