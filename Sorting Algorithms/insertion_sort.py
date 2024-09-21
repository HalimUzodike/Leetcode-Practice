# Insertion Sort

# Time Complexity: O(n^2)
# Space Complexity: O(1)

"""
Concept

Given the array [2,3,4,1,6], our goal is to sort the array so that it looks like [1,2,3,4,6].

Insertion sort accomplishes this by sorting portions of the array at a time.

Consider this: if we had an array of size 11, that would already be sorted because there is no other element to compare it to.

As such, we assume that the first element is sorted because we treat it as its own subarray.

The next subarray will be of size 22 starting from the beginning. In this example that is [2,3,...]. To sort only these two elements we need to compare them.

For an array of size 22, this is trivial.
However, when we get to the full array of size 55, there is no way to keep track of where each element is without using pointers.
So, let's take two pointers, i and j.


Insertion Sort 	O(n^2)* 	If fully, or nearly sorted, O(n)
"""

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr
