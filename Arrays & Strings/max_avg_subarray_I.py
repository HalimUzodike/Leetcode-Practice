# Maximum Average Subarray I

"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000



Constraints:
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Fixed sliding window
        # We will first build the inital array (size k) and find the avg.
        # For the values in the remaining arrays we will compute the current total
        # We will find the maximum total
        # We will use the maximum total to find the maximum average

        curr = avg = maxCurr = maxAvg = 0

        for i in range(k):
            curr += nums[i]

        avg = curr / k
        maxCurr = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]   # Subtract the value at i - k from the value at i
            maxCurr = max(maxCurr, curr)

        maxAvg = max(avg, maxCurr / k)
        return maxAvg
