# Top K Frequent Elements

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""


# Solution works; however, it is not in order. Uses a min heap

# Time - O(n*logk)
# Space - O(n)

from collections import Counter
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First we will init a list(heap) called heap
        # Then we will create a dictionary and store the numbers and their frequencies
        # Create a heap inserting each key,val pair as a tuple in the form (val, key)
        # In this case (val, key) is (frequency, number)
        # If the length of the heap is greater than k, we will pop
        # In the heap the second value is the number we want to return

        heap = []
        counter = Counter(nums)

        for number, frequency in counter.items():
            heappush(heap, (frequency, number))
        
        while len(heap) > k:
            heappop(heap)

        solution = [number[1] for number in heap]

        return solution
    
    
# More intuitive solution. This solution is the same as the one for top k frequent words. It also puts the numbers in order. Uses Max heap

# Time - O(n*logk)
# Space - O(n)

from collections import Counter
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First we will init a list(heap) called heap
        # Then we will create a dictionary and store the numbers and their frequencies
        # Create a heap inserting each key,val pair as a tuple in the form (val, key)
        # In this case (val, key) is (frequency, number)
        # If the length of the heap is greater than k, we will pop
        # In the heap the second value is the number we want to return

        counter = Counter(nums)
        heap = [(-frequency, number) for number, frequency in counter.items()]
        heapify(heap)

        solution = []
        while len(solution) < k:
            if heap:
                solution.append(heappop(heap)[1])
        
        # You can also use the following for the solution
        # solution = [heappop(heap)[1] for _ in range(k)]

        return solution



# Alternate Solution Uses Max heap

# Time - O(n*logk)
# Space - O(n)

from collections import Counter
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First we will init a list(heap) called max heap
        # Then we will create a dictionary and store the numbers and their frequencies
        # Create a heap inserting each key,val pair as a tuple in the form (val, key)
        # In this case (val, key) is (frequency, number)
        # If the length of the heap is greater than k, we will pop
        # In the heap the second value is the number we want to return

        counter = Counter(nums)
        heap = [(-frequency, number) for number, frequency in counter.items()] # Get the max heap ready
        heapify(heap) # Create the heap
        
        solution = []
        for _ in range(k):
            if heap:
                solution.append(heappop(heap)[1])
                
        # You can also use the following for the solution
        # solution = [heappop(heap)[1] for _ in range(k)]
        
        return solution







