def count_partitions_with_diff(arr, D):
    n = len(arr)
    count = [0]  # Use a list to allow modification inside the helper function

    # Helper function to recursively generate partitions
    def partition(index, S1, S2, count):
        # Base case: if all elements have been considered
        if index == n:
            if S1 - S2 == D and S1 >= S2:
                count[0] += 1
            return

        # Include arr[index] in the first subset (S1)
        partition(index + 1, S1 + arr[index], S2, count)

        # Include arr[index] in the second subset (S2)
        partition(index + 1, S1, S2 + arr[index], count)

    # Start the recursive partitioning from the first element
    partition(0, 0, 0, count)

    return count[0]  # Return the count value from the list

# Example usage
arr = [5,2,6,4]
D = 3
result = count_partitions_with_diff(arr, D)
print("Number of partitions with given difference:", result)
