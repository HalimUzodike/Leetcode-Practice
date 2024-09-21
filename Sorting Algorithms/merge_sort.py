# Merge Sort

# Time complexity: O(nlogn)
# Space complexity: O(n)

"""
The concept behind it is very simple. Keep splitting the array into halves until the subarrays hit a size of one.
Then recursively sort the subarrays by merging two subarrays at a time. The final array will be fully sorted.

This is a technique that is known as divide and conquer.
We divide the problem into smaller subproblems, solve them and then combine the solutions to get the final answer.

Merge Sort 	O(n log n)

"""

# Implementation of MergeSort
def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    # The middle index of the array
    m = (s + e) // 2

    # Sort the left half
    mergeSort(arr, s, m)

    # Sort the right half
    mergeSort(arr, m + 1, e)

    # Merge sorted halfs
    merge(arr, s, m, e)

    return arr
