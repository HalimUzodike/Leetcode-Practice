# In Python, we will use the heapq module
# Note: heapq only implements min heaps
from heapq import *

# Declaration: heapq does not give you a heap data structure.
# You just use a normal list, and heapq provides you with
# methods that can be used on this list to perform heap operations
heap = []

# Add to heap
heappush(heap, 1)
heappush(heap, 2)
heappush(heap, 3)

# Check minimum element
heap[0] # 1

# Pop minimum element
heappop(heap) # 1

# Get size
len(heap) # 2

# Bonus: convert a list to a heap in linear time
nums = [43, 2, 13, 634, 120]
max_heap = [-num for num in nums] # We need to multiply every number by -1 to use the max heap.
heapify(max_heap)   # You can simply use heapify(nums) to use the regualr python min heap

# Now, you can use heappush and heappop on nums
# and nums[0] will always be the minimum element
print(-max_heap[0]) # Printing -max_heap[0] should give the correct max heap value


print("Initial max heap:", [-num for num in max_heap])

# while max_heap:
#     for num in max_heap:
#         print(heappop(max_heap))

"""
Notes:

If a node is at index i
Then its children are at index 2i+1 and 2i+2
The parent node is located at i//2  
"""