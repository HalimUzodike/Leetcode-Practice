# Minimum Operations to Halve Array Sum

"""
You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number.
(Note that you may choose this reduced number in future operations.)

Return the minimum number of operations to reduce the sum of nums by at least half.
"""

"""
Example 1:

Input: nums = [5,19,8,1]
Output: 3
Explanation: The initial sum of nums is equal to 5 + 19 + 8 + 1 = 33.
The following is one of the ways to reduce the sum by at least half:
Pick the number 19 and reduce it to 9.5.
Pick the number 9.5 and reduce it to 4.75.
Pick the number 8 and reduce it to 4.
The final array is [5, 4.75, 4, 1] with a total sum of 5 + 4.75 + 4 + 1 = 14.75. 
The sum of nums has been reduced by 33 - 14.75 = 18.25, which is at least half of the initial sum, 18.25 >= 33/2 = 16.5.
Overall, 3 operations were used so we return 3.
It can be shown that we cannot reduce the sum by at least half in less than 3 operations.


Example 2:

Input: nums = [3,8,20]
Output: 3
Explanation: The initial sum of nums is equal to 3 + 8 + 20 = 31.
The following is one of the ways to reduce the sum by at least half:
Pick the number 20 and reduce it to 10.
Pick the number 10 and reduce it to 5.
Pick the number 3 and reduce it to 1.5.
The final array is [1.5, 8, 5] with a total sum of 1.5 + 8 + 5 = 14.5. 
The sum of nums has been reduced by 31 - 14.5 = 16.5, which is at least half of the initial sum, 16.5 >= 31/2 = 15.5.
Overall, 3 operations were used so we return 3.
It can be shown that we cannot reduce the sum by at least half in less than 3 operations.


Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 107
"""

"""
LOGIC

What is the best way to choose numbers to halve?
We want to minimize the steps, so we want to maximize the amount we reduce nums by at each step.
This means at any given moment, we should choose the largest element.
To track the largest element at any given time, let's convert the input into a max heap.
At each step, we pop the maximum x off, remove x / 2 from the sum, and then push x / 2 back onto the heap.

This is another great example of when to use a heap - we need to find the max element repeatedly.
Like in the previous example, it's not enough to just sort the input descending and go through the elements in order,
because elements are added back in after being halved.
"""


# Time - O(n*logn)
# Space - O(n)
import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        ans = 0
        while target > 0:
            ans += 1
            x = heapq.heappop(heap)
            target += x / 2
            heapq.heappush(heap, x / 2)
        
        return ans
    

# My Solution
# Time - O(n*logn)
# Space - O(n)
from heapq import *
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # Using a max heap and will init total to be 0
        # First calculate the initial sum and save it for comparison
        # Get the max value from the heap and divide by 2
        # Repeat step 3 till the sum of the current array is less than the initial sum
        # Loop ends once current_sum <= half
        # Every time we perform the operation increate the total by 1

        initial_sum = sum(nums)
        target = initial_sum / 2
        total = 0
        current_sum = initial_sum
        heap = [-num for num in nums]
        heapify(heap)
        
        while current_sum > target:
            max_num = -heappop(heap)
            max_num /= 2
            current_sum -= max_num
            heappush(heap, -max_num)
            total += 1

        return total
        
        