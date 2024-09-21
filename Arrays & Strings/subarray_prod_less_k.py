# Subarray Product Less Than K


# Given an array of integers nums and an integer k,
# return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.


# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Init the left pointer, answer and the current product
        # If the product of every number (*1) in the window is less than 100 we increase the window
        # While the product is equal to or greater than 100 then we will reduce the window size
        # We reduce the size of the window by incrementing the left pointer
        # Must not forget to remove the previous left value by using curr /= nums[left]
        # Each time we pass the validity check we will increment answer by the window size.
        # The window size can be computed by (right - left + 1)

        if k <= 1:
            return 0

        left = answer = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]

            while curr >= k:
                curr /= nums[left] # Must not forget to remove the previous left value
                left += 1 # reducing the window size

            # If we pass the validity check
            answer += right - left + 1 # Add the size of the window

        return answer
