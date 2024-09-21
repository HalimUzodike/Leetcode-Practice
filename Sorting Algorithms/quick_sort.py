# Quick Sort

"""

Time Complexity
Average Case: O(n*log(n))
Worst Case: O(n^2)
Best Case: O(n*log(n))


Space Complexity

Quicksort has a space complexity of O(log(n)) in the average case.
This arises from the recursive function calls and the partitioning process.
It can be O(n) due to an unbalanced partitioning leading to a deep recursion stack in the worst case.


Quick Sort 	O(n log n)* 	In worst case it is O(n^2)
"""


# Implementation of QuickSort
def quickSort(arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side
    quickSort(arr, s, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr
