def maxChocolates(matrix):
    n = len(matrix)        # Number of rows in the matrix
    m = len(matrix[0])     # Number of columns in the matrix
    
    # Backtracking function to calculate the maximum chocolates Alice and Bob can collect
    def collectChocolates(row, colA, colB):
        # Base case: If Alice or Bob moves out of bounds, return 0 chocolates
        if colA < 0 or colA >= m or colB < 0 or colB >= m:
            return 0
        
        # If Alice and Bob are at the same position, collect chocolates from that cell only once
        if colA == colB:
            chocolates = matrix[row][colA]
        else:
            # Otherwise, collect chocolates from both Alice's and Bob's positions
            chocolates = matrix[row][colA] + matrix[row][colB]
        
        # If they have reached the last row, return the chocolates collected so far
        if row == n - 1:
            return chocolates
        
        # Variable to keep track of the maximum chocolates they can collect in future moves
        maxChocolatesCollected = 0

        # Alice can move to the next row in 3 possible directions: down-left, down, or down-right
        for newColA in [colA - 1, colA, colA + 1]:
            # Bob can move to the next row in 3 possible directions: down-left, down, or down-right
            for newColB in [colB - 1, colB, colB + 1]:
                # Recursively collect chocolates for all possible combinations of moves for Alice and Bob
                maxChocolatesCollected = max(maxChocolatesCollected,collectChocolates(row + 1, newColA, newColB))  # Recursive call to explore further rows
        
        # Return the total chocolates collected from the current cell(s) plus the maximum chocolates from future moves
        return chocolates + maxChocolatesCollected
    
    # Start the collection from the top row: Alice at (0, 0) and Bob at (0, m-1)
    return collectChocolates(0, 0, m - 1)


matrix = [
    [2, 3, 1, 2],  # Row 1: Alice and Bob start from opposite corners
    [3, 4, 2, 2],  # Row 2: Possible moves down-left, down, or down-right
    [5, 6, 3, 5]   # Row 3: Last row where they collect final chocolates
]

print(maxChocolates(matrix))  # Output: 21
