# Bucket Sort

"""
Time complexity: O(n)
Space complexity: O(n)


Bucket Sort 	O(n)* 	Assuming all values in the input are in a specified range.
"""

def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr
